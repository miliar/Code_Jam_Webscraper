#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b_);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cout<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
int Eva[24*61];
int Evb[24*61];
int ReadyA[24*61],ReadyB[24*61];
int Tim(string a)
{
  int h,m;
  sscanf (a.c_str(),"%d:%d",&h,&m);
  return h*60+m;
}
int main ()
{
  int c,cas=1;
  //DEB(Tim("01:01"));
  scanf ("%d",&c);
  while (c--)
  {
    int T,na,nb;
    char Ta[100],Tb[100];
    memset(Eva,0,sizeof Eva);
    memset(Evb,0,sizeof Evb);
    memset(ReadyA,0,sizeof ReadyA);
    memset(ReadyB,0,sizeof ReadyB);
    scanf ("%d",&T);
    scanf ("%d%d",&na,&nb);
    REP(i,na)
    {
      scanf ("%s%s",Ta,Tb);
      
      int ta=Tim(Ta);
      int tb=Tim(Tb)+T;
      Eva[ta]++;
      FOR(x,tb,60*24)
      ReadyB[x]++;
      
    }
    REP(i,nb)
    {
      scanf ("%s %s",Ta,Tb);
      int ta=Tim(Ta);
      int tb=Tim(Tb)+T;
      Evb[ta]++;      
      FOR(x,tb,60*24)
      ReadyA[x]++;      
    }
    
    int a=0,b=0;
    REP(i,60*24)
    {
      while  (Eva[i])
      {
        Eva[i]--;
        if (ReadyA[i]>0)
        {
          FOR(x,i,60*24)
            ReadyA[x]--;
        }
        else
        {
         a++;
        }
      }
      
      while (Evb[i])
      {
        Evb[i]--;
        if (ReadyB[i]>0)
        {
          FOR(x,i,60*24)
            ReadyB[x]--;
        }
        else
        {
          //DEB(i);
         b++;
        }
      }
    }
      printf ("Case #%d: %d %d\n",cas++,a,b);
  }
}