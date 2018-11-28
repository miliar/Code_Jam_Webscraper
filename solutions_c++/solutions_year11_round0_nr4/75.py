#include<stdio.h>
double randp[1010];
int in[1010];
int vis[1010];
int main(){
    int i,j;
    randp[1]=0;
    for(i=2;i<=1000;i++){
	randp[i]=randp[i-1];
	for(j=2;j<=i-1;j++){
	    randp[i]+=(randp[j]+randp[i-j]);
	}
	randp[i]/=(i-1);
	randp[i]+=1;
//	if(i<=100)printf("%.7lf\n",randp[i]);
    }
    int t;
    scanf("%d",&t);
    int cas=1;
    while(t--){
	int n;
	scanf("%d",&n);
	for(i=1;i<=n;i++){
	    scanf("%d",&in[i]);
	    vis[i]=0;
	}
	double ans=0;
	for(i=1;i<=n;i++)if(!vis[i]){
	    int c=0;
	    int np=i;
	    while(!vis[np]){
		c++;
		vis[np]=1;
		np=in[np];
	    }
	    ans+=(c>1?c:c-1);
	}
	printf("Case #%d: %.6lf\n",cas++,ans);
    }
}
