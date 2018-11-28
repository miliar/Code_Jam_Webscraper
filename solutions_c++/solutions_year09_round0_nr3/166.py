#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

int solveIt(const char *c) {
	vector<int> ct(19, 0);
	for (const char *p = c; *p >= ' '; p++) {
		switch (*p) {
		case 'w': ct[0]++; break;
		case 'e': ct[ 1] = (ct[ 1]+ct[ 0])%10000;
			  ct[ 6] = (ct[ 6]+ct[ 5])%10000;
			  ct[14] = (ct[14]+ct[13])%10000; break;
		case 'l': ct[ 2] = (ct[ 2]+ct[ 1])%10000; break;
		case 'c': ct[ 3] = (ct[ 3]+ct[ 2])%10000;
			  ct[11] = (ct[11]+ct[10])%10000; break;
		case 'o': ct[ 4] = (ct[ 4]+ct[ 3])%10000;
			  ct[ 9] = (ct[ 9]+ct[ 8])%10000;
			  ct[12] = (ct[12]+ct[11])%10000; break;
		case 'm': ct[ 5] = (ct[ 5]+ct[ 4])%10000;
			  ct[18] = (ct[18]+ct[17])%10000; break;
		case ' ': ct[ 7] = (ct[ 7]+ct[ 6])%10000;
			  ct[10] = (ct[10]+ct[ 9])%10000;
			  ct[15] = (ct[15]+ct[14])%10000; break;
		case 't': ct[ 8] = (ct[ 8]+ct[ 7])%10000; break;
		case 'd': ct[13] = (ct[13]+ct[12])%10000; break;
		case 'j': ct[16] = (ct[16]+ct[15])%10000; break;
		case 'a': ct[17] = (ct[17]+ct[16])%10000; break;
		}
	}
	return ct[18];
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		char sz[512];
		fgets(sz, 512, stdin);

		long long res = solveIt(sz);
		printf("Case #%d: %04lld\n", cn, res);
	}
	return 0;
}

