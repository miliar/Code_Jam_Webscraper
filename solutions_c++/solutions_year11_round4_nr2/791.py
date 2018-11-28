#include<stdio.h>
#include<memory.h>
#include<algorithm>
using namespace std;

int n,m,d;
__int64 a[510][510],b[510][510],r1[510][510],r2[510][510];
char s[510];
int main()
{
	int test,T,K,i,j,k,l;
	__int64 sx,sy,cx,cy;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(T=1;T<=test;T++)
	{
		scanf("%d%d%d",&n,&m,&d);
		for(i=0;i<n;i++)
		{
			scanf("%s",s);
			for(j=0;j<m;j++)
			{
				a[i][j]=(s[j]-'0'+d);
			}
		}
		K=n;
		if(K>m)K=m;
		for(;K>=3;K--)
		{
			
			if(K%2)
			for(i=0;i<=n-K;i++)
			{
				for(j=0;j<=m-K;j++)
				{
					sx=sy=0;
					for(k=0;k<K/2;k++)
					{
						for(l=0;l<K;l++)
						{
							sx+=a[i+k][j+l]*(int)(K/2-k);
							sx+=a[i+k+K/2+1][j+l]*(-k-1);
							sy+=a[i+l][j+k]*(int)(K/2-k);
							sy+=a[i+l][j+k+(int)(K/2)+1]*(-k-1);
						}
					}
					sx-=a[i][j]*(int)(K/2);
					sx-=a[i][j+K-1]*(int)(K/2);
					sx+=a[i+K-1][j]*(int)(K/2);
					sx+=a[i+K-1][j+K-1]*(int)(K/2);
					sy-=a[i][j]*(int)(K/2);
					sy+=a[i][j+K-1]*(int)(K/2);
					sy-=a[i+K-1][j]*(int)(K/2);
					sy+=a[i+K-1][j+K-1]*(int)(K/2);
					if(sx==0 && sy==0)
					{
						break;
					}
				}
				if(sx==0 && sy==0)
					break;
			}
			else
			for(i=0;i<=n-K;i++)
			{
				for(j=0;j<=m-K;j++)
				{
					sx=sy=0;
					for(k=0;k<K/2;k++)
					{
						for(l=0;l<K;l++)
						{
							sx+=a[i+k][j+l]*((int)(K/2)-k);
							sx+=a[i+k+K/2][j+l]*(-k-1);
							sy+=a[i+l][j+k]*((int)(K/2)-k);
							sy+=a[i+l][j+k+K/2]*(-k-1);
						}
					}
					sx-=a[i][j]*(int)(K/2);
					sx-=a[i][j+K-1]*(int)(K/2);
					sx+=a[i+K-1][j]*(int)(K/2);
					sx+=a[i+K-1][j+K-1]*(int)(K/2);
					sy-=a[i][j]*(int)(K/2);
					sy+=a[i][j+K-1]*(int)(K/2);
					sy-=a[i+K-1][j]*(int)(K/2);
					sy+=a[i+K-1][j+K-1]*(int)(K/2);
					if(sx==0 && sy==0)
						break;
				}
				if(sx==0 && sy==0)
					break;
			}
			if(sx==0 && sy==0)
				break;
		}
		printf("Case #%d: ",T);
		if(K>=3)
			printf("%d\n",K);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
