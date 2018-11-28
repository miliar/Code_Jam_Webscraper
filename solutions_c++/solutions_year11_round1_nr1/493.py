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
#include <regex.h>  
using namespace std; 
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs;
#define pb push_back 
#define sz(v) ((int)(v).size()) 
 
long long ggd(long long a, long long b)
{
  if(a==0) return b;
  return ggd(b%a,a);
}



long long vandaag(int p)
{
  return 100/ggd(p,100);
}


int main()
{
  int i=0,j=0,k=0; char buf[1000]="";

  int runs,run;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++)
  {
    printf("Case #%d: ",run);
    long long n,pd,pg;
    scanf("%lld %lld %lld",&n,&pd,&pg);

    if(pg==0)
    {
      if(pd!=0) { printf("Broken\n"); continue; }
      else { printf("Possible\n"); continue; }
    } 
    else if(pg==100)
    {
      if(pd!=100||vandaag(pd)>n) { printf("Broken\n"); continue; }
      else { printf("Possible\n"); continue; }
    }
    else
    {
      if(vandaag(pd)>n) printf("Broken\n"); 
      else printf("Possible\n");
    }

  }

  return 0;
}
