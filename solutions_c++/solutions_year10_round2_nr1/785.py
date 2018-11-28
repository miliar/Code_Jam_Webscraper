#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int i = 0; i < T; ++i)
	{
		int N,M;
		cin>>N>>M;

		vector<string> vs;
		for(int j = 0; j < N; ++j)
		{
			string tmp;
			cin>>tmp;
			vs.push_back(tmp);
		}

		vector<string> vc;
		for(int j = 0; j < M; ++j)
		{
			string tmp;
			cin>>tmp;
			vc.push_back(tmp);
			vs.push_back(tmp);
		}

		sort(vs.begin(), vs.end());
		sort(vc.begin(), vc.end());

		int ret = 0;
		for(int j = 0; j < vc.size(); ++j)
		{
			vector<string>::iterator it = find(vs.begin(), vs.end(), vc[j]);
			if(it != vs.end())
			{
				if((it+1) != vs.end() && *(it+1)==vc[j])
					continue;

				if(it == vs.begin())
				{
					ret += count(vc[j].begin(), vc[j].end(), '/');
				}
				else
				{
					string s1 = *(it-1);
					string s2 = *it;
					int k = 0;
					for(; k < min(s1.length(), s2.length()); ++k)
						if(s1[k] != s2[k])
							break;
					if(k < s2.length())
						ret += 1 + count(s2.begin()+k+1, s2.end(), '/');
				}
			}
		}

		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}

}