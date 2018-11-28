#include<iostream>
using namespace std;

#define MAXN 1010

__int64 r,k;
__int64 g[MAXN];
__int64 sum[MAXN][MAXN];
int head,n;//tail=(head+n)%n

void setlist()
{
	int i,j;
	for(i=0;i<n;++i)
	{
		sum[i][0]=g[i];
		for(j=1;j<n;++j)
			sum[i][j]=sum[i][j-1]+g[(i+j)%n];
	}
}

__int64 getsum(int f,int m)//fͷ+1ĺ
{
	return sum[f][f+m];
}

int binary_search()
{
	if(sum[head][n-1]<=k) return n-1;
	int l=0,r=n-1,mid;
	int ret;
	while(l<r){
		if(l+1==r) return l;
		mid=(l+r)/2;
		if(sum[head][mid]<=k) l=mid;
		else r=mid;
	}
	return l;
}

int main()
{
	int t,ti,i,ki,gi,nown;
	__int64 ans;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	for(ti=1;ti<=t;++ti)
	{
		ans=0;
		scanf("%I64d%I64d%d",&r,&k,&n);
		for(i=0;i<n;++i)
			scanf("%I64d",&g[i]);
		setlist();
		head=0;
		for(ki=0;ki<r;++ki)
		{
			nown=binary_search();
			ans+=sum[head][nown];
			head=(head+nown+1)%n;
		}
		printf("Case #%d: %I64d\n",ti,ans);
	}
	//system("pause");
	return 0;
}