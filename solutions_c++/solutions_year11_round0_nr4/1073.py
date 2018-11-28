#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)

#define ll long long
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
bool mark[1111];
vector<int> perm;
int dfs(int node)
{
	if(mark[node]) return 0;
	mark[node] = true;
	int r = 1;
	return r + dfs(perm[node]);
}
double dp[1111];
double FF[1111][2];
double doit(int n);
double F(int n, int tope)
{
	double &res = FF[n][tope];
	if( n <= 1 ) return 0.;
	if( res >= 0. ) return res;
	
	res = 0.;
	double prob = 1.;
	for( int k = 1 ; k < n ; k ++ )
	{
		// double prob = .;
		
		prob /= (double)k;
		double prob2 = prob * (1./(double)n);
		
		res +=  prob2 * (doit(k)) + F(n-k, 0);
	}
	if(!tope)
	{
		res += (1./(double)n) * doit(n);
	}
// 	cout << n << "  " << tope << "  " << res << endl;
	return res;
}



double doit(int n)
{
	double & res = dp[n];
	if( n <= 1 ) return res = 0.;
	if( res >= 0. ) return res;
	
	res = (1.+F(n,1)) *((double)n/(double)(n-1));

	return res;
}


int main()
{
	int i,j ,k;
	int casos; cin >> casos;
	memset(dp, -1, sizeof(dp));
	memset(FF, -1, sizeof(FF));
	for( int h = 0 ; h < casos ; h ++ )
	{
		int N;
		cin >> N;
		perm.clear();
		for( i = 0 ; i < N ; i ++ )
		{
			cin >> k; k--; perm.PB(k);
		}
		memset(mark, false, sizeof(mark));
		double res = 0.;
		for( i = 0 ; i < N ; i ++ )
		{
			if(!mark[i])
			{
				int cant = dfs(i);
// 				cout << cant << endl;
				if( cant > 1 )res += cant;
			}
		}
		printf("Case #%d: %.10lf\n", h+1, res);
	}
	
	return 0;
}