/*
ID: gupan881
PROG: Magicka
LANG: C++
*/
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <vector>
#include <stack>
#include <list>
#include <utility>
#include <queue>
#include <set>
#include <map>
using namespace std;
int
main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, k;
	int i, j;
	cin >> t;
	for(k = 1; k <= t; k++) {
		int st[310];
		int comb[30][30];
		int oppo[30][30];
		memset(comb, 0, sizeof(comb));
		memset(oppo, 0, sizeof(oppo));
		int top, bot;
		int c, d, n;
		char s[5], el[110];
		top = -1; bot = 0;
		cin >> c;
		for(i = 0; i < c; i++) {
			cin >> s;
			int e1 = s[0]-'A', e2 = s[1] - 'A', e3 = s[2] - 'A';
			comb[e1][e2] = comb[e2][e1] = e3;
		}
		cin >> d;
		for(i = 0; i < d; i++) {
			cin >> s;
			int e1 = s[0] - 'A', e2 = s[1] - 'A';
			oppo[e1][e2] = oppo[e2][e1] = 1;
		}
		cin >> n >> el;
		for(i = 0; i < n; i++) {
			st[++top] = el[i] - 'A';
			int tmp;
			while(top > bot && (tmp=comb[st[top]][st[top-1]])>0)
				st[--top] = tmp;
			for(j = bot; j < top; j++)
				if(oppo[st[top]][st[j]]) break;
			if(j < top)
				bot = top+1;
		}
		printf("Case #%d: [", k);
		for(i = bot; i < top; i++)
			cout << char(st[i]+'A') << ", ";
		if(top >= bot)
			cout << char(st[top]+'A');
		cout << "]" << endl;
	}
	return 0;
}
