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

const string PROBLEM_NAME = "B-small-attempt2";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}

int n, T, P;
int a[2048];
int c[20][2048];

LL solve(){
	LL ret = 0;
	for (int i = P - 1; i >= 0; i--){
		int k = 1 << (P - 1 - i);
		int len = 1 << (i + 1);
		int t = 0;
		REP(j, k){
			bool ok = true;
			FOR(j2, t, t + len - 1){
				if (a[j2] > 0){ok = false; break;}
			}
			if (!ok){
				ret ++;
				FOR(j2, t, t + len - 1){
					if (a[j2] > 0) a[j2]--;
				}
			} else 
				cout << "";
			t += len;
		}
	}
	return ret;
}

void m_main(){
	cin >> T;
	REP(step, T){
		memset(a, 0, sizeof(a));
		cin >> P; n = 1 << P;
		REP(i, n) {
			cin >> a[i];
			a[i] = P - a[i];
		}
		REP(i, P){
			int k = 1 << (P - 1 - i);
			int t;
			REP(j, k) cin >> t;
		}
		cout << "Case #" << step + 1 << ": " << solve() << endl;
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}