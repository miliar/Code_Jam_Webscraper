/* 2012
 * Maciej Szeptuch
 * II UWr
 */
#include<cstdio>
#include<vector>
#include<set>

int tests,
    start,
    end,
    result;

int checkMoves(int base, int start, int end);

int main(void)
{
	scanf("%d ", &tests);
	for(int t = 0; t < tests; ++ t)
	{
		result = 0;
		scanf("%d %d", &start, &end);
		for(int s = start; s <= end; ++ s)
			result += checkMoves(s, start, end);

		printf("Case #%d: %d\n", t + 1, result);
	}

	return 0;
}

int checkMoves(int base, int start, int end)
{
	std::set<std::pair<int, int> > uniq;
	int req = 1,
	    act;
	for(int b = base; b > 0; b /= 10)
		req *= 10;

	for(int b = base, q = 10; b > 0; b /= 10, q *= 10)
	{
		if(base % q == 0)
			continue;

		act = (base % q) * req / q + base / q;
		if(act >= start && act > base && act <= end)
			uniq.insert(std::make_pair(base, act));
	}

	return uniq.size();
}
