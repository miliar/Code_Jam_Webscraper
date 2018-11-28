#include <stdio.h>
#include <string.h>
#include <math.h>

const int maxn = 110;

char a[maxn][maxn];
int n;

double wp[maxn], owp[maxn], oowp[maxn];

double getwp(int who, int notwho){
		int wins = 0, all = 0;
		for (int j = 0 ; j < n ; j++){
			if (j != notwho){
			if (a[who][j] == '1'){
				wins++;
			}
			if (a[who][j] != '.'){
				all++;
			}
			}
		}
		return wins * 1.0 / all;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for (int k = 0 ; k < t ; k++){
	scanf("%d\n",&n);
	for (int i = 0 ; i < n ; i++){
		gets(a[i]);
	}
	for (int i = 0 ; i < n ; i++){
		int wins = 0, all = 0;
		for (int j = 0 ; j < n ; j++){
			if (a[i][j] == '1'){
				wins++;
			}
			if (a[i][j] != '.'){
				all++;
			}
		}
		wp[i] = getwp(i,-1);
		double tekOwp = 0.0;
		for (int j = 0 ; j < n ; j++){
			if (i != j && a[i][j] != '.'){
				tekOwp += getwp(j,i);
			}
		}
		owp[i] = tekOwp / all;
	}

	for (int i = 0 ; i < n ; i++){
		int all = 0;
		double tekoowp = 0.0;
		for (int j = 0 ; j < n ; j++){
			if (a[i][j] != '.'){
				all++;
				tekoowp += owp[j];
			}
		}
		tekoowp /= all;
		oowp[i] = tekoowp;
	}
	printf("Case #%d:\n",k + 1);
	for (int i = 0 ; i < n ; i++){
		printf("%.15lf\n",wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
	}
	}

	return 0;
}