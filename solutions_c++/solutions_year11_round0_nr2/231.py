#include <iostream>
#include <map>
#include <set>
#include <string>
#include <cstring>

using namespace std;


int main()
{
	int T;
	cin >> T;
	int C,D,N;
	string s;
	for(int i=1;i<=T;i++)
	{
		map<string, char> cMap;
		cin >> C;
		set<string> opp;
		for(int j=0;j<C;j++)
		{
			cin >> s;
			cMap[s.substr(0,2)] = s[2];
			swap(s[0],s[1]);
			cMap[s.substr(0,2)] = s[2];
		}
		cin >> D;
		for(int j=0;j<D;j++)
		{
			cin >> s;
			opp.insert(s);
			swap(s[0],s[1]);
			opp.insert(s);
		}
		cin >> N;
		cin >> s;
		string ret;
		for(int j=0;j<N;j++)
		{
			ret += s[j];
			if((j-1) >= 0)
			{
				string temp;
				temp += ret[ret.size()-2];
				temp += ret[ret.size()-1];
				if(cMap.find(temp) != cMap.end())
				{
					ret = ret.substr(0, ret.size()-2) + cMap[temp];
				}
				else
				{
					bool found = false;
					for(int k=0;k<ret.size()-1;k++)
					{
						string temp1;
						temp1 += ret[k];
						temp1 += ret[ret.size()-1];
						if(opp.find(temp1) != opp.end())
						{
							found = true;
							break;
						}
					}
					if(found)
					{
						ret = "";
					}
				}
			}
		}
		cout << "Case #" << i << ": [" ;
		string temp;
		for(int j=0;j<ret.size();j++)
		{
			temp += ret[j];
			if(j != (ret.size()-1))
			{
				temp += ", ";
			}
		}
		temp += "]";
		cout << temp << endl;
	}
}
