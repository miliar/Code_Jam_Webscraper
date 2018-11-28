#include <cstdio>
#include <algorithm>
#include <string.h>
using namespace std;

struct r{
	int s, e;
	bool use;
	bool operator>(const r &a)const{
		return (s > a.s || s == a.s && e > a.e);
	}
	bool operator<(const r &a)const{
		return (s < a.s || s == a.s && e < a.e);
	}
};
r a[210];
r b[210];

int t;
bool check(int x, int y){
	int sh, sm, eh, em;
	eh = y / 100;
	em = y % 100;
	sh = x / 100;
	sm = x % 100;
	em += t;
	eh += em / 60;
	em %= 60;
	x = sh*100 + sm;
	y = eh*100 + em;
	return (y <= x);
}

int main(){
	int T, ca=0;
	scanf("%d", &T);
	while (T--){
		int na, nb;
		scanf("%d%d%d", &t, &na, &nb);
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		int x, y;
		for (int i=0; i<na; i++){
			scanf("%d:%d", &x, &y);
			a[i].s = x*100+y;
			scanf("%d:%d", &x, &y);
			a[i].e = x*100+y;
		}
		for (int i=0; i<nb; i++){
			scanf("%d:%d", &x, &y);
			b[i].s = x*100+y;
			scanf("%d:%d", &x, &y);
			b[i].e = x*100+y;
		}		
		sort(a, a+na);
		sort(b, b+nb);
		
		for (int i=0; i<na; i++)
			for (int j=0; j<nb; j++)
				if (!b[j].use && check(b[j].s, a[i].e)){
					b[j].use = true;
					break;
				}
		for (int i=0; i<nb; i++)
			for (int j=0; j<na; j++)
				if (!a[j].use && check(a[j].s, b[i].e)){
					a[j].use = true;
					break;
				}
		int aa, ab;
		aa = ab = 0;
		for (int i=0; i<na; i++)
			if (!a[i].use) aa++;
		for (int i=0; i<nb; i++)
			if (!b[i].use) ab++;
		printf("Case #%d: %d %d\n", ++ca, aa, ab);
	}
	return 0;
}
