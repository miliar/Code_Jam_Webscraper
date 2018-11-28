#include<stdio.h>
#include<string.h>
int mp[110][110];
#define MAXN 210
#define _clr(x) memset(x,0xff,sizeof(int)*MAXN)
int match1[MAXN],match2[MAXN];
int mat[MAXN][MAXN];
int s[MAXN],t[MAXN];
int hungary(int m,int n){
	int p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<m;ret+=(match1[i++]>=0))
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}
	return ret;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	scanf("%d",&nn);
	for (int ii=1;ii<=nn;ii++) {
		int n,m;
		printf("Case #%d: ",ii);
		scanf("%d%d",&n,&m);
		memset(match1,0,sizeof(match1));
		memset(match2,0,sizeof(match2));
		#define one(x) (x+x-2)
		#define two(x) (x+x-1)
		memset(mat,0,sizeof(mat));		
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=m;j++) scanf("%d",&mp[i][j]);
			for (int j=1;j<i;j++) {
				bool suc=1;
				for (int k=1;k<=m;k++) if (mp[j][k]>=mp[i][k]) {suc=0;break;}
				if (suc) mat[one(j)][two(i)]=1;
				suc=1;
				for (int k=1;k<=m;k++) if (mp[i][k]>=mp[j][k]) {suc=0;break;}
				if (suc) mat[one(i)][two(j)]=1;
			}
		}
		printf("%d\n",n-hungary(n+n,n+n));
	}
}
