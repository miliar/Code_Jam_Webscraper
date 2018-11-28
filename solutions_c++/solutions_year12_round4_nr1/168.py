#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<set>
using namespace std;

int n;
int x[21000];
int y[21000];
int f[21000];
int q[21000];
int main(){
	int h,i,j,k,t;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		x[0]=0;
		memset(q,0,sizeof(q));
		for(i=1;i<=n+1;i++){
			q[i]=0;
		}
		q[0]=1;
		for(i=1;i<=n;i++){
			scanf("%d%d",&x[i],&y[i]);
		}
		scanf("%d",&x[n+1]);
		y[n+1]=0;
		f[0]=x[1];
		j=1;
		for(i=0;i<=n;i++){
			if(q[i]==1){
				for(;j<=n+1;j++){
					if(f[i]>=x[j]){
						q[j]=1;
						if(y[j]>x[j]-x[i])
							f[j]=x[j]+x[j]-x[i];
						else
							f[j]=x[j]+y[j];
					}else break;
				}
			}
		}
		printf("Case #%d: ",h);
		if(q[n+1]==1)printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}