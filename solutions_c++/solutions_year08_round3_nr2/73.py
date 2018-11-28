#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>

using namespace std;

int sak[1000];
int T, n, ugly;

void generuok(int vt, long long suma, long long last, int sen) {
// 	cout << sak[vt] << " " << suma << " " << last << " " << sen <<  endl;
	long long lst = last * 10 + sak[vt];
	long long  s;
	if (sen == 0 || sen == -1) s = suma + lst;
	if (sen == 1) s = suma - lst;
	if (vt == n - 1) {
		long long k = abs(s);
// 		cout << k << endl;
		if (k % 2 == 0 || k % 3 == 0 || k % 5 == 0 || k % 7  == 0) ugly++;
	}
		else {
			for (int i = 0; i < 3; i++) {
				if (i == 0 || i == 1) generuok(vt + 1, s, 0, i);
				if (i == 2) generuok(vt + 1, suma, lst, sen);
			}
		}
}		
	

int main() {
	freopen("bsmall.in", "r", stdin);
	freopen("bsmall.out", "w", stdout);
	scanf("%d", &T);
	char buf[1000];
	string g;
	for (int e = 0; e < T; e++) {
		scanf(" %s", &buf); g = buf;
		n = g.size();
		ugly = 0;
		for (int i = 0; i < g.size(); i++)
			sak[i] = g[i] - '0';
		generuok(0, 0, 0, -1);
		printf("Case #%d: %d\n", e + 1, ugly);
	}
	return 0;
}