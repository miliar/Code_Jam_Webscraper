#include <stdio.h>
#define debug(sen) 
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int kase=1;kase<=Test;++kase)
	{
		debug(if (kase>6) break;)
		int n;
		int arr[55][55];
		scanf("%d",&n);
		int sq[55][55];
		int y=0,x=0;
		for (int q=0;q<n;++q)
			for (int w=0;w<=q;++w)
				scanf("%d",&sq[q-w][w]);
		for (int q=1;q<n;++q)
			for (int w=0;w<n-q;++w)
				scanf("%d",&sq[n-1-w][q+w]);
		debug( for (int q=0;q<n;++q,printf("\n")) for (int w=0;w<n;++w) printf("%d ",sq[q][w]) );
		int value[105][105];
		int mark[105][105];
		for (int sz = n;;++sz)
		{
			int good = 0;
			for (int y=0;y+n<=sz;++y) for (int x=0;x+n<=sz;++x)
			{
				for (int q=0;q<sz;++q) for (int w=0;w<sz;++w) mark[q][w] = 0;
				for (int q=0;q<n;++q) for (int w=0;w<n;++w) 
				{
					value[y+q][w+x] = sq[q][w];
					mark[y+q][w+x] = 1;
				}
				int conflict = 0;
				for (int q=0;q<sz && !conflict;++q) for (int w=0;w<sz && !conflict;++w)
				{
					if (mark[q][w] && mark[w][q] && value[q][w]!=value[w][q]) conflict = 1;
					if (mark[q][w] && mark[sz-1-w][sz-1-q] && value[q][w]!=value[sz-1-w][sz-1-q]) conflict = 1;
				}
				if (!conflict) { good=1; break; }
			}
			if (good) 
			{
				debug( for (int q=0;q<sz;++q,printf("\n")) for (int w=0;w<sz;++w) if (mark[q][w]) printf("%d ",value[q][w]); else printf("- "); )
						
				debug(printf("%d\n",sz);)
				printf("Case #%d: %d\n",kase,sz*sz - n*n);
				break;
			}
		}
	}
	return 0;
}