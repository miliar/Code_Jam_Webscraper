#include <cstdio>

int rightmost[45];

int main()
{
	int testIndex, testCount;
	scanf("%d", &testCount);
	for(testIndex = 1; testIndex <= testCount; testIndex++)
	{
		char buff[45];
		int n;
		int move = 0;
		scanf("%d\n", &n);
		int i,j;
		for(i = 0; i < n; i++)
		{
			scanf("%s", buff);
			rightmost[i] = 0;
			for(j = 0; j < n; j++)
				if(buff[j] == '1')rightmost[i] = j;
		}

		for(i = 0; i < n; i++)
		{
			for(j = i; rightmost[j] > i; j++);
			for(; j > i; j--)
			{
				int t = rightmost[j];
				rightmost[j] = rightmost[j-1];
				rightmost[j-1] = t;
				move++;
			}
		}
		printf("Case #%d: %d\n", testIndex, move);

	}
	return 0;
}