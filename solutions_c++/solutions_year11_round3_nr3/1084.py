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
	int N = ni();
	int L = ni();
	int H = ni();
	
	vi notes;
	
	for(int i = 0; i < N; i++)
	{
	    notes.pb(ni());
	}
	
	bool trig  = true;	
	int harmony = 0;
	int64 total = 0;
	
	for(int i = L; i <= H; i++)
	{
	  total = 0;
	  harmony = 0;
	  
	  trig = true;
	  
	  for(int j = 0; j < N; j++)
	  {
	    if(0 == notes[j]%i || 0 == i%notes[j])
	    {
	      harmony = i;
	      total++;
	    }
	    else
	    {
	      trig = false;	      
	    }    
	    
	  }
	  
	  if(trig && total == N)
	  {
	    break;
	  }
	  
	  //break;
	}
	
	if(trig)
	{
	  printf("Case #%d: %d\n", count, harmony);
	}
	else
	{
	  printf("Case #%d: %s\n", count, "NO");
	}
	
	
	
	
      }
    
    
      
    return 0;
}
