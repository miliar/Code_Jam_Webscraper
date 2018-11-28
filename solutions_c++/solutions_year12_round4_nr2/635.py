#include<cstdio>
#define N 1005
int now,W,L,n,x[N],y[N],r[N];
long long sqr(long long x){return x*x;}
bool check(int X,int Y)
{
	for (int i=0;i<now;i++)
		if (sqr(x[i]-X)+sqr(y[i]-Y)<sqr(r[i]+r[now])) return 0;		
	return 1;
}
int find(int X)
{
	int l=0,r=L+1,mid;
	while (l<r){
		mid=(l+r)/2;
		if (check(X,mid)) r=mid; else l=mid+1;
		}
	return l;
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int test,Case=0; scanf("%d",&test);
	while (test--){
		scanf("%d%d%d",&n,&W,&L);
		for (int i=0;i<n;i++) scanf("%d",&r[i]);
		for (int i=0;i<n;i++){
			int l=0,r=W,mid; now=i;
			while (l<r){
				mid=(l+r)/2;
				if (find(mid)<=L) r=mid; else l=mid+1;
				}
			x[i]=l; y[i]=find(l);
			}
		printf("Case #%d:",++Case);
		for (int i=0;i<n;i++) printf(" %d %d",x[i],y[i]);
		printf("\n");
		}
	return 0;
}
