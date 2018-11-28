
//include
//------------------------------------------
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <istream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#include <stdio.h>
#include <memory.h>
#include <math.h>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//math
//-------------------------------------------
template<class T> inline T sqr(T x) {return x*x;}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<long long> VLL;
typedef vector<VI> VVI;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;

//container util
//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define RFOR(i,a,b) for(int i=(a)-1;i>=(b);--i)
#define REP(i,n)  FOR(i,0,n)

//constant
//--------------------------------------------
const double EPS = 1e-10;
const double PI  = acos(-1.0);

//clear memory
#define CLR(a) memset((a), 0 ,sizeof(a))

//debug
#ifdef DEBUG
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define print(x) cerr << x << endl;
#else
#define dump(x) ;
#define debug(x) ;
#define print(x) ;
#endif

int ni(){
	int a;
	scanf("%d", &a);
	return a;
}

double nf(){
	double d;
	scanf("%lf", &d);
	return d;
}

long long nll(){
	long long l;
	scanf("%lld", &l);
	return l;
}

VI nvi(int num){
	VI v;
	FOR(i, 0, num){
		v.push_back(ni());
	}
	return v;
}

VD nvf(int num){
	VD v;
	FOR(i, 0, num){
		v.push_back(nf());
	}
	return v;
}

VLL nvll(int num){
	VLL v;
	FOR(i, 0, num){
		v.push_back(nf());
	}
	return v;
}

char sbuf[10000];
string ns(){
	scanf("%s", sbuf);
	return sbuf;
}

char table[20][20];

int calc(int r, int c, int size){
	int rw = 0;
	int sum = 0;
	int cw = 0;

	for(int i = 0; i < size; i++){
		for(int j = 0; j < size; j++){
			rw += i * table[r + i][c + j];
			cw += j * table[r + i][c + j];
			sum += table[r + i][c + j];
		}
	}

	rw -= (size - 1) * (table[r + size - 1][c] + table[r + size - 1][c + size - 1]);
	cw -= (size - 1) * (table[r][c + size - 1] + table[r + size - 1][c + size - 1]);
	sum -= (table[r][c + size - 1] + table[r + size - 1][c]);
	sum -= (table[r][c] + table[r + size - 1][c + size - 1]);

	if(rw == cw && cw == sum * (size - 1) / 2) return 1;
	return 0;
}

int run(){
	FOR(i, 0, 20) FOR(j, 0, 20) table[i][j] = 0;
	int R, C, D;

	cin >> R >> C >> D;

	FOR(i, 0, R) FOR(j, 0, C){
		char c;
		cin >> c;
		table[i][j] = c - '0';
	}

	
	for(int size = min(R, C); size >= 3; size--){
		for(int i = 0; i <= R - size; i++){
			for(int j = 0; j <= C - size; j++){
				if(calc(i, j, size)) return size;
			}
		}

	}
	return 0;
}

int main(void){
    freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-large.in", "r", stdin);
	//freopen("a.txt", "r", stdin);
    freopen("B.out", "w", stdout);

	int cases ;
	cin >> cases;

	FOR(i, 1, cases + 1){
		int result = run();
		if(result){
			cout << "Case #" << i << ": " << result << endl;
		}else{
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}


	return 0;
}