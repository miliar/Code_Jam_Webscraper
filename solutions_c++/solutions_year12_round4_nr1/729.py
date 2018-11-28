#include<cstdio>
#include<cstring>
#define N 60005
int q[N],d[N],l[N],m[N],n,D,oo=2000000000;
inline int min(int a,int b){return a<b?a:b;}
bool can()
{
	d[++n]=D;
	for (int i=1;i<=n;i++) m[i]=oo; m[1]=0;
	for (int i=1;i<=n;i++){
		int len=d[i]+min(l[i],d[i]-m[i]);
		for (int j=i+1;j<=n && d[j]<=len;j++) if (m[j]==oo) m[j]=d[i];
		}
	return m[n]<oo;
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int test,Case=0; scanf("%d",&test); 
	while (test--){
		scanf("%d",&n);
		for (int i=1;i<=n;i++) scanf("%d%d",&d[i],&l[i]);
		scanf("%d",&D);
		printf("Case #%d: %s\n",++Case,can()?"YES":"NO");		
		}
	return 0;
}
