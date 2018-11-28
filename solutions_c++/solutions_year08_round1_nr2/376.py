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
	int C;
	cin >> C;
	FOR(ccc,1,C+1)
	{
		cout << "Case #" << ccc << ": ";
		
		int N,M;
		cin>> N >> M;

		vector<VPII> A(M);
		FOR(i,0,M)
		{
			int n; cin >> n;
			FOR(j,0,n)
			{
				int a,b;
				cin >> a >> b;
				A[i].pb(mp((a-1),b));
			}
		}
		
		VI min;
		int minc=PINF;

		FOR(n,0,(1<<N))
		{
			VI B;
			FOR(i,0,N) B.pb( (n & (1<<i))?(1):(0) );

			int fal=0;
			FOR(c,0,M)
			{
				int f=0;
				FOR(i,0,A[c].sz) if (B[A[c][i].first]==A[c][i].second) {f=1; break;}
				if (!f) {fal = 1; break;}
			}
			if (!fal)
			{
				int y=0; FOR(i,0,N) y+=B[i];
				if (y<minc) { min = B; minc=y;}
			}
		}
		if (minc==PINF) cout << "IMPOSSIBLE" << endl;
		else 
		{
			FOR(i,0,N) cout << min[i] << " ";
			cout << endl;
		}
	}
	
	
	return 0;
}