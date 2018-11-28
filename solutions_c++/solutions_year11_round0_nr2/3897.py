#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int j = 0; j < T; ++j)
	{
		int C;
		cin>>C;
		map<string, char> comb;
		for(int i = 0; i < C; ++i)
		{
			string tmp;
			cin>>tmp;
			string tmp1 = tmp[1] + tmp.substr(0,1);
			
			comb.insert(make_pair(tmp.substr(0,2), tmp[2]));
			comb.insert(make_pair(tmp1, tmp[2]));
		}

		int D;
		cin>>D;
		map<char, char> oppo;
		for(int i = 0; i < D; ++i)
		{
			string tmp;
			cin>>tmp;

			oppo.insert(make_pair(tmp[0], tmp[1]));
			oppo.insert(make_pair(tmp[1], tmp[0]));
		}

		int N;
		cin>>N;
		string s;
		cin>>s;
		string ret;
		for(int i = 0; i < N; ++i)
		{
			// check comb
			if(ret.length() >= 1)
			{
				string tail = ret.substr(ret.length()-1) + s[i];
				map<string, char>::iterator it = comb.find(tail);
				if(it != comb.end())
				{
					ret = ret.substr(0, ret.length()-1);
					ret.push_back(it->second);
				}
				else
					ret.push_back(s[i]);
			}
			else
				ret.push_back(s[i]);

			// check oppose
			if(ret.length() >= 1)
			{
				char back = ret[ret.length()-1];
				map<char,char>::iterator it = oppo.find(back);
				if(it != oppo.end())
				{
					int pos = ret.find(it->second);
					if(pos != string::npos)
					//	ret.erase(pos);
						ret.clear();
				}
			}
		}

		cout<<"Case #"<<j+1<<": "<<"[";
		for(int i = 0; i < ret.length(); ++i)
			if(i != ret.length()-1)
				cout<<ret[i]<<", ";
			else
				cout<<ret[i];
		cout<<"]"<<endl;
	}

	return 0;
}