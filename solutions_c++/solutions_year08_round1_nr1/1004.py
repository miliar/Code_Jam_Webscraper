#include<iostream>
#include <cstring>
#include<cstdio>
using namespace std;
#define MAXN 900
#define inf 1000000000
#define _clr(x) memset(x,0xff,sizeof(__int64)*n)
int a[1000];
int b[1000];
__int64 ok[900][900];
__int64 m1[MAXN],m2[MAXN];
int num;
__int64 kuhn_munkras(int m,int n,__int64 mat[][MAXN],__int64* match1,__int64* match2){
	__int64 s[MAXN],t[MAXN],l1[MAXN],l2[MAXN],p,q,ret=0,i,j,k;
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

int main()
{
int t,n,m;
int i,j,k;
freopen("1.in.txt","r",stdin);
freopen("1.out","w",stdout);
scanf("%d",&t);
for(i=1;i<=t;i++)
{
scanf("%d",&n);
for(j=0;j<=n-1;j++)
 scanf("%d",&a[j]);
for(j=0;j<=n-1;j++)
 scanf("%d",&b[j]);
for(j=0;j<n;j++)
 for(k=0;k<n;k++)
	 ok[j][k]=-a[j]*b[k];

 printf("Case #%d: ",i);
printf("%I64d\n",-kuhn_munkras(n,n,ok,m1,m2));
}
return 0;
}