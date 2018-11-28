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
#define SI(a) sizeof(a)
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR_SET(it, type, ss) for (set<type>::iterator it = ss.begin(); it!= ss.end(); it++)

const int INFI = 2000000000;
const int goX[4] = {-1, 0, 1, 0};
const int goY[4] = {0, 1, 0, -1};

const string PROBLEM_NAME = "C-small-attempt0";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}
const int MAXN = 1000;
const int MID = 0;
typedef int arr1[MAXN][MAXN];
arr1 a, b;
int n, T, m;
int n1, m1, n2, m2;

int solve(){
	int ret = 0;
	while (true){
		bool ok = true;
		FOR(i, n1, n2) FOR(j, m1, m2) if (a[i + MID][j + MID] == 1){
			ok = false; break;
		}
		if (ok) 
			return ret;
		ret++;
		FOR(i, n1, n2) FOR(j, m1, m2) {
			if (a[i + MID][j + MID]){
				if (a[i + MID - 1][j + MID] == 0 && a[i + MID][j + MID - 1] == 0)
					b[i + MID][j + MID] = 0;
				else b[i + MID][j + MID] = 1;
			} else if (a[i + MID - 1][j + MID] == 1 && a[i + MID][j + MID - 1] == 1){
				b[i + MID][j + MID] = 1;
			}
		}
		FOR(i, n2 + 1, n2 + 1) FOR(j, m2 + 1, m2 + 1){
			if (a[i + MID - 1][j + MID] == 1 && a[i + MID][j + MID - 1] == 1){
				b[i + MID][j + MID] = 1;
			}
		}
		n2 ++; m2++;
		memcpy(a, b, sizeof(a));
		if (n2 >= MAXN || m2 >= MAXN)
			cout << "AAA";
		//FOR(i, n1, n2) FOR(j, m1, m2) if (a[i + MID][j + MID]) cout <<i << " " << j << endl;
	}
}

void m_main(){
	cin >> T;
	REP(step, T){
		memset(a, 0, sizeof(a));
		cin >> m;
		m1 = n1 = INFI; 
		m2 = n2 = -INFI;
		REP(i, m){
			int x1, y1, x2, y2;
			//cin >> x1 >> y1 >> x2 >> y2;
			cin >> y1 >> x1 >> y2 >> x2;
			FOR(i, x1, x2) FOR(j, y1, y2) a[i + MID][j + MID] = 1;
			n1 = min(n1, x1); n2 = max(n2, x2);
			m1 = min(y1, m1); m2 = max(m2, y2);
		}
		cout << "Case #" << step + 1 << ": " << solve() << endl;
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}