#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

const int MAX= 102;

char mp[MAX][MAX];
int win[MAX], lose[MAX];
double res[MAX], rate[MAX], oprate[MAX], owp[MAX];
//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, j, n, icas, cas;
	scanf("%d", &cas);
	for (icas = 1; icas <= cas; ++icas) {
		scanf("%d", &n);
		memset(win, 0, sizeof(win));
		memset(lose, 0, sizeof(lose));
		memset(rate, 0, sizeof(rate));
		for (i = 0; i < n; ++i) {
			scanf("%s", &mp[i]);
			for (j = 0; j < n; ++j) {
				if (mp[i][j] == '0')
				   lose[i]++;
				else if (mp[i][j] == '1')
					 win[i]++;	
			}
  			rate[i] = (double)win[i] / (win[i] + lose[i]);
  		//	printf("rate %d %lf\n", i, rate[i]);
		}
		for (i = 0; i < n; ++i) {
			double tmp1 = 0.0, tmp2 = 0.0;
			int acc = 0;
			for (j = 0; j < n; ++j) {
				if (mp[i][j] == '0') {
				   		
						tmp1 += (double)(win[j] - 1) / (win[j] + lose[j] - 1);	 
			    }
			    else if (mp[i][j] == '1') {
						tmp1 += (double)(win[j]) / (win[j] + lose[j] - 1);
			   }
			   
			   if (mp[i][j] != '.') {
			   	  			acc++;
			   }
			}
			owp[i] = (double)tmp1 / acc;
		}
		for (i = 0; i < n; ++i) {
			double tmp1 = 0.0, tmp2 = 0.0;
			int acc = 0;
			res[i] = 0.0;
			for (j = 0; j < n; ++j) {
			   
			   if (mp[i][j] != '.') {
			   	  			acc++;
 			         tmp2 += owp[j];
			   }
			}
		//	printf("rr %lf %lf %lf\n", rate[i], owp[i], tmp2 /acc);
		//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP	
			res[i] += 0.25 * rate[i] + 0.5 * owp[i] + 0.25 * tmp2 / acc;
			
			
			
		}
			
		printf("Case #%d:\n", icas);
		for (i = 0; i < n; ++i)
			printf("%.12lf\n", res[i]);
	
	
	
	
	
	}
	
	//system("pause");
}