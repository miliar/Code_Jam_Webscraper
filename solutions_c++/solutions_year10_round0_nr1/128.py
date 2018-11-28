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

const string PROBLEM_NAME = "A-large";
const string INPUT_FILE = PROBLEM_NAME + ".in";
const string OUTPUT_FILE = PROBLEM_NAME + ".out";

ofstream fout (OUTPUT_FILE.c_str());
ifstream fin (INPUT_FILE.c_str());

int T, n, K;
LL a[100];

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}

void precompute(){
	a[1] = 2;
	FOR(i, 2, 32){
		a[i] = a[i - 1] * 2;
	}
}

void m_main(){
	precompute();
	cin >> T;
	REP(i, T){
		cin >> n >> K;
		cout << "Case #" << (i + 1) << ": ";
		if ((K + 1) % a[n] == 0) cout << "ON";
		else cout << "OFF";
		cout << endl;
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}