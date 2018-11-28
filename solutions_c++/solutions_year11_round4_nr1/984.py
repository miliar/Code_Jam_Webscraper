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
#include <string.h>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long 
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

vector<int> SplitInt(string &s)
{
	vector<int>Res;int tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

vector<string> SplitStr(string &s)
{
	vector<string>Res;string tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

//////////////////////////////////////////////////////////////
double T[1100000];
int e[1000],f[1000],S[1000],wi[10000];
int main ()
{
	int c,x,s,r,t,n;
	scanf ("%d",&c);
	FOR(cas,1,c)
	{
		//TODO
		double res=0;
		scanf ("%d%d%d%d%d",&x,&s,&r,&t,&n);
		
		
		vector< pair<int,double> > v;
       double sum=0;
       REP(i,n)
       {
         scanf("%d%d%d",&e[i],&f[i],&wi[i]);
         sum+=(f[i]-e[i]);
         v.PB(make_pair(wi[i],f[i]-e[i]));
       }
       v.PB(make_pair(0,x-sum));
       SORT(v);
       ///gogogogogog
       double Tot=t; 
       REP(i,SZ(v))
       {
          if (Tot>0)        
          {
            double tmp=min(Tot,v[i].second/(double)(r+v[i].first)); 
            res+=tmp;
            v[i].second-=tmp*(double)((r+v[i].first));
            Tot-=tmp;
            res+=v[i].second/(s+v[i].first);
          }
          else
          res+=v[i].second/(s+v[i].first);
          
       }
       printf("Case #%d: %lf\n",cas,res);

	}
	return 0;
}



