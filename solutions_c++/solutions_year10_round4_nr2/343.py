#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <math.h>

using namespace std;

int * x[20];
int m[1<<20];

int bt(int l,int s,int p,int b,int e)
{
	if (l==p)
	{
		if (s>m[b]) return -1; else return 0;
	} else
	{
		int i,j,k;
		for (i=b;i<e;++i) if (s>m[i]) return -1;
//		printf("%d %d %d %d\n",p,l,b,x[p-l-1][b>>(p-l-1)]);
		i=bt(l+1,s,p,b,b+(e-b)/2)+bt(l+1,s,p,b+(e-b)/2,e)+x[l][b>>(p-l)];
		j=bt(l+1,s+1,p,b,b+(e-b)/2);
		if (j!=-1)
		{
			k=bt(l+1,s+1,p,b+(e-b)/2,e);
			if (k!=-1)
			{
				if (j+k<i) return j+k;
			}
		}
		return i;
	}
}

int main()
{
	int case_c,p,i,j;
	for (i=0;i<20;++i) x[i]=(int*)malloc((1<<i)*sizeof(int));
	scanf("%d",&case_c);
	case_c=0;
	while (scanf("%d",&p)==1)
	{
		for (i=0;i<(1<<p);++i) scanf("%d",m+i);
		for (j=p-1;j>=0;--j) for (i=0;i<(1<<j);++i) scanf("%d",x[j]+i);
		printf("Case #%d: %d\n",++case_c,bt(0,0,p,0,(1<<p)));
	}
	for (i=0;i<20;++i) free(x[i]);
	return 0;
}
