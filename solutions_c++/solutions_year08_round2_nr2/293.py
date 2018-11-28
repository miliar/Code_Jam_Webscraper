#include <stdio.h>
#include <string.h>

int a,b,p,i,j,k,f,r;
int cs,ct,tot,w[1001][1001],l[1001],mark[1001];

int gcd(int x,int y)
{
	if (!y) return x;
	else return gcd(y,x%y);
}

int main()
{
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
		memset(mark,0,sizeof(mark));
		tot=0;
		for (i=a;i<=b;i++)
		if (!mark[i]) {
			mark[i]=1;
			f=0; r=1; l[0]=i;
			while (f<r) {
				for (j=a;j<=b;j++)
				if (!mark[j] && w[l[f]][j]) {
					mark[j]=1;
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
