#include <cstdio>
#include <cstring>

const int maxn = 10;

char map[maxn][maxn];

inline bool judgex(char a)
{
	if(a == 'X' || a == 'T')
		return true;
	return false;
}

inline bool judgeo(char a)
{
	if(a == 'O' || a == 'T')
		return true;
	return false;
}

int main()
{
	freopen("d://test/a.in", "r", stdin);
	freopen("d://test/a.out", "w", stdout);
	bool x, o, d;
	int i, j, t, cnt = 0;
	
	scanf("%d", &t);
	while(t--)
	{
		for(i = 0; i < 4; i++)
			scanf("%s", map[i]);
		x = o = d = false;
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
				if(!judgex(map[i][j]))
					break;
			if(j == 4)
			{
				x = true;
				break;
			}
		}
		for(i = 0; i < 4; i++)
		{
			for(j = 0; j < 4; j++)
				if(!judgex(map[j][i]))
					break;
			if(j == 4)
			{
				x = true;
				break;
			}
		}
		for(i = 0; i < 4; i++)
			if(!judgex(map[i][i]))
				break;
		if(i == 4)
			x = true;
		for(i = 0; i < 4; i++)
			if(!judgex(map[i][3-i]))
				break;
		if(i == 4)
			x = true;
		if(!x)
		{
			for(i = 0; i < 4; i++)
			{
				for(j = 0; j < 4; j++)
					if(!judgeo(map[i][j]))
						break;
				if(j == 4)
				{
					o = true;
					break;
				}
			}
			for(i = 0; i < 4; i++)
			{
				for(j = 0; j < 4; j++)
					if(!judgeo(map[j][i]))
						break;
				if(j == 4)
				{
					o = true;
					break;
				}
			}
			for(i = 0; i < 4; i++)
				if(!judgeo(map[i][i]))
					break;
			if(i == 4)
				o = true;
			for(i = 0; i < 4; i++)
				if(!judgeo(map[i][3-i]))
					break;
			if(i == 4)
				o = true;
		}
		if(!x && !o)
		{
			for(i = 0; j < 4; i++)
				for(j = 0; j < 4; j++)
					if(map[i][j] == '.')
					{
						d = true;
						break;
					}
		}
		if(x)
			printf("Case #%d: X won\n", ++cnt);
		else if(o)
			printf("Case #%d: O won\n", ++cnt);
		else if(d)
			printf("Case #%d: Game has not completed\n", ++cnt);
		else
			printf("Case #%d: Draw\n", ++cnt);
	}
	return 0;
}