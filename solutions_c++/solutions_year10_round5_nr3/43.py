#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

struct thing {
	thing *next, *prev;
	int lo, hi; 
};
thing *t_l, *t_r;
thing *cur;

long long ans;

void normalise(thing* t) {
	if (t->lo == t->prev->hi+1) {
		t->prev->hi = t->hi;
		t->prev->next = t->next;
		t->next->prev = t->prev;
		if (t == cur) cur = t->prev;
		thing* tmp = t;
		t = t->prev;
		delete tmp;
	}
	if (t->hi == t->next->lo-1) {
		t->next->lo = t->lo;
		t->next->prev = t->prev;
		t->prev->next = t->next;
		if (t == cur) cur = t->prev;
		thing* tmp = t;
		t = t->prev;
		delete tmp;
	}
}

void add_thing(int loc) {
	while (cur != t_r && loc >= cur->next->lo) {cur = cur->next;}
	if (loc > cur->hi) {
		thing *tmp = new thing;
		tmp->prev = cur;
		tmp->next = cur->next;
		tmp->prev->next = tmp;
		tmp->next->prev = tmp;
		tmp->lo = loc;
		tmp->hi = loc;
		cur = tmp;
		normalise(cur);
	} else {
		int old_lo = cur->lo, old_hi = cur->hi;
		thing *tmp = new thing;
		tmp->prev = cur;
		tmp->next = cur->next;
		tmp->prev->next = tmp;
		tmp->next->prev = tmp;
		tmp->lo = old_hi - (loc-old_lo) + 1;
		tmp->hi = old_hi+1;
		cur->lo = old_lo-1;
		cur->hi = old_lo + (old_hi-loc) - 1;

		ans += ((long long)(loc-old_lo+1))*((long long)(old_hi-loc+1));

		normalise(tmp);
		normalise(cur);
	}
}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		
		t_l = new thing;
		t_r = new thing;
		t_l->lo = t_l->hi = -999999999;
		t_r->lo = t_r->hi =  999999999;
		t_l->next = t_r; t_r->prev = t_l;
		cur = t_l;

		int N; scanf("%d",&N);
		ans = 0;
		for (int i = 0; i < N; i++) {
			int loc,amt;
			scanf("%d%d",&loc,&amt);
			while (amt > 0) {
				add_thing(loc);
				amt--;
			}
		}
		//clean up
		for (thing* tmp = t_l->next; ; tmp = tmp->next) {
			delete(tmp->prev);
			if (tmp == t_r) {
				delete(tmp);
				break;
			}
		}
		
		
		printf("Case #%d: %lld\n",test,ans);
	}
}
