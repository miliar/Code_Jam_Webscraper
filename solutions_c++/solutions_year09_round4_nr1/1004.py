#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
	int t, n;
	bool isGood;
	int findIdx;
	int result;
	scanf("%d", &t);
	char table[41][41];

	for(int i = 0; i < t; i++)
	{
		scanf("%d\n", &n);

		for(int j = 0; j < n; j++)
		{
			scanf("%s", table[j]);
		}

		result = 0;

		for(int j = 0; j < n; j++)
		{
			findIdx = -1;
			for(int k = j; k < n; k++)
			{
				isGood = true;
				for(int l = j+1; l < n && isGood; l++)
				{
					if(table[k][l] == '1') isGood = false;
				}
				if(isGood)
				{
					findIdx = k;
					break;
				}
			}
			if(findIdx >= 0)
			{	
				result += findIdx - j;
			}
			for(int k = findIdx; k > j; k--)
			{
				strcpy(table[k], table[k-1]);
			}
		}

		printf("Case #%d: %d\n", i+1, result);


	}

	return 0;
}