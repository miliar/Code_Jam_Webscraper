#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

__int64 t,r,k,n;
__int64 g[1001];
__int64 f[1001][2];
__int64 v[1001][2];

int main(){
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	__int64 h,i,j,l;
	bool u=0;
	scanf("%I64d",&t);
	for(h=1;h<=t;h++){
		memset(v,255,sizeof(v));
		memset(g,0,sizeof(g));
		memset(f,0,sizeof(f));
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%I64d",&g[i]);
		for(i=0;i<n;i++){
			l=0;
			for(j=i;j<n+i;j++){
				if(l+g[j%n]<=k){
					l+=g[j%n];
				}else break;
			}
			f[i][0]=j%n;
			f[i][1]=l;
		}
		j=0;
		l=0;
		u=0;
		for(i=0;i<r;i++){
			if(u==1 || v[j][0]==-1){
				v[j][0]=i;
				v[j][1]=l;
				l+=f[j][1];
				j=f[j][0];
			}else{
				l+=((r-i)/(i-v[j][0]))*(l-v[j][1]);
				i+=((r-i)/(i-v[j][0]))*(i-v[j][0])-1;
				u=1;
			}
		}
		printf("Case #%I64d: %I64d\n",h,l);
	}
	return 0;
}