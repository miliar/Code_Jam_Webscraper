#include <algorithm>
#include <cstdio>
#include <cmath>

using namespace std;

int t, n, p;
char r[2];
int poso, posb, timeo, timeb;

int main(){
	scanf("%d", &t);
	for (int cas = 1; cas <= t; ++cas){
		scanf("%d", &n);
		poso = posb = 1;
		timeo = timeb = 0;
		for (int i = 0; i < n; ++i){
			scanf("%s %d", r, &p);
			int current_time = max(timeo, timeb);
			if (r[0] == 'B'){
				timeb += abs(p-posb)+1;
				posb = p;
				if (timeb <= current_time)
					timeb = current_time+1;
			}
			else{
				timeo += abs(p-poso)+1;
				poso = p;
				if (timeo <= current_time)
					timeo = current_time+1;
			}
			//printf("(%c %d) => (%d %d), (%d %d)\n", r[0], p, posb, timeb, poso, timeo);
		}
		printf("Case #%d: %d\n", cas, max(timeo, timeb));
	}
	return 0;
}
