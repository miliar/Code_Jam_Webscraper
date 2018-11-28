#include <stdio.h>
#include <string.h>

int a,b,p,i,j,k,f,r;
int cs,ct,tot,l[1001],mrk[1001];
int w[1001][1001];

int gcd(int x,int y)
{
	if (x%y==0) return y;
	else return gcd(y,x%y);
}

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
	scanf("%d",&cs);
	for (ct=1;ct<=cs;ct++) {
		scanf("%d%d%d",&a,&b,&p);
		memset(w,0,sizeof(w));
		for (i=a;i<=b;i++)
		for (j=i+1;j<=b;j++)
		{
			r=gcd(i,j);
			f=0;
			for (k=2;k<=r;)
			if (r%k==0) {
				r/=k;
				if (k>=p) { f=1; break; }
				break;
			} else k++;
			if (f) {
				w[i][j]=w[j][i]=1;
//				if (i==16 || j==16) printf("*%d %d %d ",i,j,r);
			}
		}
		memset(mrk,0,sizeof(mrk));
		tot=0;
		for (i=a;i<=b;i++)
		if (!mrk[i]) {
			mrk[i]=1;
			f=0; r=1; l[0]=i;
			while (f<r) {
				for (j=a;j<=b;j++)
				if (!mrk[j] && w[l[f]][j]) {
					mrk[j]=1;
					l[r++]=j;
				}
				f++;
			}
			tot++;
		}
		printf("Case #%d: %d\n",ct,tot);
	}
	return 0;
}
