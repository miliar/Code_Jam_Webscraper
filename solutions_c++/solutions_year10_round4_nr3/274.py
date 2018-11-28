#include <stdio.h>
#define debug(x)
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int kase=1;kase<=Test;++kase)
	{
		int n;
		int data[200][200];
		scanf("%d",&n);
		int m = 200;
		for (int q=0;q<m;++q) for (int w=0;w<m;++w) data[q][w] = 0;
		for (int q=0;q<n;++q)
		{
			int a,c,b,d;
			scanf("%d %d %d %d",&a,&c,&b,&d);a--;b--;c--;d--;
			for (int w=a;w<=b;++w) for (int e=c;e<=d;++e) data[e][w] = 1;
		}
		debug (for (int q=0;q<m;++q) for (int w=0;w<m;++w) printf("%d%c",data[q][w],(char)(w==m-1)?'\n':' '); )
		for (int t =0;;++t)
		{
			int cnt = 0;
			for (int q=0;q<m;++q) for (int w=0;w<m;++w)
			{
				cnt += data[q][w];
				if (data[q][w])
				{
					int ng = 0;
					if (q && (data[q-1][w]&1)) ng++;
					if (w && (data[q][w-1]&1)) ng++;
					if (ng) data[q][w] |= 2;
				}
				else
				{
					int ng = 0;
					if (q && (data[q-1][w]&1)) ng++;
					if (w && (data[q][w-1]&1)) ng++;
					if (ng==2) data[q][w] |= 2;
				}
			}
			for (int q=0;q<m;++q) for (int w=0;w<m;++w) data[q][w] >>= 1;
			if (!cnt) 
			{
				printf("Case #%d: %d\n",kase,t);
				break;
			}
		}

	}
	return 0;
}