#include <cstdio>
#include <cstring>

char a[10000][16];

int main()
{
	int l,n,tn;
	freopen("A-large.in","r",stdin);
	freopen("output.txt", "w" ,stdout);

	scanf("%d %d %d",&l,&n,&tn);
	for(int i = 0; i < n; i++)
		scanf("%s",a[i]);
	int ti = 0;
	while(tn--)
	{
		int ans = 0;
		char p[1024];
		scanf("%s",p);
		int len = strlen(p);
		for(int j = 0; j < n; j++)
		{
			int cc = 0;
			int op = 0;
			int ww = 0;
			int t = 0;
			for(int i = 0; i < len; i++)
			{
				if (p[i] == '(') op = 1;
				else if (p[i] == ')') 
				{
					if (cc == 0) break;
					op = cc = 0;
					t++;
				}
				else
				{
					if (a[j][t] == p[i]) 
					{
						cc = 1;
						if (op == 0) t++;
					}
					else if (op == 0) break;
				}
			}
			if (t == l) ans++;
		}
		printf("Case #%d: %d\n", ++ti, ans);
	}
}

/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/