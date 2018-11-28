#include <stdio.h>
#include <string.h>

long long n,m,x0,y0,a,b,c,d,tot;
long long w[3][3];

int main()
{
//	freopen("1.in","r",stdin);
	int cs,i;
	scanf("%d",&cs);
	for (int ct=1;ct<=cs;ct++) {
		scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d",&n,&a,&b,&c,&d,&x0,&y0,&m);
		memset(w,0,sizeof(w));
		w[x0%3][y0%3]++;
		for (i=1;i<n;i++) {
			x0=(a*x0+b)%m;
			y0=(c*y0+d)%m;
			w[x0%3][y0%3]++;
		}
		tot=0;
		for (a=0;a<9;a++)
		for (b=a;b<9;b++)
		for (c=b;c<9;c++)
		if ((a%3+b%3+c%3)%3==0 && (a/3+b/3+c/3)%3==0)
		{
			if (a==b && a==c) tot+=w[a/3][a%3]*(w[a/3][a%3]-1)*(w[a/3][a%3]-2)/6;
			else if (a==b) tot+=w[a/3][a%3]*(w[a/3][a%3]-1)*w[c/3][c%3]/2;
			else if (a==c) tot+=w[a/3][a%3]*(w[a/3][a%3]-1)*w[b/3][b%3]/2;
			else if (b==c) tot+=w[a/3][a%3]*w[b/3][b%3]*(w[c/3][c%3]-1)/2;
			else tot+=w[a/3][a%3]*w[b/3][b%3]*w[c/3][c%3];
			if (tot>1e16) printf("**");
		}
		printf("Case #%d: %I64d\n",ct,tot);
	}
	return 0;
}
