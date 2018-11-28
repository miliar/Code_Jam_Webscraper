#include <cstdio>
#include <cstring>

const int MAXTRAIN = 110;
const int MAXT = 66;
const int MAXTIME = 24*60+MAXT;

int ncas = 0, n, nt[2], t;
int train[2][2][MAXTRAIN];
int available[2][MAXTIME], left[2];

int main(){
	scanf("%d", &n);
	while (n--){
		scanf("%d", &t);
		scanf("%d %d", &nt[0], &nt[1]);
		for (int k = 0; k < 2; ++k)
			for (int i = 0, a, b; i < nt[k]; ++i)
				for (int j = 0; j < 2; ++j){
					scanf("%d:%d", &a, &b);
					train[k][j][i] = a*60+b;
				}
		memset(available, 0, sizeof(available));
		left[0] = left[1] = 0;
		
		for (int k = 1; k < MAXTIME-1; ++k)
			for (int p = 0; p < 2; ++p){
				for (int i = 0; i < nt[p]; ++i)
					if (train[p][0][i] == k){
						if (available[p][k] > 0){
							available[p][k]--;
							available[1-p][train[p][1][i]+t]++;
						}
						else{
							available[1-p][train[p][1][i]+t]++;
							left[p]++;
							//printf("1 more train at %d:%d, side %d\n", k/60, k%60, p);
						}
					}
				available[p][k+1] += available[p][k];
				//printf("Trains available at %d:%d in the %d side --> %d\n", k/60, k%60, p, available[p][k]);
			}
		printf("Case #%d: %d %d\n", ++ncas, left[0], left[1]);
	}
	return 0;
}
