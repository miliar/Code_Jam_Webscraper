#include <stdio.h>

int main()
{
	int ca;
	
	freopen("B-large.in" , "r" , stdin);
	freopen("B-large.out" , "w" , stdout);
	scanf("%d" , &ca);
	for (int cas = 1; cas <= ca; cas ++)
	{
		int cn;
		char c[40][5];
		int dn;
		char d[30][4];
		int n;
		char s[150];
		scanf("%d" , &cn);
		for (int i = 0; i < cn; i ++) scanf("%s" , c[i]);
		scanf("%d" , &dn);
		for (int i = 0; i < dn; i ++) scanf("%s" , d[i]);
		scanf("%d" , &n);
		scanf("%s" , s);
		char res[150] = "";
		int L = 0;
		for (int i = 0; i < n; i ++)
		{
			char x = s[i];
			if (L > 0)
			{
				char y = res[L-1];
				int comb = 0;
				for (int j = 0; j < cn; j ++)
					if ((c[j][0] == x && c[j][1] == y) || (c[j][0] == y && c[j][1] == x))
					{
						comb = 1;
						x = c[j][2];
						break;
					}
				if (comb == 1)
				{
					res[L-1] = x;
					continue;
				}
			}
			int opp = 0;
			for (int j = L-1; j >= 0; j --)
			{
				char y = res[j];
				opp = 0;
				for (int k = 0; k < dn; k ++)
					if ((d[k][0] == x && d[k][1] == y) || (d[k][0] == y && d[k][1] == x))
					{
						opp = 1;
						break;
					}
				if (opp == 1)
				{
					L = 0;
					break;
				}
			}
			if (opp == 1) continue;
			res[L++] = x;
		}
		printf("Case #%d: [" , cas);
		if (L > 0)
		{
			printf("%c" , res[0]);
			for (int i = 1; i < L; i ++)
				printf(", %c" , res[i]);
		}
		printf("]\n");
	}
	return 0;
}