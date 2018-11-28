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

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	int z,n,s,p,t;
	scanf("%d", &z);
	for(int _ = 1; _ <= z; ++_){
		scanf("%d %d %d", &n, &s, &p);
		int resp = 0, r2 = 0;
		for(int i = 0; i < n; ++i){
			scanf("%d", &t);
			if(t) r2++;
			if(t >= p*3-2) ++resp;
			else if(s){
				if(t >= p*3-4){
					++resp;
					--s;
				}
			}
		}
		if(p == 0) resp = n;
		if(p == 1) resp = r2;
		printf("Case #%d: %d\n", _, resp);
	}
	return 0;
}


