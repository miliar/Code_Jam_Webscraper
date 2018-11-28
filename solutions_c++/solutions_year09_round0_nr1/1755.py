#include <stdio.h>
#include <string.h>
#include <algorithm>
using  namespace std;

const  int MAXN = 5000+10;
char  s[MAXN][20];
int  L, D, N;
char  p[1000];
bool  bj[30][30];
bool  head[30];
int  calc()
{
	int  ret = 0;
	int  i, j;
	bool  tag = false;
	memset(bj, false, sizeof(bj));
	j = 0; 
    if(p[0] == '(') 
	{
		tag = true;
		j++;
	}

	for(i = 0; i < L; i++)
	{
		if(tag == false)
		{
			bj[i][p[j]-'a'] = true;	
		}
		else
		{
			while(p[j] != ')')
			{
				if(p[j] >= 'a' && p[j] <= 'z')
					bj[i][p[j]-'a'] = true;
				j++;
			}
		}
		j++;
		if(p[j] == '(') tag = true;
		else  tag = false;
	}
	for(i = 0; i < D; i++)
	{
 		for(j = 0; j < L; j++)
		{
			if(!bj[j][s[i][j]-'a'])
				break;
		}
		if(j == L) ret++;
	}
	return ret;
}
int  main()
{
	int  i;
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	while(scanf("%d %d %d", &L, &D, &N) != EOF)
	{
		for(i = 0; i < D; i++)
		{
			scanf("%s", s[i]);
		}
		for(i = 1; i <= N; i++)
		{
			scanf("%s", p);
			printf("Case #%d: %d\n", i, calc());
		}
	}	
	return 0;
}
