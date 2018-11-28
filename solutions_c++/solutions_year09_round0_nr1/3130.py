#include <stdio.h>
#include <string.h>

int l,d,n;
char dic[5005][20];
char w[1000];
char ws[20][50];
int wsl[20];

int main()
{
	int i,j,k,m;
	freopen("D:\\Projects\\GoogleCodeJam2009\\Qualification\\Task1\\Task1\\Debug\\A-large.in", "rt", stdin);
	freopen("D:\\Projects\\GoogleCodeJam2009\\Qualification\\Task1\\Task1\\Debug\\A-large.out", "wt", stdout);

	scanf("%d%d%d", &l, &d, &n);
	for (i=0; i<d; i++)
	{
		scanf("%s", dic[i]);
	}
	for (i=0; i<n; i++)
	{
		memset(wsl, 0, sizeof(wsl));
		memset(ws, 0, sizeof(ws));
		scanf("%s", w);
		int res=0;
		int wl = strlen(w);
		k=0;
		for (j=0; j<wl; j++, k++)
		{
			if (w[j]=='(')
			{
				for (j++;w[j]!=')';j++)
				{
					ws[k][wsl[k]++]=w[j];
				}
			}
			else
			{
				ws[k][wsl[k]++]=w[j];
			}
		}

		for (j=0; j<d; j++)
		{
			for (k=0; k<l; k++)
			{
				for (m=0; m<wsl[k]; m++)
				{
					if (ws[k][m]==dic[j][k])
					{
						break;
					}
				}
				if (m==wsl[k])
				{
					break;
				}
			}
			if (k==l)
			{
				res++;
			}
		}
		printf("Case #%d: %d", i+1, res);
		if (i<n-1)
		{
			printf("\n");
		}
	}

	return 0;
}