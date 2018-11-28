
#include <cstdio>
using namespace std;

int teams;
char games[105][105];
int pla[105], win[105];
double owp[105];

main() {
	int ntc;
	scanf("%d", &ntc);
	for (int tec=1; tec<=ntc; tec++) {
		printf("Case #%d:\n", tec);
	
		scanf("%d",&teams);
		for (int t=0; t<teams; t++) {
			scanf("%s",games+t);
		}
		for (int t=0; t<teams; t++) {
			pla[t]=win[t]=0;
			for (int o=0; o<teams; o++) {
				if (games[t][o]!='.') pla[t]++;
				if (games[t][o]=='1') win[t]++;
			}
		}
		for (int t=0; t<teams; t++) {
			double swp=0;
			for (int o=0; o<teams; o++) {
				char g=games[o][t];
				if (g=='.') continue;
				swp += (win[o]-(g=='1'?1:0))*1.0/(pla[o]-1);
			}
			owp[t]=swp/pla[t];
		}
		for (int t=0; t<teams; t++) {
			double re=0.25*win[t]/pla[t];
			re += 0.5*owp[t];
			double oowp=0;
			for (int o=0; o<teams; o++) if (games[o][t]!='.') {
				oowp += owp[o];
			}
			printf("%.7lf\n", re+0.25*oowp/pla[t]);
		}
	}
}
