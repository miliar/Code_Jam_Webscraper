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

int cont[10000001];

int main (){
	#ifdef INTERNO
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	#endif
	int z,a,b,at;
	scanf("%d", &z);
	for(int _ = 1; _ <= z; ++_){
		scanf("%d %d", &a, &b);
		int x = 1, resp = 0;
		while(x <= b) x*=10;
		x /= 10;
		for(int i = a; i <= b; ++i){
			int total = 0;
			at = i;
			do{
				cont[at] = _;
				if(at >= a && at <= b) ++total;
				at = at/10 + (at%10*x);				
			}while(cont[at] < _);
			resp += (total*(total-1))/2;
		}
		printf("Case #%d: %d\n", _, resp);
	}
	return 0;
}


