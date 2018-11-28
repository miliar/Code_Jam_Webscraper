#include<stdio.h>
#include<string.h>

char a[1111][1111];
int n, m;
int b[1111];
int D[1111][1111];
char s[1111];

#define INF 1000000000

int main(void)
{
	int T, l0;
	int l1, l2, l3;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		scanf("%d",&n);
		gets(s);
		for(l1=0;l1<n;l1++)
		{
			gets(a[l1]);
		}

		scanf("%d",&m);
		gets(s);
		for(l1=0;l1<m;l1++)
		{
			gets(s);
			for(l2=0;l2<n;l2++)
			{
				if(s[0] == a[l2][0] && strcmp(s, a[l2]) == 0)
				{
					b[l1] = l2;
					break;
				}
			}
		}

		for(l1=0;l1<n;l1++)
		{
			D[0][l1] = 0;
		}
		D[0][b[0]] = INF;

		for(l1=1;l1<m;l1++)
		{
			for(l2=0;l2<n;l2++)
			{
				D[l1][l2] = INF;
				if(b[l1] == l2){ D[l1][l2] = INF; continue; }
				if(D[l1][l2] > D[l1-1][l2]) D[l1][l2] = D[l1-1][l2];
				for(l3=0;l3<n;l3++)
				{
					if(l2 == l3) continue;
					if(D[l1][l2] > D[l1-1][l3] + 1) D[l1][l2] = D[l1-1][l3] + 1;
				}
			}
		}

		int ret = INF;
		for(l1=0;l1<n;l1++) if(ret > D[m-1][l1]) ret = D[m-1][l1];
		printf("Case #%d: %d\n",l0,ret);
	}

	return 0;
}