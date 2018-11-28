#include <stdio.h>

int ok(char s[][55], int r, int c)
{
	int i,j;
	for (i=0; i<r; i++)
	{
		for (j=0; j<c; j++)
		{
			if (s[i][j]=='#')
			{
				if (j+1>=c || s[i][j+1]!='#') return 0;
				if (i+1>=r || s[i+1][j]!='#') return 0;
				if (s[i+1][j+1]!='#') return 0;
				s[i][j]='/'; s[i][j+1]='\\';
				s[i+1][j]='\\'; s[i+1][j+1]='/';
			}
		}
	}
	return 1;
}

int main()
{
	int t,c,r,i;
	char s[55][55];
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&t);
	for (int cas = 1; cas <= t; cas++)
	{
		scanf("%d%d",&r,&c);
		for (i=0; i<r; i++) scanf("%s",s[i]);
		printf("Case #%d:\n",cas);
		if (ok(s,r,c)) {
			for (i=0; i<r; i++) printf("%s\n",s[i]);
		} else {
			printf("Impossible\n");
		}
	}
	return 0;
}

/*
3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##.. 
*/