#include <stdio.h>
#include <string.h>

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

const int len=128;
const int maxs=128;
const int maxq=1024;
const int inf=0x7fffffff;
char s[maxs][len],qs[maxq][len];
int d[2][maxs];

int main(){
	int t,c;
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d",&t);
	for(c=1; c<=t; c++){
		int m[2],k,q,n,i,j,u;
		scanf("%d\n",&n);
		for(i=0; i<n; i++)
			gets(s[i]);
		scanf("%d\n",&q);
		for(i=0; i<q; i++)
			gets(qs[i]);
		m[0]=0;
		m[1]=1;
		for(i=0; i<n; i++)
			d[0][i]=0;
		for(i=q-1,k=0; i>=0; i--,k=1-k){
			for(u=0; u<n; u++)
				if(strcmp(s[u],qs[i])==0) break;
			for(j=0; j<n; j++){
				int &f=d[1-k][j];
				f=inf;
				if(u!=j)
					f=d[k][j];
				if(u!=m[0])
					f=min(f,d[k][m[0]]+1);
				else
					f=min(f,d[k][m[1]]+1);
			}
			m[0]=m[1]=-1;
			for(j=0; j<n; j++){
				if(m[0]<0||d[1-k][j]<d[1-k][m[0]]){
					m[1]=m[0];
					m[0]=j;
				}else if(m[1]<0||d[1-k][j]<d[1-k][m[1]])
					m[1]=j;
			}
		}
		printf("Case #%d: %d\n",c,d[k][m[0]],n,q);
	}
	return 0;
}
