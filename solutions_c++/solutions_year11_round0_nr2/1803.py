#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	map < string, string > com;
	set < string > opp;
	while (T--)
	{
		string res = "";
		printf("Case #%d: ", ++tc);
		com.clear();
		opp.clear();
		int temp;
		char str[111];
		scanf("%d", &temp);
		while (temp--)
		{
			scanf("%s", str);
			com[string(str).substr(0, 2)] = string(str).substr(2, 1);
		}
		scanf("%d", &temp);
		while (temp--)
		{
			scanf("%s", str);
			opp.insert(string(str));
		}
		scanf("%d", &temp);
		scanf("%s", str);
		for (int i = 0; i < temp; ++i)
		{
			res.append(1, str[i]);
			while (true)
			{
				if (res.length() >= 2)
				{
				    string last = "12";
			    	last[0] = res[res.length() - 1];
				    last[1] = res[res.length() - 2];
					if (com.find(last) != com.end())
					{
						res = res.substr(0, res.length() - 2);
						res.append(com[last]);
						continue;
					}
					last[1] = res[res.length() - 1];
				    last[0] = res[res.length() - 2];
					if (com.find(last) != com.end())
					{
						res = res.substr(0, res.length() - 2);
						res.append(com[last]);
						continue;
					}
					int size = res.size();
					int flag = 0;
				    for (int j = 0; j < size; ++j)
					{
						for (int k = j + 1; k < size; ++k)
						{
							if (opp.find(string(1, res[k]) + string(1, res[j])) != opp.end() ||
								opp.find(string(1, res[j]) + string(1, res[k])) != opp.end())
							{
								flag = 1;
								j = size;
								break;
							}
						}
					}
					if (flag == 1)
					{
						res.clear();
					}
					break;
				}
				else
				{
					break;
				}
			}
		}
		printf("[");
		if (res.size() > 0)
		{
			printf("%c", res[0]);
			for (int i = 1, j = res.size(); i < j; ++i)
			{
				printf(", %c", res[i]);
			}
		}
		printf("]\n");
	}
	return 0;
}
