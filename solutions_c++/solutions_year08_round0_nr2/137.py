#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <map>

using namespace std;

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

int getTime() {
	int h, m;
	scanf("%d:%d ", &h, &m);
	return h*60+m;
}

pair<int, int> solveIt(int T, vector<pair<int, int> > &tab,
		vector<pair<int, int> > &tba) {
	sort(tab.begin(), tab.end());
	sort(tba.begin(), tba.end());

	vector<int> ta(1440, 0), tb(1440, 0);

	for (int i = 0; i < tab.size(); i++) {
		for (int j = tab[i].first; j < 1440; j++) ta[j]--;
		for (int j = tab[i].second+T; j < 1440; j++) tb[j]++;
	}

	for (int i = 0; i < tba.size(); i++) {
		for (int j = tba[i].first; j < 1440; j++) tb[j]--;
		for (int j = tba[i].second+T; j < 1440; j++) ta[j]++;
	}

	pair<int, int> res(0, 0);
	for (int i = 0; i < 1440; i++) {
//printf("%4d: %3d %3d\n", i, ta[i], tb[i]);
		if (-ta[i] > res.first) res.first = -ta[i];
		if (-tb[i] > res.second) res.second = -tb[i];
	}

	return res;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int T = readIntLine();

		int AB, BA;
		scanf("%d %d ", &AB, &BA);

		vector<pair<int, int> > tab(AB), tba(BA);
		for (int i = 0; i < AB; i++) {
			tab[i].first = getTime();
			tab[i].second = getTime();
//printf("AB: %d -> %d\n", tab[i].first, tab[i].second);
		}
		for (int i = 0; i < BA; i++) {
			tba[i].first = getTime();
			tba[i].second = getTime();
//printf("BA: %d -> %d\n", tba[i].first, tba[i].second);
		}

		pair<int, int> res = solveIt(T, tab, tba);

		printf("Case #%d: %d %d\n", cn, res.first, res.second);
	}
	return 0;
}

