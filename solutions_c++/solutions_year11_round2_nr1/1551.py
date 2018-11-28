#include<stdio.h>
#include<string.h>
#include<math.h>

int main(void){
	int T,c,N,i,j;
	double wp[102],owp[102],oowp[102],max;
	char team[102][102];
	int win[102],all[102];
	freopen("F:\\A.in","r",stdin);
    freopen("F:\\A.out","w",stdout);
	scanf("%d",&T);
	for(c=1;c<=T;c++){
		scanf("%d",&N);
		for(i=0;i<N;i++){
			scanf("%s",team[i]);
		}
		for(i=0;i<N;i++){
			all[i]=0;win[i]=0;
			for(j=0;j<N;j++){
				if(team[i][j]=='0') all[i]++;
				if(team[i][j]=='1'){
					all[i]++;
					win[i]++;
				}
			}
			wp[i]=win[i]*1.0/all[i];
		}
		for(i=0;i<N;i++){
			max=0;
			for(j=0;j<N;j++){
				if(team[i][j]=='1'){
					max+=win[j]*1.0/(all[j]-1);
				}
				if(team[i][j]=='0'){
					max+=(win[j]-1)*1.0/(all[j]-1);
				}
			}
			owp[i]=max/all[i];
		}
		for(i=0;i<N;i++){
			max=0;
			for(j=0;j<N;j++){
				if(team[i][j]=='0'||team[i][j]=='1'){
					max+=owp[j];
				}
			}
			oowp[i]=max/all[i];
		}
		printf("Case #%d:\n",c);
		for(i=0;i<N;i++){
			printf("%.12f\n",0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
	fclose(stdout);
}