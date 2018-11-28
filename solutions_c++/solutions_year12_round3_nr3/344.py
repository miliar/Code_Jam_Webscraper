#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

#define MAXN 110

using namespace std;

typedef long long ll;

int n, m;
ll pd[MAXN][MAXN];
ll box[MAXN][2], toy[MAXN][2];

ll f(int b, int t, ll resto, bool isBox, bool isToy);
ll rec(int b, int t);

ll f(int b, int t, ll resto, bool isBox, bool isToy) {
	if(!resto) return rec(b, t);
	if(b == n || t == m) return 0;
	
	ll ans = 0, tmp = 0;
	bool c1 = false, c2 = false, c3 = false;
	if(isBox) {
		ans = rec(b + 1, t);
		for(int i = t; i < m; ++i) {
			if(box[b][0] == toy[i][0]) {
				if(resto == toy[i][1]) {
					if(!c1) tmp = resto + rec(b + 1, i + 1);
					c1 = true;
				} else if(resto < toy[i][1]) {
					if(!c2) tmp = resto + f(b + 1, i, toy[i][1] - resto, false, true);
					c2 = true;
				} else {
					if(!c3) tmp = toy[i][1] + f(b, i + 1, resto - toy[i][1], true, false);
					c3 = true;
				}
				
				if(ans < tmp) ans = tmp;
			}
		}
	} else if(isToy) {
		ans = rec(b, t + 1);
		for(int i = b; i < n; ++i) {
			if(toy[t][0] == box[i][0]) {
				if(resto == box[i][1]) {
					if(!c1) tmp = resto + rec(i + 1, t + 1);
					c1 = true;
				} else if(resto < box[i][1]) {
					if(!c2) tmp = resto + f(i, t + 1, box[i][1] - resto, true, false);
					c2 = true;
				} else {
					if(!c3) tmp = box[i][1] + f(i + 1, t, resto - box[i][1], false, true);
					c3 = true;
				}

				if(ans < tmp) ans = tmp;
			}
		}
	}

	return ans;
}

ll rec(int b, int t) {
	if(b == n || t == m) return 0;
	if(~pd[b][t]) return pd[b][t];
	pd[b][t] = 0;
	ll menor, maior;
	bool isToy = false, isBox = false;
	if(box[b][0] == toy[t][0]) {
		
		if(box[b][1] == toy[t][1]) pd[b][t] = box[b][1] + rec(b + 1, t + 1);
		else {
			if(box[b][1] < toy[t][1])
				menor = box[b][1], maior = toy[t][1], isToy = true;
			else menor = toy[t][1], maior = box[b][1], isBox = true;
			
			pd[b][t] = menor + f(b + (isToy ? 1 : 0), t + (isBox ? 1 : 0), maior - menor, isBox, isToy);
		}
	} else {
		menor = f(b, t + 1, box[b][1], true, false);
		maior = f(b + 1, t, toy[t][1], false, true);
		if(menor < maior) pd[b][t] = maior;
		else pd[b][t] = menor;
	}

	return pd[b][t];
}

int main() {
	int t, caso = 0;
	scanf("%d", &t);
	while(t--) {
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; ++i)
			scanf("%lld%lld", &box[i][1], &box[i][0]);
		for(int i = 0; i < m; ++i)
			scanf("%lld%lld", &toy[i][1], &toy[i][0]);

		memset(pd, -1, sizeof(pd));
		printf("Case #%d: %lld\n", ++caso, rec(0, 0));
	}
	
	return 0;
}

