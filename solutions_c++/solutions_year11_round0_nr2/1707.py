#include<cstdio>
#include<cstdlib>
#include<cstring>

int Value(char ch)
{
	int ret = -1;
	switch(ch)
	{
		case 'Q':
			ret = 0;
			break;
		case 'W':
			ret = 1;
			break;
		case 'E':
			ret = 2;
			break;
		case 'R':
			ret = 3;
			break;
		case 'A': 
			ret = 4;
			break;
		case 'S': 
			ret = 5;
			break;
		case 'D': 
			ret = 6;
			break;
		case 'F':
			ret = 7;
			break;
		default:
			ret = -1;
			break;
	}
	return ret;
}

char MatCom[8][8];
bool MatOpp[8][8];

int main()
{
	int T, cas;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int i, j, k, C, D, N;
		int x, y;
		memset(MatCom, 0, sizeof(MatCom));
		memset(MatOpp, 0, sizeof(MatOpp));
		
		char Com[16];
		scanf("%d", &C);
		for(i = 0; i < C; i ++)
		{
			scanf("%s", Com);
			x = Value(Com[0]);
			y = Value(Com[1]);
			if(x == -1 || y == -1)continue;
			MatCom[x][y] = Com[2];
			MatCom[y][x] = Com[2];
		}
		
		char Opp[16];
		scanf("%d", &D);
		for(i = 0; i < D; i ++)
		{
			scanf("%s", Opp);
			x = Value(Opp[0]);
			y = Value(Opp[1]);
			if(x == -1 || y == -1)continue;
			MatOpp[x][y] = true;
			MatOpp[y][x] = true;
		}
		
		char base[128];
		scanf("%d", &N);
		scanf("%s", base);
		bool sep;
		for(i = 0; i < N; i ++)
		{
			sep = false;
			x = Value(base[i]);
			for(j = i-1; j >= 0; j --)
			{
				y = Value(base[j]);
				if(y == -1)
				{
					if(base[j]!='?')sep = true;
					continue;
				}
				
				if(MatCom[x][y] != 0 && sep == false)
				{
					base[i] = MatCom[x][y];
					base[j] = '?';
					break;
				}
				else 
				{
					sep = true;
					if(MatOpp[x][y] != 0)
					{
						for(k = 0; k <= i; k ++)
						{
							base[k] = '?';
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: [", cas);
		
		bool first = true;
		for(i = 0; i < N; i ++)
		{
			if(base[i] != '?')
			{
				if(!first)printf(", ");
				putchar(base[i]);
				first = false;
			}
		}
		printf("]\n");
	}
	return 0;
}
