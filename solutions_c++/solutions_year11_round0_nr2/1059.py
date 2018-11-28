#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
	int T;
	freopen("B-large.in", "rb", stdin);
	freopen("B-large.out", "wb", stdout);

	scanf("%d", &T);

	for(int t = 0; t < T; t++)
	{
		char buffer[1024];
		map< pair<char, char>, char > combine;
		vector< pair<char, char> > opposed;
		
		int C, D, N;
		scanf("%d", &C);
		for(int c = 0; c < C; c++)
		{
			scanf("%s", buffer);
			combine[pair<char, char>(buffer[0], buffer[1])] = buffer[2];
			combine[pair<char, char>(buffer[1], buffer[0])] = buffer[2];
		}

		scanf("%d", &D);
		for(int d = 0; d < D; d++)
		{
			scanf("%s", buffer);
			opposed.push_back(pair<char, char>(buffer[0], buffer[1]));
			opposed.push_back(pair<char, char>(buffer[1], buffer[0]));
		}
		sort(opposed.begin(), opposed.end());

		scanf("%d %s", &N, buffer);

		string list;
		for(int i = 0; i < N; ++i)
		{
			if(list.size() == 0)
			{
				list += buffer[i];
				continue;
			}
			else if(combine.find(pair<char, char>(list[list.size() - 1], buffer[i])) != combine.end())
			{
				list[list.size() - 1] = combine[pair<char, char>(list[list.size() - 1], buffer[i])];
			}
			else
			{
				int j;
				for(j = 0; j < list.size(); j++)
				{
					if(binary_search(opposed.begin(), opposed.end(), pair<char, char>(list[j], buffer[i])))
					{
						list = "";
						break;
					}
				}

				if(list.size() > 0)
				{
					list += buffer[i];
				}
			}
		}

		printf("Case #%d: ", t + 1);
		if(list.size() == 0)
		{
			printf("[]\n");
		}
		else
		{
			printf("[%c", list[0]);
			for(int i = 1; i < list.size(); i++)
			{
				printf(", %c", list[i]);
			}
			printf("]\n");
		}
	}

	return 0;
}