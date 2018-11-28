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

vector<int> readVI(int n = 0) {
	if (!n) scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

long long solveIt(int R, int N, vector<int> &gi) {
	vector<int> seen(gi.size(), -1);
	vector<int> start;
	vector<long long> count;
	long long ct = 0; int p = 0;
	for (int i = 0; i < gi.size(); i++) {
		if (seen[p] >= 0) break;
		seen[p] = i;
		start.push_back(p);
		count.push_back(ct);
		int j = p;
		long long tct = 0;
		while (j < gi.size() && tct+gi[j] <= N) tct += gi[j++];
		if (j == gi.size()) {
			j = 0;
			while (j < p && tct+gi[j] <= N) tct += gi[j++];
		}
		ct += tct;
		p = j;
	}
	ct -= count[seen[p]];
	int loopsize = start.size()-seen[p];
//	printf("loop repeats starting with %d\n", p);
//	printf("start.size() %d, seen[%d] %d\n", start.size(), p, seen[p]);
//	printf("R %d -> %d\n", R, R-seen[p]);
	R -= seen[p];
	long long res = (R/loopsize)*ct + count[R%loopsize+seen[p]];
//	printf("res = %Ld + (%d/%d)*%Ld = %Ld + count[%d%%%d+%d] = %Ld) = %Ld\n", count[seen[p]], R, loopsize, ct, R/loopsize*ct, R, loopsize, seen[p], count[R%loopsize+seen[p]], res);
	return res;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int R, N;
		scanf("%d %d ", &R, &N);
		vector<int> gi = readVI();

		long long res = solveIt(R, N, gi);
		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

