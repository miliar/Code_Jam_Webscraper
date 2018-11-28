#include <iostream>
#include <set>
#include <string>

using namespace std;

int		N, S, Q;
set<string>	engSet, usedSet;
char		line[1000];
string		query;

int main()
{
	scanf("%d\n", &N);
	for (int now = 1; now <= N; ++now)
	{
		engSet.clear(); usedSet.clear();
		int answer = 0;

		scanf("%d\n", &S);
		for (int i = 0; i < S; ++i)
		{
			gets(line);
			engSet.insert( string(line) );
		}
		scanf("%d\n", &Q);
		for (int i = 0; i < Q; ++i)
		{
			gets(line);
			query = string(line);

			if (engSet.count(query))
			{
				usedSet.insert(query);
				if (usedSet.size() == S)
				{
					usedSet.clear();
					usedSet.insert(query);
					++answer;
				}
			}
		}

		printf("Case #%d: %d\n", now, answer);
	}
}
