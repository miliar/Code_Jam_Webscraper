#include <cstdio>
#include <cstring>

char buf[200][200];
int T, N;
double wp[200], owp[200], oowp[200];
int win[200], ply[200];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int cc=1; cc<=T; cc++) {
		scanf("%d", &N);
		memset(win, 0, sizeof(win));
		memset(ply, 0, sizeof(ply));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));
		for(int i=0; i<N; i++) {
			scanf("%s", buf[i]);;
			for(int j=0; j<N; j++) {
				if(buf[i][j] == '.') continue;
				ply[i] ++;
				if(buf[i][j] == '0') continue;
				win[i] ++;
			}
			wp[i] = (double)win[i]/ply[i];
	//		printf("%d : win %d ply %d   %f\n", i, win[i], ply[i], wp[i]);

		}

		printf("Case #%d:\n", cc);
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(buf[i][j] != '.') {
					if(buf[i][j] == '1') {
						owp[i] += (double)win[j] / (ply[j]-1);
					} else {
						owp[i] += (double)(win[j]-1) / (ply[j]-1);
					}
				}
//				printf("%d : %d\n", i, ply[i]);
			}
			owp[i] /= ply[i];
	//		printf("%d : owp %f  ply %d\n", i, owp[i], ply[i]);
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				if(buf[i][j] != '.')
					oowp[i] += owp[j];
			}
			oowp[i] /= ply[i];
			printf("%.10f\n", wp[i]*0.25 + owp[i]*0.5 + oowp[i]*0.25);
		}
	}
}
