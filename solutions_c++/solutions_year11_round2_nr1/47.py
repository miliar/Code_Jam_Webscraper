#include<stdio.h>
#include<string.h>
int n;
char s[110][110];
double w[110],ow[110],oow[110];
int tot[110];
int main(){
	int _,t;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d",&n);
		memset(tot,0,sizeof(tot));
		memset(w,0,sizeof(w));
		memset(ow,0,sizeof(ow));
		memset(oow,0,sizeof(oow));
		for(int i=0; i<n; i++){
			scanf("%s",s[i]);
			for(int j=0; j<n; j++){
				if(s[i][j]=='0' || s[i][j]=='1')tot[i]++;
				if(s[i][j]=='1')w[i]+=1;
			}
		}
		for(int i=0; i<n; i++)
			w[i]/=tot[i];
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				if(s[i][j]!='.')
					ow[i]+=(w[j]*tot[j]-(s[j][i]=='1'))/(tot[j]-1);
		for(int i=0; i<n; i++)
			ow[i]/=tot[i];
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				if(s[i][j]!='.')
					oow[i]+=ow[j];
		for(int i=0; i<n; i++)
			oow[i]/=tot[i];
		printf("Case #%d:\n",t);
		for(int i=0; i<n; i++)
			printf("%.10lf\n",(w[i]+2*ow[i]+oow[i])/4);
	}
	return 0;
}
