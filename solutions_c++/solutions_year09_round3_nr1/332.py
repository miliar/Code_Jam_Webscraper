#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <numeric> 
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 


int conv(int i)
{
  if(i<=1) return 1-i;
  return i;
}


bool isin(string in, char k)
{
  for(int j=0;j<sz(in);j++) 
    if(in[j]==k)
      return true;
  return false;
}


int cijfs(string in)
{
  string bouw;
  for(int i=0;i<sz(in);i++)
    if(!isin(bouw,in[i]))
      bouw+=in[i];
  return max(2,sz(bouw));  
}


long long macht(int b, int n)
{
  long long uit=1;
  for(int j=0;j<n;j++)
    uit=uit*b;
  return uit;
}


int afb[128];

long long waarde(string in,int base)
{
  memset(afb,-1,sizeof(afb));
  int i,j,k;
  long long uit=0;

  int gezien=0;
  for(i=0;i<sz(in);i++)
  {
    if(afb[int(in[i])]==-1)
    { afb[in[i]]=conv(gezien); gezien++; }

    long long m=macht(base,sz(in)-1-i);

    uit+=m*afb[in[i]];
  }


  return uit;

}





int main()
{
  int i,j,k;
  char buf[1000];


  int N;
  scanf("%d",&N);
  for(int run=1;run<=N;run++)
  {
    scanf("%s",buf);
    string S=buf;

    long long mini=1000000; mini=mini*mini*mini+1;

    int b=cijfs(S);

    printf("Case #%d: %lld\n",run,waarde(S,b));
  }


  return 0;
}

