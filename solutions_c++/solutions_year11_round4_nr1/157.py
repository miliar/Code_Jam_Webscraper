#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <functional>
#include <sstream>
#include <iostream>
#include <ctime>
#include <algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define _foreach(it, b, e) for(__typeof__(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll; // sao dois L's!!!
const double eps = 1e-9;


int x,s,r;
int n;
double t;
struct pedaco {
  int a,b;
  int v;
}lis[2111];
vector<pair<double, double> > trecho;
bool comp (pedaco a, pedaco b)
{
  return a.a<b.a;
}
int main()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      trecho.clear();
      scanf("%d %d %d %lf %d",&x,&s,&r,&t,&n);
      for(int i=0;i<n;i++)
	{
	  int a,b,c;
	  scanf("%d %d %d",&a,&b,&c);
	  lis[i]= (pedaco) {a,b,c};
	}
      sort(lis,lis+n,comp);
      pedaco fim = (pedaco) {x,x,inf};
      lis[n++]=(fim);
      int ant = 0;
      for(int i=0;i<n;i++)
	{
	  trecho.push_back(make_pair(s, lis[i].a-ant));
	  trecho.push_back(make_pair(s+lis[i].v, lis[i].b-lis[i].a));
	  ant = lis[i].b;
	}
      sort(all(trecho));
      double best = 0;
      for(int i=0;i<trecho.size();i++)
	{
	  //	  printf("%lf %lf\n",trecho[i].first,trecho[i].second); 
	  if(trecho[i].second>eps)
	    {
	      if(trecho[i].second/(trecho[i].first+r-s) > t)
		{
		  best += (trecho[i].second - (trecho[i].first+r-s)*t)/trecho[i].first;
		  best += t;
		  t=0;
		}
	      else
		{
		  t-=trecho[i].second/(trecho[i].first+r-s);
		  best+=trecho[i].second/(trecho[i].first+r-s);
		}
	    }
	}
      printf("Case #%d: %.7lf\n",pp,best);
    }
  return 0;
}
