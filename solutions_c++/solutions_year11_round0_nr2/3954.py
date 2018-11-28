#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
using namespace std;


bool isclear(string str, const set<pair<char, char> >& rev)
{
	int n = str.size();
	for(int j = 0; j < n - 1; j++)
	{
		if(rev.find(make_pair(str[j], str[n - 1])) != rev.end())
			return true;
	}
	return false;
}

int main()
{
	int nt, C, D, N;
	char input[107];
	memset(input, 0, sizeof(input));
	scanf("%d", &nt);
	for(int i = 1; i <= nt; i++)
	{
		map<pair<char, char>, char> dict;
		set<pair<char, char> > rev;
		scanf("%d", &C);
		for(int j = 0; j < C; j++)
		{
			scanf("%s", input);
			dict.insert(make_pair(make_pair(input[0], input[1]), input[2]));
			dict.insert(make_pair(make_pair(input[1], input[0]), input[2]));
		}
		scanf("%d", &D);
		for(int j = 0; j < D; j++)
		{
			scanf("%s", input);
			rev.insert(make_pair(input[0], input[1]));
			rev.insert(make_pair(input[1], input[0]));
		}
		scanf("%d", &N);
		scanf("%s", input);
		string ans;
		ans += input[0];
		map<pair<char, char>, char>::iterator it;
		for(int j = 1; j < N; j++)
		{
			if((it = dict.find(make_pair(ans[ans.size() - 1], input[j]))) != dict.end())
			{
				ans[ans.size() - 1] = it->second;
			}
			else if((it = dict.find(make_pair(input[j], ans[ans.size() - 1]))) != dict.end())
			{
				ans[ans.size() - 1] = it->second;
			}
			else if(isclear(ans + input[j], rev))
			{
				ans = "";
			}
			else
				ans += input[j];
		}
		printf("Case #%d: [", i);
		for(int j = 0; j < ans.size(); j++)
		{
			printf("%c", ans[j]);
			if(j != ans.size() - 1)
				printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
