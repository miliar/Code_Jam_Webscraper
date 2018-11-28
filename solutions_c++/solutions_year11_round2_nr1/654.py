#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char pic[120][120];
double wp[120];
double owp[120];
double oowp[120];
double ans[120];
double take[120];
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i){
			scanf("%s",pic[i]);
		}
		for(int i=0;i<n;++i){
			wp[i]=0.0;
			int cnt=0;
			for(int j=0;j<n;++j){
				if(pic[i][j]=='1'){
					wp[i]+=1.0;
					++cnt;
				}else if(pic[i][j]=='0')
					++cnt;
			}
			//printf("%lf %d\n",wp[i],cnt);
			take[i]=cnt;
			ans[i]=0.25*wp[i]/cnt;
		}
		for(int i=0;i<n;++i){
			owp[i]=0.0;
			int cnt=0;
			for(int j=0;j<n;++j){
				if(pic[i][j]!='.'){
					++cnt;
					if(take[j]<=1)continue;
					if(pic[i][j]=='0'){
						owp[i]+=(wp[j]-1.0)/(take[j]-1);
					}else{
						owp[i]+=wp[j]/(take[j]-1);
					}
				}
			}
			if(cnt)owp[i]/=cnt;
			//printf("%lf\n",owp[i]);
			ans[i]+=owp[i]*0.50;
		}
		for(int i=0;i<n;++i){
			oowp[i]=0;
			int cnt=0;
			for(int j=0;j<n;++j){
				if(pic[i][j]!='.'){
					oowp[i]+=owp[j];
					++cnt;
				}
			}
			if(cnt)oowp[i]/=cnt;
			ans[i]+=0.25*oowp[i];
		}
		printf("Case #%d:\n",t);
		for(int i=0;i<n;++i){
			printf("%.12f\n",ans[i]);
		}
	}
}
