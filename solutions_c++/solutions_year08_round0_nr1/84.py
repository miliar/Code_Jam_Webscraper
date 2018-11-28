#include <stdio.h>
#include <string>
using namespace std;

int tc, ntc;
int n, m;
string a[110], b[1100];

char buf[10000];
int main()
{
	scanf("%d",&ntc);
	int i, j;
	int res;
	int cur;
	int tmax, tmp;
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%d",&n); gets(buf);
		for (i=0; i<n; i++) 
		{
			gets(buf);
			a[i] = buf;
		}
		
		scanf("%d",&m); gets(buf);
		for (i=0; i<m; i++)
		{
			gets(buf);
			b[i] = buf;
		}
		
		res = 0;
		cur = 0;
		while (true)
		{
			tmax = 0;
			for (i=0; i<n; i++)
			{
				tmp = find( b+cur, b+m, a[i] ) - b;
				if (tmp == m) goto fin;
				if (tmp > tmax) tmax = tmp;
			}
			res++;
			cur = tmax;
		}
		
		fin:;
		printf("Case #%d: %d\n",tc, res);
	}
}