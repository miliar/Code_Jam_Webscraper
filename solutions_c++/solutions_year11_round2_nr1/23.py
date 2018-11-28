#include <stdio.h>
char dat[105][105];
int win[105], loss[105], cnt[105];

double WP[105], OWP[105], OOWP[105], RPI[105];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	int T, n;
	scanf("%d",&T);
	while(T>0){T--;
		scanf("%d",&n);
		int i, j;
		for(i=0;i<n;i++) scanf("%s",dat[i]);
		for(i=0;i<n;i++) cnt[i] = win[i] = loss[i] = 0;
		for(i=0;i<n;i++) WP[i] = OWP[i] = OOWP[i] = RPI[i]  =0.0;
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(dat[i][j] == '1') win[i] ++;
				if(dat[i][j] == '0') loss[i] ++;
				if(dat[i][j] != '.')cnt[i] ++;
			}
		}
		for(i=0;i<n;i++){
			WP[i] = (double)win[i] / (double)cnt[i];
		}
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(dat[i][j] != '.'){
					if(dat[i][j] == '0') OWP[i] += (double)(win[j]-1) / (double)(cnt[j]-1);
					if(dat[i][j] == '1') OWP[i] += (double)(win[j]) / (double)(cnt[j]-1);
				}
			}
		}
		for(i=0;i<n;i++) OWP[i] /= (double)cnt[i];
		
		for(i=0;i<n;i++){
			for(j=0;j<n;j++){
				if(dat[i][j] != '.'){
					OOWP[i] += OWP[j];
				}
			}
		}
		for(i=0;i<n;i++) OOWP[i] /= (double)cnt[i];

		for(i=0;i<n;i++) RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		static int cs=0;
		printf("Case #%d:\n",++cs);
		for(i=0;i<n;i++){
			printf("%.10lf\n",RPI[i]);
		}
	}
	return 0;
}