#define _CRT_SECURE_NO_DEPRECATE

//[C++]
#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>

//[STL]
#include <vector>
#include <map>
#include <string>

//[STL Macro]
#define all(v) (v).begin(), (v).end()
#define pb push_back


//[MACRO]
#define fori(a) for(int i = 0; i < a; i++)

//[Types]
using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<string, int> psi;
typedef map<string, int> msi;

typedef long long int64;

//[Get data]
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[10240]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }




int main(int argc, char **argv)
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    
    int cases = ni();
    
    for(int count = 1; count <= cases; count++)
    {
      int h = ni();
      int w = ni();
      
      vs pic;
      
      for(int i = 0; i < h; i++)
      {
	pic.pb(ns());
      }
      
      printf("Case #%d:\n", count);
      
      int blue = 0;
      
      for(int i = 0; i < h; i++)
      {
	for(int j = 0; j < w; j++)
	{
	  if('#' == pic[i].at(j))
	  {
	    blue++;
	  }
	}
      }
      
      if(0 != blue%4)
      {
	printf("%s\n", "Impossible");
	continue;
      }
      
      bool trig = true;
      
      for(int i = 0; i < h; i++)
      {
	for(int j=0; j<w; j++)
	{
	  if('#' == pic[i].at(j))
	  {
	    if(j<(w-1) && i<(h-1))
	    {
	      if('#' == pic[i].at(j+1) && '#' == pic[i+1].at(j) && '#' == pic[i+1].at(j+1))
	      {
		(pic[i])[j] = '/';
		(pic[i])[j+1] = '\\';
		(pic[i+1])[j] = '\\';
		(pic[i+1])[j+1] = '/';
	      }
	    }	    
	  }
	}
      }
      
      for(int i = 0; i < h; i++)
      {
	for(int j=0; j < w; j++)
	{
	  if('#' == pic[i].at((j)))
	  {
	    trig = false;
	  }
	}
      }
      
      if(!trig)
      {
	printf("%s\n", "Impossible");
      }
      else
      {
	for(int i = 0; i < h; i++)
	{
	  printf("%s\n", pic[i].c_str());
	}
      }
      
    }
    
      
    return 0;
}
