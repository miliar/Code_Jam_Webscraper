#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define maxn 110

char map[maxn][maxn];
int win[maxn],lose[maxn];
double wp[maxn],owp[maxn],oowp[maxn],rp[maxn];
int n,zu,T;
char ch;

void process(){
	int i,j,tem,num;
	double sum;
	memset(win,0,sizeof(win));
	memset(lose,0,sizeof(lose));
	for (i = 0 ; i < n; i++){
		for (j = 0 ; j < n; j++){
			if (map[i][j] == '0') lose[i]++;
			if (map[i][j] == '1') win[i]++;
		}
		wp[i] = (win[i] * 1.0)/(win[i] + lose[i]);
	}

	for (i = 0; i < n; i++){
		num = 0;
		sum = 0;
		for (j = 0; j < n; j++)
			if (i != j){
				if (map[j][i] == '0') {
					num++;
					sum += (win[j] * 1.0)/(win[j] + lose[j] - 1);
				}
				if (map[j][i] == '1') {
					num++;
					sum += ((win[j] - 1) * 1.0)/(win[j] + lose[j] - 1);
				}
			}
		owp[i] = sum / num;
	}

	for (i = 0; i < n; i++){
		num = 0;
		sum = 0;
		for (j = 0; j < n; j++)
			if (map[i][j] != '.'){
				num++;
				sum += owp[j];
			}
		oowp[i] = sum / num;
	}
	for (i = 0; i < n; i++)
		rp[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
}

int main(){
	int i,j,tem;
	/*freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);*/
	scanf("%d",&T);
	for (zu = 1; zu <= T; zu++){
		scanf("%d",&n);
		scanf("%c",&ch);
		memset(map, 0, sizeof(map));
		for (i = 0; i < n; i++)
			gets(map[i]);
		process();
		printf("Case #%d:\n",zu);
		for (i = 0; i < n; i++)
			printf("%.12lf\n",rp[i]);
	}
	return 0;
}
