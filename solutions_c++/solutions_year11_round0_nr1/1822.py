#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

//#define debug

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long lint;

const int inf = 0x7fffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 20000;

char buffer[Size];

int solution(int nTest) {
	int res = 0;
	int n;

	scanf("%d", &n);
	vector<pii> v;
	For(i, 0, n) {
		getchar();
		char t = getchar();
		int lab;
		scanf("%d", &lab);
		if(t == 'O')
			v.pb(mp(0, lab));
		else
			v.pb(mp(1, lab));
	}

	int pos[2];
	int last[2];
	pos[0] = pos[1] = 1;
	last[0] = last[1] = 0;
	For(it, 0, n) {
		int r = v[it].first;
		int l = v[it].second;
		int time = abs(l - pos[r]) + 1;
		pos[r] = l;
		time = max(1, time - last[r ^ 1]);
		last[r ^ 1] = 0;
		last[r] += time;
		res += time;
	//	cerr << last[0] << " " << last[1] << " " << time << endl;
	}

	printf("Case #%d: %d\n", nTest + 1, res);

	return 1;
}

int main() {
	freopen("input.txt", "r", stdin);
#ifndef debug
	freopen("output.txt", "w", stdout);
#endif

	int i = 0, n = 999999;
	scanf("%d", &n);

	while(i < n && solution(i))
		i++;

	return 0;
}

