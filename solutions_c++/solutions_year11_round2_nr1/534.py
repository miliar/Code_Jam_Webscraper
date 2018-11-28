#include<cstdio>
#include<cstring>
int T, N;
char cht[101][101];
double WP[101], OWP[101], OOWP[101], cmp[101], win[101];
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		scanf("%d", &N);
		for(int i = 0; i < N; i++){
			WP[i] = OWP[i] = OOWP[i] = cmp[i] = win[i] = 0.0;
		    scanf("%s", cht[i]);
			for(int j = 0; j < N; j++){
			    if(cht[i][j] != '.')cmp[i] += 1.0;
			    if(cht[i][j] == '1')win[i] += 1.0;
			}
			WP[i] = win[i] / cmp[i];
		}
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				if(cht[i][j] == '1')OWP[i] += win[j] / (cmp[j] - 1.0);
				else if(cht[i][j] == '0')OWP[i] += (win[j] - 1.0) / (cmp[j] - 1.0);
			}
			OWP[i] /= cmp[i];
		}
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++)
			    if(cht[i][j] != '.')OOWP[i] += OWP[j];
			OOWP[i] /= cmp[i];
		}
		printf("Case #%d:\n", t);
		for(int i = 0; i < N; i++)
		    printf("%lf\n", WP[i] * 0.25 + OWP[i] * 0.5 + OOWP[i] * 0.25);
	}
}
