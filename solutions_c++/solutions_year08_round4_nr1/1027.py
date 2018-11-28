#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

using namespace std;

#ifndef DEB
#define DEBUG(out)
#else
#define DEBUG(out) cerr << __LINE__ << ":\t" << out << endl
#endif

#define INT_M 1<<20

struct node{
	int i;
	int p;
	int c[2];
	int v;
	int f;
	int ch;
	int s;
};

node t[10001];

int fill(node &n){
	bool a, b;
	if(n.f == 1){
		a = fill(t[n.c[0]]);
		b = fill(t[n.c[1]]);
		n.v = a && b;
	}else if (n.f == 0){
		a = fill(t[n.c[0]]);
		b = fill(t[n.c[1]]);
		n.v = a || b;
	}
	DEBUG("f " << n.i << " " << n.v);
	return n.v;
}

void sw(node &n){
	if(n.f == -1)
		return;
	sw(t[n.c[0]]);
	sw(t[n.c[1]]);
	int best = INT_M;
	int t0, t1;
	if(n.f == 1 && n.v == 1){
		best = min(best, min(t[n.c[0]].s, t[n.c[1]].s));
	}else if(n.f == 1 && n.v == 0){
		if(t[n.c[0]].v == 0 && t[n.c[0]].v == 0){
			t0 = t[n.c[0]].s;
			t1 = t[n.c[1]].s;
			if(t0 != INT_M && t1 != INT_M)
				best = min(best, t0 + t1);
		}else if(t[n.c[0]].v == 0){
			best = min(best, t[n.c[0]].s);
		}else if(t[n.c[1]].v == 0){
			best = min(best, t[n.c[1]].s);
		}
	}else if(n.f == 0 && n.v == 0){
		best = min(best, min(t[n.c[0]].s, t[n.c[1]].s));
	}else if(n.f == 0 && n.v == 1){
		if(t[n.c[0]].v == 1 && t[n.c[0]].v == 1){
			t0 = t[n.c[0]].s;
			t1 = t[n.c[1]].s;
			if(t0 != INT_M && t1 != INT_M)
				best = min(best, t0 + t1);
		}else if(t[n.c[0]].v == 1){
			best = min(best, t[n.c[0]].s);
		}else if(t[n.c[1]].v == 1){
			best = min(best, t[n.c[1]].s);
		}
	}
	if(n.ch == 1){
		DEBUG(n.i << " " << n.f << " " << t[n.c[0]].v << " " << t[n.c[1]].v);
		if(n.f == 1 && (t[n.c[0]].v || t[n.c[1]].v) != n.v)
			best = 1;
		else if(n.f == 0 && (t[n.c[0]].v && t[n.c[1]].v) != n.v)
			best = 1;
		else if(n.f == 0 && n.v == 1){
			best = min(best, 1 + min(t[n.c[0]].s, t[n.c[1]].s));
		}else if(n.f == 0 && n.v == 0){
			if(t[n.c[0]].v == 0 && t[n.c[0]].v == 0){
				t0 = t[n.c[0]].s;
				t1 = t[n.c[1]].s;
				if(t0 != INT_M && t1 != INT_M)
					best = min(best, t0 + t1 + 1);
			}else if(t[n.c[0]].v == 0){
				best = min(best, 1 + t[n.c[0]].s);
			}else if(t[n.c[1]].v == 0){
				best = min(best, 1 + t[n.c[1]].s);
			}
		}else if(n.f == 1 && n.v == 0){
			best = min(best, 1 + min(t[n.c[0]].s, t[n.c[1]].s));
		}else if(n.f == 1 && n.v == 1){
			if(t[n.c[0]].v == 1 && t[n.c[0]].v == 1){
				t0 = t[n.c[0]].s;
				t1 = t[n.c[1]].s;
				if(t0 != INT_M && t1 != INT_M)
					best = min(best, 1 + t0 + t1);
			}else if(t[n.c[0]].v == 1){
				best = min(best, 1 + t[n.c[0]].s);
			}else if(t[n.c[1]].v == 1){
				best = min(best, 1 + t[n.c[1]].s);
			}
		}
	}
	n.s = best;
	DEBUG(n.i << " " << n.s);
}

int N, V;
int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int tc=0; tc<tcs; ++tc){
		scanf("%d %d", &N, &V);
		for(int i=1; i<(N+1)/2; ++i){
			DEBUG(i << " -> " << (i*2) << " " << (i*2+1));
			t[i].c[0] = i*2;
			t[i].c[1] = i*2+1;
			t[t[i].c[0]].p = i;
			t[t[i].c[1]].p = i;
			scanf("%d", &t[i].f);
			scanf("%d", &t[i].ch);
			t[i].i = i;
		}
		for(int i=(N+1)/2; i<=N; ++i){
			DEBUG("i" << i);
			t[i].i = i;
			t[i].f = -1;
			t[i].s = INT_M;
			scanf("%d", &t[i].v);
		}
		fill(t[1]);
		sw(t[1]);
		int erg = t[1].v == V ? 0 : t[1].s;
		if(erg!=INT_M){
			printf("Case #%d: %d\n", tc+1, erg);
		}else{
			printf("Case #%d: IMPOSSIBLE\n", tc+1);
		}
	}
}
