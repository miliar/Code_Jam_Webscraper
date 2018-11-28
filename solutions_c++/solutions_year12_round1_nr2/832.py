#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>

using namespace std;

int t, a, b, n,resp;
struct level{
	int one, two;
	const bool operator< (const level &that) const{
		if(two != that.two) return two < that.two;
		return one < that.one;
	}
} lev[1001];
bool mark[1001];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	scanf("%d", &t);
	for(int _ = 1; _ <= t; ++_){
		scanf("%d", &n);
		memset(mark, 0, sizeof mark);
		resp = 0;
		for(int i = 0; i < n; ++i){
			scanf("%d %d", &a, &b);
			lev[i].one = a;
			lev[i].two = b;
			if(a == 0) resp++;
			if(b > 2*n) resp = -10000;
		}
		int at = 0;
		if(resp <= 0) goto fail;
		sort(lev, lev+n);
		resp = 0;
		for(int i = 0; i < n; ++i){
			++resp;
			if(lev[i].two <= at){
				at += 2-mark[i];
			}
			else{
				for(int j = n-1; j >= i; --j){
					if(lev[j].one <= at && !mark[j]){
						mark[j] = true;
						at++;
						goto saida;
					}
				}
				goto fail;
				saida:;
				--i;
			}
		}
		printf("Case #%d: %d\n", _, resp);
		continue;
		fail:
		printf("Case #%d: Too Bad\n", _);
	}
	return 0;
}
