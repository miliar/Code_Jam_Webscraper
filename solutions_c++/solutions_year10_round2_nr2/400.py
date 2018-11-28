#include <cstdio>
#include <vector>

using std::vector;

int main()
{
	int tests;
	std::scanf("%d", &tests);
	for (int testcase = 1; testcase <= tests; testcase++)
	{
		int chicks, need, barn, time;
		std::scanf("%d%d%d%d", &chicks, &need, &barn, &time);
		
		vector<int> loc(chicks);
		for (int i = 0; i < chicks; i++) std::scanf("%d", &(loc[i]));
		
		vector<int> speed(chicks);
		for (int i = 0; i < chicks; i++) std::scanf("%d", &(speed[i]));
		
		vector<bool> gets(chicks, false);
		vector<int> overtakes(chicks, 0);
		
		for (int i = 0; i < chicks; i++)
			gets[i] = loc[i] + speed[i]*time >= barn;
			
		overtakes[chicks-1] = 0;
		for (int i = chicks-2; i >= 0; i--)
			overtakes[i] = overtakes[i+1] + (gets[i+1] ? 0 : 1);
			
		int canget = 0;
		for (int i = 0; i < chicks; i++)
			if (gets[i]) canget++;
			
		if (canget < need) {std::printf("Case #%d: IMPOSSIBLE\n", testcase);}
		else
		{
			int swaps = 0;
			int has = 0;
			for (int i = chicks-1; has < need; i--)
				if (gets[i])
				{
					swaps += overtakes[i];
					has++;
				}
				
			std::printf("Case #%d: %d\n", testcase, swaps);
		}
	}

	return 0;
}
