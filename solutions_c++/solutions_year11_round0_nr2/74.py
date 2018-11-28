#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
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

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

char change[256][256];
bool gao[256][256];

void run()
{
	memset(change, 0, sizeof(change));
	memset(gao, false, sizeof(gao));
	int c;
	scanf("%d", &c);
	while (c--) {
		char s[10];
		scanf("%s", s);
		change[s[0]][s[1]] = s[2];
		change[s[1]][s[0]] = s[2];
	}
	int d;
	scanf("%d", &d);
	while (d--) {
		char s[10];
		scanf("%s", s);
		gao[s[0]][s[1]] = true;
		gao[s[1]][s[0]] = true;
	}
	int n;
	scanf("%d", &n);
	char s[1000];
	scanf("%s", s);
	vector<char> v;
	for (int i = 0; i < n; ++i) {
		v.push_back(s[i]);
		if (v.size() == 1) continue;
		if (change[v[v.size() - 1]][v[v.size() - 2]] != 0) {
			char ch = change[v[v.size() - 1]][v[v.size() - 2]];
			v.pop_back();
			v.pop_back();
			v.push_back(ch);
		}
		for (int i = 0; i < v.size(); ++i) {
			if (gao[v[i]][v.back()]) {
				v.clear();
			}
		}
	}
	printf("[");
	for (int i = 0; i < v.size(); ++i) {
		if (i != 0) {
			printf(", ");
		}
		printf("%c", v[i]);
	}
	printf("]\n");
}

int main()
{
	freopen("B0.in", "r", stdin);
	freopen("B0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}