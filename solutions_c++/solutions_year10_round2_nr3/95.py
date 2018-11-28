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

const string PROBLEM_NAME = "C-large";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());
const int MAXN = 502;
const int MODULO = 100003;
LL d[MAXN][MAXN];
LL c[MAXN][MAXN];
LL a[MAXN];
int n;

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}

void computeCK(){
	REP(i, n + 1) c[i][0] = 1;
	FOR(i, 1, n) c[i][1] = i;
	FOR(k, 2, n){
		FOR(i, k, n) {
			c[i][k] = c[i - 1][k] + c[i - 1][k - 1];
			c[i][k] %= MODULO;
		}
	}
}

void precompute(){
	n = 500;
	computeCK();
	FOR(i, 2, n) d[i][1] = 1;
	a[2] = 1; 

	FOR(i, 3, n){
		for (int len = 2; len < i; len++){
			for (int k = 0; k <= i - 1 - len; k++){
				d[i][len] += d[len][len - 1 - k] * c[i - 1 - len][k];
				d[i][len] %= MODULO;
			}	
		}
		for (int len = 1; len < i; len++){
			a[i] += d[i][len];
			a[i] %= MODULO;
		}
	}
}

void m_main(){
	precompute();
	int T;
	cin >> T;
	REP(i, T){
		int x; cin >> x;
		cout << "Case #" << i + 1 << ": " << a[x] << endl;
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}