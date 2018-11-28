#include <iostream>
#include <sstream>  
#include <cstring>
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

struct interval
{
  int length;
  int wi;
};

bool operator<(const interval &a, const interval &b)
{
  return a.wi<b.wi;
}


int main()
{
  int i,j,k;
  int a,b,c;

  int run,runs;
  scanf("%d",&runs);

  for(int kees=1;kees<=runs;kees++)
  {
    printf("Case #%d:",kees);

    int X,S,R,t,N;
    int Bi,Ei,wi;

    scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
    interval q;
    int totaal=0;
    vector<interval> V;

    for(i=0;i<N;i++)
    {
      scanf("%d %d %d",&Bi,&Ei,&q.wi);
      q.length=Ei-Bi;
      totaal+=q.length;
      V.pb(q);
    }
    q.length=X-totaal;
    q.wi=0;
    V.pb(q);
    sort(V.begin(),V.end());

    double tijd=0;
    double T=t;
    for(j=0;j<sz(V);j++)
    {
      double groverentijd=double(V[j].length)/(R+V[j].wi);
      double rentijd=min(T,groverentijd);
      T-=rentijd;
      tijd+=rentijd;
      double rest=V[j].length-rentijd*(R+V[j].wi);
      tijd+=rest/(S+V[j].wi);
    }
    printf(" %.9lf\n",tijd);
  }




  return 0;
}
