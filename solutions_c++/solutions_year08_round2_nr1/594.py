#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cstdio>
using namespace std;
#define debug(a) cout << #a
#define FO(it,a) for(__typeof(a)::iterator it=a.begin();it!=a.end();++it)
#define FZ(i,n) for(long long i=0;i<n;++i)
#define FL(i,s,e) for(long long i=s;i<e;++i)
#define CL(s,t) memset(s,t,sizeof(s))
#define sz size()
#define pb push_back
#define b begin()
#define E end()
#define all(a) a.b,a.E 
#define GI ({int t;scanf("%d",&t);t;})
typedef pair<long long,long long> ii;
typedef vector<long long> vi;
typedef vector<string> vs;
typedef vector<vector<long long> > vvi;
typedef vector<long long> vii;
int main()
{
	int tt = GI;
	FZ(t,tt)
	{
		long long n, A, B, C, D, x0, y0,M ;
		n =GI ;
		A =GI ; B = GI ;C =GI ;D = GI ; x0 = GI ; y0 = GI; M = GI;

		long long X = x0, Y = y0;
		vector<ii> pt;
		pt.pb(ii(X,Y));
		FL(i,1,n)
		{
			 X = (A * X + B)% M;
			  Y = (C * Y + D) %M;
			pt.pb(ii(X,Y));
		}
		sort(all(pt));
		int cnt = 0;
		FZ(i,pt.sz)
		FL(j,i+1,pt.sz)
		FL(k,j+1,pt.sz)
		if((pt[i].first + pt[j].first + pt[k].first)%3==0)
		if((pt[i].second + pt[j].second + pt[k].second)%3==0)
			++cnt;
		cout <<"Case #"<<t+1<<": "<< cnt << endl;
	}
	return 0;
}
