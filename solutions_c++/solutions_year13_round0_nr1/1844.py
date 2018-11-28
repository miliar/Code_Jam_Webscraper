#include <stdio.h>

int a[4][4];

int main()
{
	int ti = 0, tn;
	scanf("%d",&tn);
	while(tn--)
	{
		int result = 0;
		for(int i = 0; i < 4; ++i) 
		{
			char p[5];
			scanf(" %s",p);
			for(int j = 0; j < 4; ++j)
			{
				if(p[j] == 'T') a[i][j] = 3;
				else if(p[j] == 'O') a[i][j] = 2;
				else if(p[j] == 'X') a[i][j] = 1;
				else a[i][j] = 0;
				if(a[i][j] == 0) result = -1;
			}
		}
		for(int i = 0; i < 4; ++i) 
		{
			int t1 = 0;
			int t2 = 0;
			for(int j = 0; j < 4; ++j)
			{
				if(a[i][j] == 1 || a[i][j]  == 3) t1++;
				if(a[i][j] == 2 || a[i][j]  == 3) t2++;
			}
			if(t1 == 4) {result = 1; break;}
			if(t2 == 4) {result = 2; break;}
			t1 = t2 = 0;
			for(int j = 0; j < 4; ++j)
			{
				if(a[j][i] == 1 || a[j][i]  == 3) t1++;
				if(a[j][i] == 2 || a[j][i]  == 3) t2++;
			}
			if(t1 == 4) {result = 1; break;}
			if(t2 == 4) {result = 2; break;}
		}
		int t1 = 0;
		int t2 = 0;
		for(int i = 0; i < 4; ++i)
		{
			if(a[i][i] == 1 || a[i][i]  == 3) t1++;
			if(a[i][i] == 2 || a[i][i]  == 3) t2++;
		}
		if(t1 == 4) result = 1;
		if(t2 == 4) result = 2;
		t1 = t2 = 0;
		for(int i = 0; i < 4; ++i)
		{
			if(a[i][3-i] == 1 || a[i][3-i]  == 3) t1++;
			if(a[i][3-i] == 2 || a[i][3-i]  == 3) t2++;
		}
		if(t1 == 4) result = 1;
		if(t2 == 4) result = 2;

		printf("Case #%d: ", ++ti);
	
		if(result == 1) printf("X won\n");
		else if(result == 2) printf("O won\n");
		else if(result == 0) printf("Draw\n");
		else printf("Game has not completed\n");

	}
}
