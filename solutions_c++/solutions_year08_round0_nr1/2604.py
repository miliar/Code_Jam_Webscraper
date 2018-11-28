#include <cstdio>
#include <string>

int engineIndex[1000];
int engines, queries;

int GetSwitches(int queryIndex)
{
	int newQueryIndex = 0;

	for (int i = 0; i < engines; i++)
	{
		int j;
		for (j = queryIndex; j < queries && engineIndex[j] != i; j++);

		if (j >= queries)
			return 0;
		if (newQueryIndex < j)
			newQueryIndex = j;
	}

	return GetSwitches(newQueryIndex) + 1;
}

int main(int argc, char* argv[])
{
	int count;
	char engine[100][101];

	scanf("%d\n", &count);
	for (int i = 0; i < count; i++)
	{
		scanf("%d\n", &engines);
		for (int j = 0; j < engines; j++)
		{
			scanf("%100[a-zA-Z 0-9]s\n", engine[j]);
			getchar();
		}

		scanf("%d\n", &queries);
		for (int j = 0; j < queries; j++)
		{
			char query[101];
			scanf("%100[a-zA-Z 0-9]s\n", query);
			for (int x = 0; x < engines; x++)
				if (strcmpi(query, engine[x]) == 0)
				{
					engineIndex[j] = x;
					break;
				}
			getchar();
		}

		printf("Case #%d: %d\n", i + 1, GetSwitches(0));
	}

	return 0;
}
