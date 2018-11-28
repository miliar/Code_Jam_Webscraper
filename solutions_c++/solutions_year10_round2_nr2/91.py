#include <fstream>
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

#define VI vector<int> 
#define VS vector<string> 
#define LL long long 
#define FOR(i,n,m) for(int i=n;i<=m;i++)
#define REP(i,n) for(int i = 0; i < n; i++)
#define REPD(i,n) for(int i = n - 1; i>=0; i--)
#define BE(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair
#define EPS 0.0000000001
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)

const int INFI = 2000000000;
const int goX[4] = {-1, 0, 1, 0};
const int goY[4] = {0, 1, 0, -1};

const string PROBLEM_NAME = "B-large";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());
const int MAXN = 200;
int n, m, K, T, B, C;
LL x[MAXN], v[MAXN];
double mtime[MAXN];
bool mark[MAXN];
int swaps[MAXN];

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}

void solve(int testNo){
	memset(mark, 0, sizeof(mark));

	int m_count = 0;
	REP(i, n){
		mtime[i] = (double) (B - x[i]) / v[i];
		if (mtime[i] <= T || abs(mtime[i] - T) < EPS) {
			mark[i] = true;
			m_count++;
		}
	}
	cout << "Case #" << testNo << ": ";
	if (m_count < K) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	memset(swaps, 0, sizeof(swaps));

	int m = 0;
	REP(i, n) if (mark[i]){
		int t = 0;
		FOR(j, i + 1, n - 1) if (!mark[j]) t++;
		swaps[m ++ ] = t;
	}
	sort(swaps, swaps + m);
	LL res = 0;
	REP(i, K) res += swaps[i];
	cout << res << endl;
}

void m_main(){
	cin >> C;
	REP(step, C){
		cin >> n >> K >> B >> T;
		REP(i, n) cin >> x[i];
		REP(i, n) cin >> v[i];
		solve(step + 1);
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}