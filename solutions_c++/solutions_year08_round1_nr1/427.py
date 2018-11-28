#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <list>
#include <stack>
#include <queue>
#include <vector>
#include <deque>
#include <set>
#include <map>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<double> VD;
typedef pair<double,double> PDD;

const int PINF = 1<<30;
const int NINF = -PINF;
const double EPSILON = 1e-10;
const double PI = M_PI;

#define ALL(a) (a).begin(), (a).end()
#define FOR(i,a,b) for (int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for (int i=(a)-1,_b(b); i>=_b; --i)
#define FORV(i,v) for (int i=0; i<(v).size(); ++i)
#define ABS(a) ((a)>0?(a):-(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define mp make_pair
#define pb push_back
#define sz size()
#define sqr(a) (a)*(a)
#define pow2(n) (1<<(n))
#define has(a,k) ((a).find(k)!=(a).end())



int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin >> T;
	FOR(ttt,1,T+1)
	{
		cout << "Case #" << ttt << ": ";
		int N;
		cin >> N;
		vector<LL> v1(N),v2(N);
		FOR(i,0,N) cin >> v1[i];
		FOR(i,0,N) cin >> v2[i];
		
		deque<LL> v1n,v1p,v2n,v2p;
		FOR(i,0,N) 
		{
			
			if (v1[i]<=0) v1n.pb(v1[i]); else v1p.pb(v1[i]);
			if (v2[i]<=0) v2n.pb(v2[i]); else v2p.pb(v2[i]);
		}
			LL r=0;
			sort(ALL(v1n));
			sort(ALL(v1p));
			sort(ALL(v2n));
			sort(ALL(v2p));
	
			while(!v1n.empty())
			{
				if (v2p.empty()) break;
				r+=v1n.front()*v2p.back();
				v1n.pop_front(); v2p.pop_back();
			}
			
			while(!v2n.empty())
			{
				if (v1p.empty()) break;
				r+=v2n.front()*v1p.back();
				v2n.pop_front(); v1p.pop_back();
			}

			if (!v1n.empty() && !v2n.empty())
			{
				while (!v1n.empty())
				{
					r+= v1n.front()*v2n.back();
					v1n.pop_front(); v2n.pop_back();
				}
			}
			else
			{
				while (!v1p.empty())
				{
					r+= v1p.front()*v2p.back();
					v1p.pop_front(); v2p.pop_back();
				}
			}
			cout << r << endl;
	}
	
	return 0;
}