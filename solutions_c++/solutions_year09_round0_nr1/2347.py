#include <stdio.h>

int l, n, d;
char dic[5000][16], p[15][256], nc;
int res;

int main()
{
	scanf(" %d %d %d", &l, &d, &n);
	for(int i=0; i<d; i++)
		scanf(" %s", dic[i]);
	for(int cs=1; cs<=n; cs++)
	{
		res=0;
		for(int i=0; i<15; i++)
			for(int j=0; j<256; j++)
				p[i][j]=0;
		for(int pos=0; pos<l; pos++)
		{
			scanf(" %c", &nc);
			if (nc=='(')
			{
				while(nc!=')')
				{
					scanf(" %c", &nc);
					if (nc!=')')
						p[pos][int(nc)]=1;					
				}
			}
			else
				p[pos][int(nc)]=1;
		}
		for(int i=0; i<d; i++)
		{
			for(int j=0; j<l; j++)
				if (!p[j][int(dic[i][j])]) goto weiter;
			res++;
		weiter:;
		}
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}
