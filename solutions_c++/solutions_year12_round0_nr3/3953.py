#include <stdio.h>
#include <string.h>

int cases;

int main()
{
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		int res=0, a, b; scanf(" %d %d", &a, &b);
		char xx[10]; sprintf(xx, "%d", b);
		for(int z=a; z<=b; z++)
		{
			char x[10][10];
			sprintf(x[0], "%d", z);
			int l=strlen(x[0]);
			for(int j=1; j<l; j++)
				for(int i=0; i<l; i++)
					x[j][i]=x[0][(i+j)%l];
			for(int j=1; j<l; j++)
			{
				x[j][l]=0;
				if (strcmp(x[0], x[j])>-1) continue;
				if (strcmp(xx, x[j])<0) continue;
				for(int i=1; i<j; i++)
					if (!strcmp(x[i], x[j])) goto weiter;
				// printf("%s %s\n", x[0], x[j]);
				res++;
			weiter:;
			}
		}
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}
