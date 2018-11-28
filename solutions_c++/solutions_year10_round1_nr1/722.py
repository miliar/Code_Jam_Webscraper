#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i)
#define ALL(cont) cont.begin(), cont.end()

using namespace std;

typedef long long ll;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<ll> vl;
typedef vector<double> vd;

bool find_row(const vs &d, char c, int K)
{
	int N = d.size();
	vii b[4];
	REP(i,4) b[i].resize(N, vi(N, 0));
	REP(i,N)REP(j,N)
	{
		if(d[i][j] == c)
		{
			b[0][i][j] = 1 + (j>0 ? b[0][i  ][j-1] : 0);
			b[1][i][j] = 1 + (i>0 ? b[1][i-1][j  ] : 0);
			b[2][i][j] = 1 + (i>0 && j>0 ? b[2][i-1][j-1] : 0);
			b[3][i][j] = 1 + (i>0 && j+1<N ? b[3][i-1][j+1] : 0);
			REP(k,4) if(b[k][i][j] >= K) return true;
		}
	}
	return false;
}

int main()
{
	int T;
	cin >> T;
	REP(t,T)
	{
		int N, K;
		cin >> N >> K;
		vs d(N);
		REP(i,N) cin >> d[i];
		REP(i,N) stable_partition(ALL(d[i]), bind2nd(equal_to<char>(), '.'));
		int ans = 0;
		ans |= find_row(d, 'R', K) ? 1 : 0;
		ans |= find_row(d, 'B', K) ? 2 : 0;
		const char* word[] = {"Neither", "Red", "Blue", "Both"};
		printf("Case #%d: %s\n", t + 1, word[ans]);
	}
	
	return 0;
}
