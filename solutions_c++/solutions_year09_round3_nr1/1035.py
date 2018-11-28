#include <cstdio>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <iomanip>
#include <math.h>

using namespace std;

typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<int> vll;
typedef vector<string> vs;

#define FORITER(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORI(n) FOR(i,0,n)
#define FORJ(n) FOR(j,0,n)
#define FORK(n) FOR(k,0,n)
#define MEM(var, v) memset(var, v, sizeof(var))
#define GETINT(row,col,q) FORI(row) FORJ(col) cin >> q[i][j]
#define GETCHAR(row,col,q) FORI(row) {string line; cin >> line; FORJ(col) q[i][j]=line.at(j);}
#define TESTOUT FORI(T) cout << "Case #" << i+1 << ": "
#define DBG(mi,mj,q) FORI(mi){FORJ(mj){ cout << q[i][j];} cout << endl;}

enum DIR {UP, LEFT, RIGHT, DOWN};
int T, R, C = 0;
// int Q[][];
// char Q[][];
enum STAT { NON = -1 };

int Q[40];

ll play()
{
	string line;
	getline(cin, line);

	MEM(Q, NON);

	int lineLen = (int)(line.length());

	int idx = 0;
	char ch;
	int seq = 1;
	FORI((int)(line.length())) {
		ch = line[i];
		if(ch <= '9')
			idx = ch - '0';
		else
			idx = ch - 'a' + 10;
		if(Q[idx] == NON) {
			if(seq == 1) {
				Q[idx] = 1;
				++seq;
			}
			else if(seq == 2) {
				Q[idx] = 0;
				++seq;
			}
			else {
				Q[idx] = seq - 1;
				++seq;
			}
		}
	}

	int base = 0;
	FORI(36) {
		if(Q[i] != NON)
			++ base;
	}
	if(base < 2)
		base = 2;

	//convert symbol to digit
	FORI((int)(line.length())) {
		ch = line[i];
		if(ch <= '9')
			idx = ch - '0';
		else
			idx = ch - 'a' + 10;

		line[i] = Q[idx] + '0';
	}
//cout << "* NUM:  [" << line << "] BASE: " << base << endl;
	ll ans = 0;
	int num = 0;
	FORI(lineLen) {
		num = line[i] - '0';
		if (num == 0) continue;
		int th = 1;
		FORJ(lineLen-i-1)
			th *= base;
		if(i == lineLen-1)
			ans += (ll)num;
		else
			ans += (ll)num * (ll)th;
	}
	return ans;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin >> T;
	string line; getline(cin, line);
	TESTOUT << play() << endl;
	return 0;
}
