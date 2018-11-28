#include <stdio.h>

int data[10000];

int main()
{
	FILE* fp=fopen("c:\\c-small.in","r");
	FILE* fp2=fopen("c:\\c-small.txt","w");
#if 0
#define fp stdin
#define fp2 stdout
#endif
	int T;
	fscanf(fp,"%d",&T);
	for (int t=1; t<=T; t++)
	{
		int n,l,h;
		fscanf(fp,"%d%d%d",&n,&l,&h);

		for (int i=0; i<n; i++)
		{
			fscanf(fp,"%d",&data[i]);
		}

		for (int i=l; i<=h; i++)
		{
			int j;
			for (j=0; j<n; j++)
			{
				if (i%data[j] && data[j]%i) break;
			}
			if (j==n)
			{
				fprintf(fp2,"Case #%d: %d\n", t, i);
				goto out;
			}
		}

		fprintf(fp2,"Case #%d: NO\n", t);

out:
		;
	}
	return 0;
}