#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;
int games[110][110];
int ngame[110],nscore[110];
double wp[110];
double owp[110];
double oowp[110];
double total[110];
int main()
{
	int t,i,n,j,k;
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	char a[110];
	scanf("%d",&t);
	for (i = 1;i <= t;i++){
		scanf("%d",&n);
		for (j = 0;j < n;j++){
			scanf("%s",a);
			for (k = 0;k < n;k++){
				if (a[k] == '.')
					games[j][k] = -1;
				else if (a[k] == '0')
					games[j][k] = 0;
				else
					games[j][k] = 1;
			}
		}
		int gamenum,score;
		for (j = 0;j < n;j++){
			ngame[j] = 0;
			nscore[j] = 0;
			for (k = 0;k < n;k++){
				if (games[j][k] >= 0)
					ngame[j] ++;
				if (games[j][k] == 1)
					nscore[j] ++;
			}
			wp[j] = (double)nscore[j]/(double)ngame[j];
		}
	
		double wpall;
		for (j = 0;j < n;j++){
			wpall = 0.0;
			for (k = 0;k < n;k++){
				if (games[j][k] == 0)
				{
					gamenum = ngame[k]-1;
					score = nscore[k]-1;
				}				
				else if (games[j][k] == 1){
					gamenum = ngame[k]-1;
					score = nscore[k];
				}
				else{
					continue;
				}
				wpall += (double)score/(double)gamenum;
			}
			owp[j] = wpall/(double)ngame[j];
		}
		
		for (j = 0;j < n;j++){
			wpall = 0.0;gamenum = 0;
			for (k = 0;k < n;k++){
				if (games[j][k] >= 0){
					gamenum ++;
					wpall += owp[k];
				}
			}
			oowp[j] = wpall/(double)gamenum;
		}
		
		printf("Case #%d:\n",i);
		for(j = 0;j < n;j++){
			total[j] = 0.25*wp[j]+0.5*owp[j]+0.25*oowp[j];
			printf("%lf\n",total[j]);
		}
		
	}
	return 0;
}