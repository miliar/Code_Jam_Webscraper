#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <algorithm>
#include <utility>
#include <cmath>
#define LL long long

using namespace std;


int dists[1010];
LL acu[1010];
int L, N, C;
LL t;
int main(){
	int casos; scanf("%d", &casos);
	int caso = 1;
	int a;
	LL menor;
	while(casos--){
		printf("Case #%d: ", caso++);
		scanf("%d%lld%d%d", &L, &t, &N, &C);
		for(int i = 0; i < C; ++i){
			scanf("%d", &a); a += a;
			for(int k = 0; k*C+i < N; ++k){
				dists[k*C+i] = a;
			}
		}
		
		acu[0] = 0;
		for(int i = 1; i <= N; ++i){
			acu[i] = dists[i-1] + acu[i-1];
		//	printf("%d: %lld\n", i, acu[i]);
		}
		menor = 0x6363636363LL;
		double aux1, aux2, at, at2;
		//printf("acu[N] = %lld\n", acu[N]);
		if(L > 0)
		for(int i = 0; i < N; ++i){
//			printf("%d: %lld\n", i, acu[i]);
			aux2 = acu[i+1] - acu[i];
//printf("aux 2 = %lf\n", aux2);
			if(acu[i+1] > t){
				if(t >= acu[i]){
					aux2 -= (double)(acu[i+1]-t)/2.0;
				}else{
					aux2 /= 2.0;
				}
			}
		//	printf("depois aux 2 = %lf\n", aux2);
			
			at2 = at = acu[i] + aux2;
			
			if(L == 2){
				for(int j = i+1; j < N; ++j){
					at =at2+  (acu[j] - acu[i+1]);
		//			printf("j = %d: at = %lf;\n", j, at);
					aux2 = acu[j+1] - acu[j];
		//				printf("aux 2 = %lf\n", aux2);
					aux1 = at + aux2;
					if(aux1 > t){
						if(t >= at){
							aux2 = (t - at) + ( aux2-(t-at) )/2.0;
						}else{
							aux2 /= 2.0;
						}
					}
			//		printf("depois aux 2 = %lf\n", aux2);
					at += aux2;
					at += acu[N] - acu[j+1];
					if(at < menor) menor = at;
				}
			}
			
			at2 += acu[N] - acu[i+1];
			if(at2 < menor) menor = at2;
			
		}
		else menor = acu[N];
		printf("%lld\n", menor);
	}
	
	return 0;
}
