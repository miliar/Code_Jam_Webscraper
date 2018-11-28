#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<memory>
#include<string>
#include<vector>
#include<cctype>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

typedef unsigned long long		ui64;
typedef long long				i64;
typedef	vector<int>				vi;
typedef	vector<string>			vs;
typedef	pair<int,int>			pii;
typedef	pair<double,double>		point;

#define pb						push_back
#define mp						make_pair
#define X						first
#define Y						second
#define all(a)					(a).begin(), (a).end()
#define INF						(2000000000)


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int tests;
	scanf("%d",&tests);

	for(int test=0;test<tests;test++){
		printf("Case #%d: ", test+1);

		int x,S,R,n; double t;
		cin >> x >> S >> R >> t >> n;
		vi W,L;
		int FreeL = x;
		vector< pair< double, int> > a;
		for(int i=0;i<n;i++){
			int b,e,w;
			cin >> b >> e >> w;
			L.pb(e-b);
			W.pb(w);
			double q1 = (e-1.0*b)/(w+R);
			double q2 = (e-1.0*b)/(w+S);
			double q = q2/q1;
			a.pb( mp(q,i) );
			FreeL -= (e-b);
		}
		
		double q1 = 1.0*FreeL/R;
		double q2 = 1.0*FreeL/S;
		a.pb( mp(q2/q1,n) );
		W.pb(0);
		L.pb(FreeL);
		n++;
		sort( a.rbegin(),a.rend() );
		double ans = 0;
		for(int i=0;i<n;i++){
			int top = a[i].second;
			double tx = 1.0*L[top]/(W[top]+R);
			if(tx>t){
				double xx = (W[top] + R)*t;
				double yx = L[top] - xx;
				ans += xx/(W[top] + R);
				ans += yx/(W[top] + S);
				t = INF;
				R = S;
			}
			else{
				ans += tx;
				t -= tx;
			}
		}
		printf("%.7f\n", ans);
	}

	return 0;
}