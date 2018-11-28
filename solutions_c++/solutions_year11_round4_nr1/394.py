


/*
	Prob: (Google code jam 2011 - Round 2 - A)
	Author: peanut
	Time: 04/06/11 22:10
	Description: Greedy
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxN = 1111;

struct node{
	double len, w;
	node() {}
	node(double _l, double _w) {len = _l, w = _w;}
} walkway[MaxN];

bool cmp(const node &p, const node &q) {return p.w < q.w;}

int T, N;
double t, c, s, r, x;

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++ cs) {
		scanf("%lf %lf %lf %lf %d", &x, &s, &r, &t, &N);
		for (int k = 1; k <= N; ++ k) {
			int b, e, w;
			cin >> b >> e >> w;
			walkway[k] = node(e - b, w);
			x -= e - b;
		}
		walkway[0] = node(x, 0);
		sort(walkway, walkway + N + 1, cmp);
		
		c = 0;
		for (int k = 0; k <= N; ++ k) {
			double tmp = min(t, walkway[k].len / (r + walkway[k].w));
			t -= tmp; c += tmp;
			c += (walkway[k].len - tmp * (r + walkway[k].w)) / (s + walkway[k].w);
		}
		
		printf("Case #%d: %.9lf\n", cs, c);
	}
	
	return 0;
}
