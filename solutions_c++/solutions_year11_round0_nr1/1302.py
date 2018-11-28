#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
//---------------------------------------------
// 
int main ()
{
	int testsCount, n, i, delta, result, oPosition, bPosition, timeForO, timeForB, cost, tmp;
	char color;

	scanf_s("%d", &testsCount); 
	for (int testNo = 1; testNo <= testsCount; ++testNo)
	{
		// Read commands
		scanf_s("%d", &n);
		
		oPosition = 1;
		bPosition = 1;


		timeForO = 0;
		timeForB = 0;
		result = 0;
		
		for (i = 0; i < n; i++)
		{
			scanf_s(" %c %d", &color, 1, &tmp);
			if (color == 'O')
			{
				cost = abs(tmp-oPosition) + 1;
				delta = (timeForO >= cost) ? 1: cost - timeForO;
				result += delta;
				oPosition = tmp;
				timeForO = 0;
				timeForB += delta;
			}
			else
			{
				cost = abs(tmp-bPosition) + 1;
				delta = (timeForB >= cost) ? 1: cost - timeForB;
				result += delta;
				bPosition = tmp;
				timeForO += delta;
				timeForB = 0;
			}
		}

		printf("Case #%d: %d", testNo, result);
		puts("");
	}

	return 0;
}
