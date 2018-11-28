#include<iostream>
using namespace std;
const int fm[11]={1,2,4,8,16,32,64,128,256,512,1024};
int f[11][1024][11];
int ans,tot,tt;
int min(int a,int b){
	if(a==-1)return b;
	if(b==-1)return a;
	return (a>b?b:a);
}
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int i,j,k,x,i1,i2,p,ii;
	scanf("%d",&tot);
	for(tt=1;tt<=tot;tt++){
		scanf("%d",&p);
		for(i=0;i<=10;i++)
			for(j=0;j<fm[10];j++)
				for(k=0;k<=10;k++)f[i][j][k]=-1;
		for(i=0;i<fm[p];i++){
			scanf("%d",&x);
			if(x>10)x=10;
			f[p][i][x]=0;
		}
		for(i=p-1;i>=0;i--){
			for(k=0;k<fm[i];k++){
				scanf("%d",&x);
				int p1=2*k;
				int p2=2*k+1;
				for(i1=0;i1<=10;i1++)
					for(i2=0;i2<=10;i2++)
						if((f[i+1][p1][i1]!=-1)&&(f[i+1][p2][i2]!=-1)){
							ii=min(i1,i2);
							f[i][k][ii]=min(f[i][k][ii],f[i+1][p1][i1]+f[i+1][p2][i2]+x);
							if(ii>0)f[i][k][ii-1]=min(f[i][k][ii-1],f[i+1][p1][i1]+f[i+1][p2][i2]);
						}
			}
		}
		ans=-1;
		for(i=0;i<10;i++)
			ans=min(ans,f[0][0][i]);
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}