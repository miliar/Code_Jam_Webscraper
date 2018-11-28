#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int L,D,N;
vector<string> Dic;
vector<set<char> > pat;

int main(void)
{
	cin >> L >> D >> N;
	for(int i=0;i<D;i++)
	{
		string str;
		cin >> str;
		Dic.push_back(str);
	}

	for(int ii=0;ii<N;ii++)
	{
		pat.clear();
		pat.resize(L);
		string str;
		cin >> str;
		int pos = 0;
		for(int i=0;i<(int)str.size();i++, pos++)
		{
			if(str[i] == '(')
			{
				i++;
				while(str[i] != ')')
				{
					pat[pos].insert(str[i]);
					i++;
				}
			}
			else
			{
				pat[pos].insert(str[i]);
			}
		}

		int ret = 0;

		for(int i=0;i<D;i++)
		{
			bool nofound = false;
			for(int j=0;j<(int)Dic[i].size();j++)
			{
				if(pat[j].count(Dic[i][j]) == 0)
				{
					nofound = true;
					break;
				}
			}
			if(!nofound) ret++;
		}

		printf("Case #%d: %d\n",ii+1,ret);
	}
}
