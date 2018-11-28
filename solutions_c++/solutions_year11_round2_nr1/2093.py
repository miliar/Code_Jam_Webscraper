#include <stdio.h>
#include <string.h>

#define MAXN 110

char map[MAXN][MAXN];
int sum[MAXN];
double wp[MAXN][MAXN], owp[MAXN], oowp[MAXN];

int main(){
	int n, CASE, t, i, j, k;
	int yin, shu;
	char ch;
	double ans;
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &CASE);
	for(t = 1; t <= CASE; t ++){
		scanf("%d", &n); 
		for(i = 0; i < n; i ++)
			scanf("%s", map[i]);
		
		for(i = 0; i < n; i ++){
			for(k = 0; k < n; k ++){
				yin = shu = 0;
				for(j = 0; j < n; j ++)
					if(k != j && map[i][j] == '0') shu ++;
					else 
						if(k != j && map[i][j] == '1') yin ++;
				wp[i][k] = (yin + shu != 0) ? (double) yin / (yin + shu) : 0;
			}
		}
		for(i = 0; i < n; i ++){
			sum[i] = 0;
			for(j = 0; j < n; j ++)
				if(map[i][j] != '.') sum[i] ++;
		}

		for(i = 0; i < n; i ++){
				ans = 0;
				for(j = 0; j < n; j ++)
					if(map[i][j] != '.') ans += wp[j][i];
				owp[i] = ans / sum[i];
		}

		for(i = 0; i < n; i ++){
				ans = 0;
				for(j = 0; j < n; j ++)
					if( map[i][j] != '.') ans += owp[j];
				oowp[i] = ans / sum[i];
		}
		printf("Case #%d:\n", t);
		for(i = 0; i < n; i ++)
			printf("%lf\n", 0.25 * wp[i][i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}

