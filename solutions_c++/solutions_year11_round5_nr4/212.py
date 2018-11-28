#include <stdio.h>
#include <math.h>

int x[500];
int y[500];

long long go(char * s, long long a)
{
	if (*s==0)
	{
		long long p=sqrt((double)a);
		if (p*p==a || (p-1)*(p-1)==a || (p+1)*(p+1)==a) return a; else return -1;
	} else
	{
		if (*s=='0') return go(s+1,a*2);
		if (*s=='1') return go(s+1,a*2+1);
		long long l=go(s+1,a*2);
		if (l==-1) return go(s+1,a*2+1); else return l;
	}
}

void p(long long a)
{
	if (a==0) return;
	p(a/2);
	if (a&1) printf("1"); else printf("0");
}

int main()
{
	int ic,nc;
	char s[150];
	scanf("%d",&nc);
	for (ic=1;ic<=nc;++ic)
	{
		scanf("%s",s);
		printf("Case #%d: ",ic);
		p(go(s,0));
		printf("\n");
	}
	return 0;
}
