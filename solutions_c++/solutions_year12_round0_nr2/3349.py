#include <stdio.h>
#include <math.h>


int max(int a, int b)
{
	return (a>b)? a: b;
}

int m(int x , int *s)
{
	int i,j,k;
	int c=0;

	for(i=0;i<=10;i++)
	{
		for(j=0;j<=10;j++)
		{
			for(k=0;k<=10;k++)
			{
				if((i + j + k == x) && abs(i - j) < 2 && abs(i - k) < 2 && abs(j - k) < 2)
				{
					c = max(c,max(max(i,j),k));
				}
				
				if((i + j + k == x) && abs(i - j) <= 2 && abs(i - k) <= 2 && abs(j - k) <= 2)
				{
					*s = max(*s,max(max(i,j),k));
				}
			}
		}
	}
	return c;
}


void main()
{
	FILE *infp = fopen("input.txt","r");
	FILE *outfp = fopen("output.txt","w");

	int N;
	int T;
	int S;
	int P;

	int a[101];

	int i,j,k;

	fscanf(infp,"%d",&T);

	for(k=1;k<=T;k++)
	{
		int cnt=0;

		fscanf(infp,"%d %d %d",&N,&S,&P);

		for(i=1;i<=N;i++)
		{
			int c;
			int s=0;
			fscanf(infp,"%d",&a[i]);
			c = m(a[i], &s);
			if(P <= c)
			{
				cnt++;
			}
			else if(P <= s && S>0)
			{
				cnt++;
				S--;
			}
		}
		fprintf(outfp,"Case #%d: %d\n",k,cnt);
	}
}
		