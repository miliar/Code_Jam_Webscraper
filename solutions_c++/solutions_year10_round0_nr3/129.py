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
const LL MAXN = 2000;
LL K, n, R, T;
LL a[MAXN];
int  mark[MAXN];

void read_input(){
	freopen (INPUT_FILE.c_str(),"r",stdin);
	//freopen ("","w",stdout);
	freopen (OUTPUT_FILE.c_str(),"w",stdout);
}

LL cal2(int x, int pointer){
	LL res = 0;
	REP(i, x){
		if (a[pointer] > K) break;
		LL t = a[pointer];
		int start = pointer;
		do {
			if (t + a[(pointer + 1) % n] <= K && (pointer + 1) % n != start){
				t += a[(pointer + 1) % n];
				pointer = (pointer + 1) % n;
			} else break;
		} while (true);
		res += t;
		pointer = (pointer + 1) % n;
	}
	return res;
}

LL cal(){
	//int _maxRn = max(n, R);
	REP(i, n) mark[i] = 0;
	LL sum = 0;
	LL round = 0;
	LL pointer = 0;
	REP(i, R){
		if (mark[pointer]){
			round = i + 1 - mark[pointer];
			break;
		}
		mark[pointer] = i + 1;
		if (a[pointer] > K) break;
		LL t = a[pointer];
		int start = pointer;
		do {
			if (t + a[(pointer + 1) % n] <= K && (pointer + 1) % n != start){
				t += a[(pointer + 1) % n];
				pointer = (pointer + 1) % n;
			} else break;
		} while (true);
		sum += t;
		pointer = (pointer + 1) % n;
	}	

	if (round == 0 || a[pointer] > K) return sum;
	LL initSum = cal2(mark[pointer] - 1, 0);
	sum -= initSum;

	LL res = ((R - mark[pointer] + 1) / round) * sum + initSum;
	R = (R - mark[pointer] + 1) % round;

	res += cal2(R, pointer);

	return res;
}

void m_main(){
	cin >> T;
	REP(i, T){
		cin >> R >> K >> n;
		REP(j, n) cin >> a[j];
		cout << "Case #" << (i + 1) << ": " << cal() << endl;
	}
}

int main(){
	read_input();
	m_main();

	return 0;
}
