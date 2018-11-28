#include <cstdio>
#include <cstring>

using namespace std;

bool poss[110][2] = { {false} };

int main()
{
	int T;
	scanf(" %d", &T);
	for(int z = 1; z <= T; z ++)
	{
		int n, s, p;
		int normal = 0, both = 0, special = 0;
		scanf(" %d %d %d", &n, &s, &p);
		for(int i = 0; i < n; i ++)
		{
			int t;
			scanf(" %d", &t);
			if(t < 2 || t > 28)
			{
				if(t % 3 == 0)
				{
					if(t / 3 >= p)
						poss[i][0] = true;
				}
				else
					if(t / 3 + 1 >= p)
						poss[i][0] = true;
			}
			else
			{
				if(t % 3 == 0)
				{
					if(t / 3 >= p)
						poss[i][0] = poss[i][1] = true;
				}
				else
					if(t / 3 + 1 >= p)
						poss[i][0] = poss[i][1] = true;
				if(!poss[i][0])
				{
					if(t % 3 == 0)
					{
						if(t / 3 + 1 >= p)
							poss[i][1] = true;
					}
					else if(t % 3 == 1)
					{
						if(t / 3 + 1 >= p)
							poss[i][1] = true;
					}
					else if(t % 3 == 2)
					{
						if(t / 3 + 2 >= p)
							poss[i][1] = true;
					}
				}
			}
			if(poss[i][0] == true && poss[i][1] == true)
				both ++;
			else if(poss[i][0] == true)
				normal ++;
			else if(poss[i][1] == true)
				special ++;
		}
		int _s = s;
		int ans = 0;
		if(s > special)
		{
			s -= special;
			ans += special;
			special = 0;
		}
		else if(s <= special)
		{
			special -= s;
			ans += s;
			s = 0;
		}
		if(s > both)
		{
			s -= both;
			ans += both;
			both = 0;
		}
		else if(s <= both)
		{
			both -= s;
			ans += s;
			s = 0;
		}
		if(normal + both > n - _s)
		{
			ans += n - _s;
		}
		else
			ans += normal + both;
		memset(poss, false, sizeof(poss));
		printf("Case #%d: %d\n", z, ans);
	}
	return 0;
}
