#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <cctype>
#include <set>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

char buf[128];
int C, D, N, T;
vector<string>	cb;
string op[128];

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		cb.clear();
		for(int i = 0; i < 128; i++)
			op[i].clear();
		scanf("%d", &C);
		for(int i = 0; i < C; i++)
		{
			scanf("%s", buf);
			if(buf[0] > buf[1])		swap(buf[0], buf[1]);
			cb.push_back(buf);
		}
		scanf("%d", &D);
		for(int i = 0; i < D; i++)
		{
			scanf("%s", buf);
			op[buf[0]].push_back(buf[1]);
			op[buf[1]].push_back(buf[0]);
		}
		scanf("%d", &N);
		scanf("%s", buf);
		string ans;
		for(int i = 0; i < N; i++)
		{
			ans += buf[i];
			while(true)
			{
				bool f1 = false;
				bool f2 = false;
				if(ans.size() > 1)
				{
					char a = ans[ans.size()-1];
					char b = ans[ans.size()-2];
					if(a > b)	swap(a, b);
					for(int j = 0; j < cb.size(); j++)
					{
						if(cb[j][0] == a && cb[j][1] == b)
						{
							ans.pop_back();
							ans.pop_back();
							ans.push_back(cb[j][2]);
							f1 = true;
							break;
						}
					}
				}
				if(f1)	continue;
				if(ans.size() > 1)
				{
					char k = ans.back();
					for(int j = 0; j < ans.size()-1; j++)
					{
						if(find(op[k].begin(), op[k].end(), ans[j]) != op[k].end())
						{
							ans.clear();
							break;
						}
					}
				}
				break;
			}
		}
		printf("Case #%d: [", t);
		for(int i = 0; i < ans.size(); i++)
		{
			if(i != 0)	printf(", ");
			printf("%c", ans[i]);
		}
		printf("]\n");
	}
	return 0;
}