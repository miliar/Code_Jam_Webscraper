#include <cstdio>
#include <cstring>

using namespace std;

int a[256][256], b[256][256];
int t, c, d, n, i, j, k, ii, gasit;
char c1, c2, c3, s[113];

void init()
{
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
}

int main()
{
	freopen("magicka.in" , "r" , stdin);
	freopen("magicka.out" , "w" , stdout);
	scanf("%d\n", &t);
	for(k = 1 ; k <= t ; ++k)
	{
		memset(s,'0',sizeof(s));
		j = 0;
		init();
		scanf("%d ", &c);
		for(i = 1 ; i <= c ; ++i)
		{
			scanf("%c%c%c ", &c1, &c2, &c3);
			a[c1][c2] = a[c2][c1] = c3;
		}
		scanf("%d ", &d);
		for(i = 1 ; i <= d ; ++i)
		{
			scanf("%c%c ", &c1, &c2);
			b[c1][c2] = b[c2][c1] = 1;
		}
		scanf("%d ", &n);
		for(i = 0 ; i < n ; ++i)
		{
			scanf("%c", &c1);
			gasit = 0;
			if(a[s[j-1]][c1])
				s[j-1] = (char)a[s[j-1]][c1];
			else
			{
				for(ii = 0 ; ii < j ; ++ii)
					if(b[s[ii]][c1])
						gasit = 1;
				if(gasit == 1)
				{
					for(ii = 0 ; ii < j ; ii++);
						s[ii] = '0';
					j = 0;
				}
				else
				{
					s[j] = c1;
					j++;
				}
			}
		}
		printf("Case #%d: ", k);
		if(j == 0)
			printf("[]\n");
		else
		{
			printf("[");
			for(ii = 0 ; ii < j-1 ; ++ii)
				printf("%c, ",s[ii]);
			printf("%c]",s[j-1]);
			printf("\n");
		}
		scanf("\n");
	}
	return 0;
}