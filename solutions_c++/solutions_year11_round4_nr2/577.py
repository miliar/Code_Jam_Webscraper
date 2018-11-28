#include<stdio.h>
typedef long long ll;
ll suml[501][501];
ll sumr[501][501];
ll sum[501][501];
long a[501][501];
char s[1001];
long i,j,k,l;
long T,TT,n,m,d,ans=2;
inline ll getsum(const long x1,const long y1,const long x2,const long y2){
	return sum[x2][y2]-sum[x1][y2]-sum[x2][y1]+sum[x1][y1];
}
inline ll getl(const long x1,const long y1,const long x2,const long y2){
	return suml[x2][y2]-suml[x1][y2]-suml[x2][y1]+suml[x1][y1];
}
inline ll getr(const long x1,const long y1,const long x2,const long y2){
	return sumr[x2][y2]-sumr[x1][y2]-sumr[x2][y1]+sumr[x1][y1];
}
inline bool check1(){
	ll f1,f2;
	f1=getl(i,j,i+k,j+k);
	f2=getsum(i,j,i+k,j+k);
	return (double)(f1-(ll)(i+1)*(a[i+1][j+1]+a[i+1][j+k])-(ll)(i+k)*(a[i+k][j+1]+a[i+k][j+k]))/(f2-a[i+1][j+1]-a[i+1][j+k]-a[i+k][j+1]-a[i+k][j+k])==i+k*0.5+0.5;
}
inline bool check2(){
	ll f1,f2;
	f1=getr(i,j,i+k,j+k);
	f2=getsum(i,j,i+k,j+k);
	return (double)(f1-(ll)(j+1)*(a[i+1][j+1]+a[i+k][j+1])-(ll)(j+k)*(a[i+1][j+k]+a[i+k][j+k]))/(f2-a[i+1][j+1]-a[i+1][j+k]-a[i+k][j+1]-a[i+k][j+k])==j+k*0.5+0.5;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%ld",&T);
	while(TT++!=T){
		scanf("%ld%ld%ld",&n,&m,&d),ans=2;
		for(i=1;i<=n;++i)
			for(scanf("%s",s+1),j=1;j<=m;++j){
				a[i][j]=s[j]-'0'+d;
				sum[i][j]=s[j]-'0'+d-sum[i-1][j-1]+sum[i][j-1]+sum[i-1][j];
				suml[i][j]=(s[j]-'0'+d)*i-suml[i-1][j-1]+suml[i][j-1]+suml[i-1][j];
				sumr[i][j]=(s[j]-'0'+d)*j-sumr[i-1][j-1]+sumr[i][j-1]+sumr[i-1][j];
				}
		for(i=0;i+ans<n;++i)
			for(j=0;j+ans<m;++j)
				for(k=ans+1;k+i<=n&&k+j<=m;++k)
					if(check1()&&check2())
						ans=k;
		printf("Case #%ld: ",TT);
		if(ans==2) puts("IMPOSSIBLE");
		else printf("%ld\n",ans);
		}
	scanf("%ld",&T);
	return 0;
}
