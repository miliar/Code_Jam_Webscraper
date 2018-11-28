#include<stdio.h>
#include<string.h>

int D[1000][33];
int ACC[1000][33];
char *p="welcome to code jam";
char a[555];
int n, m;
int T;

int main(void)
{
	int l0, l1, l2, l3;

	freopen("C2.in","r",stdin);
	freopen("C2.out","w",stdout);

	gets(a);
	sscanf(a,"%d",&T);
	for(l0=1;l0<=T;l0++)
	{
		gets(a);

		n = strlen(a);
		m = strlen(p);

		for(l1=0;l1<n;l1++) for(l2=0;l2<m;l2++) D[l1][l2] = ACC[l1][l2] = 0;

		for(l1=0;l1<n;l1++)
		{
			if(a[l1] == 'w')
			{
				D[l1][0] = 1;
			}

			for(l2=1;l2<m;l2++)
			{
				if(a[l1] == p[l2])
				{
					D[l1][l2] += ACC[l1-1][l2-1];
					D[l1][l2] %= 10000;
				}
			}


			if(l1 != 0)
			{
				for(l2=0;l2<m;l2++)
				{
					ACC[l1][l2] = ACC[l1-1][l2] + D[l1][l2];
					ACC[l1][l2] %= 10000;
				}
			}
			else
			{
				for(l2=0;l2<m;l2++)
				{
					ACC[l1][l2] = D[l1][l2];
				}
			}
		}

		printf("Case #%d: %04d\n",l0,ACC[n-1][m-1]);
	}

	return 0;
}