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
string readLine();
int readIntLine();
vector<int> readVI(int n);
vector<string> readVS(int n);
vector<int> itokens(string s, string sep);
vector<string> stokens(string s, string sep);

bool solveIt(long long N, int pd, int pg) {
//	if (pd > pg) return false;
/*	if (pd < 100 && pg == 100) return false;
	if (pd == 0 && pg == 0) return true;
	for (int d = 1; d <= N; d++) {
		for (int a = 1; a <= d; a++) {
			int b = d-a;
			for (int c = 0; c <= a; c++) if (c*100 == a*pd) {
				for (int x = 0; x <= b; x++) if (x*100 == b*pg) return true;
			}
		}
	}*/
	for (int a = 1; a <= N; a++) if (!(a*pd%100)) {
		int x = a*pd/100;
//		printf("x = %d\n", x);
//		printf("%d/%d*100 = %d\n", x, a, pd);
		for (int b = 0; b < 100*N; b++) {
			int z = pg*(a+b)-a*pd;
			if (z >= 0 && !(z%100) && b*100 >= z) {
				int y = z/100;
//				printf("y = %d\n", y);
//				printf("(%d+%d)/(%d+%d) * 100 = %d\n", x, y, a, b, pg);
				return true;
			}
		}
	}
/*	for (int a = 1; a <= N; a++) for (int x = 0; x <= a; x++) {
		if (x*100 == a*pd) {
			for (int b = 0; b+a <= N; b++) for (int y = 0; y <= b; y++) {
				if ((x+y)*100 == (a+b)*pg) {
					return true;
				}
			}
		}
	}*/
	return false;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		long long N; int pd, pg;
		scanf("%Ld %d %d", &N, &pd, &pg);

		if (N > 100) N = 100;
		bool res = solveIt(N, pd, pg);
		printf("Case #%d: %s\n", cn, res?"Possible":"Broken");
	}
	return 0;
}








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
vector<int> readVI(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}
vector<string> readVS(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<string> v(n);
	for (int i = 0; i < n; i++) v[i] = readLine();
	return v;
}
vector<string> stokens(string s, string sep = " \n\r\t") {
	vector<string> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(s.substr(start, end-start));
	}
	return res;
}
vector<int> itokens(string s, string sep = " \n\r\t") {
	vector<int> res;
	int start, end = 0;
	while ((start = s.find_first_not_of(sep, end)) != string::npos) {
		end = s.find_first_of(sep, start);
		res.push_back(atoi(s.substr(start, end-start).c_str()));
	}
	return res;
}

