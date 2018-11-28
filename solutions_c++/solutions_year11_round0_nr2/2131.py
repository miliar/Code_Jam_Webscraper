#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main()
{
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; k++)
	{
		int c, d, n;
		string str;
		map<string,char> comb;
		vector<int> opp[200];
		scanf("%d", &c);
		while(c--)
		{
			char buf[5];
			scanf("%s", buf);
			string tmp="";
			tmp += buf[0];
			tmp += buf[1];
			comb[tmp] = buf[2];
			reverse(tmp.begin(), tmp.end());
			comb[tmp] = buf[2];
		}
		scanf("%d", &d);
		while(d--)
		{
			char buf[5];
			scanf("%s", buf);
			opp[buf[0]].push_back(buf[1]);
			opp[buf[1]].push_back(buf[0]);
		}
		scanf("%d", &n);
		char buf[200];
		vector<int> count(200,0);
		scanf("%s", buf);
		for(int i = 0; i < n; i++)
		{
			str+=buf[i];
			count[str[str.size()-1]]++;
			bool q = true;
			while(str.size()>1 && q)
			{
				string tmp="";
				tmp += str[str.size()-2];
				tmp += str[str.size()-1];
				//printf("  %s\n", tmp.c_str());
				if(comb.find(tmp) != comb.end())
				{
					count[str[str.size()-1]]--;
					str.erase(str.size()-1,1);
					count[str[str.size()-1]]--;
					str.erase(str.size()-1,1);
					str += comb[tmp];
				}
				else
					q=0;
				
				for(int j = 0; j < opp[str[str.size()-1]].size(); j++)
					if(count[opp[str[str.size()-1]][j]])
					{
						str = "";
						fill(count.begin(),count.end(),0);
						break;
					}
			}
			//printf("%s\n", str.c_str());
		}
		//printf("%d\n", str.size());
		printf("Case #%d: [", k);
		for(int i = 0; i < (int)str.size()-1; i++)
			printf("%c, ", str[i]);
		if(str.size())
			printf("%c]\n", str[str.size()-1]);
		else
			printf("]\n");
		
	}
}


