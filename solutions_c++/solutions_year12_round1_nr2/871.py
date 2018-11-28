#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;

#define pb push_back
#define mp make_pair
#define st first
#define nd second

int t, n, m, x, a, b, sta, res, r[1010], dw;
vector<pii > d, p;

int main() {
	scanf("%d", &t);
	for(int c = 1; c <= t; c++) {
		printf("Case #%d: ", c);
		res = sta = dw = 0;
		p.clear();
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			scanf("%d%d", &a, &b);
			p.pb(mp(a, b));
			r[i] = 0;
		}
		bool w=true;
		while(w) {
			w = false;
			for(int i = 0; i < n; i++) {
				if(r[i]==0) {
					if(sta>=p[i].nd) {
						w = true;
						r[i] = 2;
						sta+=2;
						dw++;
						res++;
					}
				}
			}
			if(!w) {
				for(int i = 0; i < n; i++) {
					if(r[i]==1 && sta>=p[i].nd) {
						w = true;
						sta++;
						dw++;
						res++;
						r[i] = 2;
					}
				}
			}
			if(!w) {
				m = -1;
				for(int i = 0; i < n; i++) {
					if(r[i]==0) {
						if(sta>=p[i].st && m<p[i].nd) {
							m = p[i].nd;
							x = i;
						}
					}
				}
				if(m!=-1) {
					w = true;
					sta++;
					r[x] = 1;
					res++;
				}
			}
		}
		if(dw<n)
			printf("Too Bad\n");
		else
			printf("%d\n", res);
	}
	return 0;
}
