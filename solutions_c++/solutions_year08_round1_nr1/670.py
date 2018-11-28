#include <iostream>
#include <string>

using namespace std;
#define MAXN 810
#define inf 1000000000
#define _clr(x) memset(x,0xff,sizeof(long long)*n)


long long kuhn_munkras(int m,int n,long long mat[][MAXN],long long* match1,long long* match2){
	long long s[MAXN],t[MAXN],l1[MAXN],l2[MAXN],p,q,ret=0,i,j,k;
	for (i=0;i<m;i++)
		for (l1[i]=-inf,j=0;j<n;j++)
			l1[i]=mat[i][j]>l1[i]?mat[i][j]:l1[i];
	for (i=0;i<n;l2[i++]=0);
	for (_clr(match1),_clr(match2),i=0;i<m;i++){
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (l1[k]+l2[j]==mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
		if (match1[i]<0){
			for (i--,p=inf,k=0;k<=q;k++)
				for (j=0;j<n;j++)
					if (t[j]<0&&l1[s[k]]+l2[j]-mat[s[k]][j]<p)
						p=l1[s[k]]+l2[j]-mat[s[k]][j];
			for (j=0;j<n;l2[j]+=t[j]<0?0:p,j++);
			for (k=0;k<=q;l1[s[k++]]-=p);
		}
	}
	for (i=0;i<m;i++)
		ret+=mat[i][match1[i]];
	return ret;
}

long long mat[MAXN][MAXN];
long long m1[MAXN], m2[MAXN];
long long A[MAXN], B[MAXN];
int n;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	int ctr = 0;
	scanf("%d", &T);
	while (T--)
	{
		ctr ++;
		scanf("%d", &n);
		for (int i = 0;i < n; i++)
			scanf("%I64d", &A[i]);

		for (int j = 0; j < n; j++)
			scanf("%I64d", &B[j]);

		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				mat[i][j] = -A[i] * B[j];

		printf("Case #%d: %I64d\n", ctr,-kuhn_munkras(n, n,mat,m1, m2));


	}
	return 0;
}
