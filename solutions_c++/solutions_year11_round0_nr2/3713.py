#include <string>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <map>

using namespace std;

int t;
int n;



ofstream out("out.txt");

bool Con(string str, char ch)
{
	for(int i = 0;i < str.size();i ++)
	{
		if(str[i] == ch)
			return true;
	}
	return false;
}


int main()
{
	cin >> t;
	int count = 1;
	while(--t >= 0)
	{
		map<string, char> mp;
		map<char, char> op;
		int c,d;
		cin >> c;
		for(int i = 0;i < c;i ++)
		{
			string str;
			cin >> str;
			char ch = str[2];
			str = str.substr(0,2);
			mp[str] = ch;
			reverse(str.begin(), str.end());
			mp[str] = ch;
		}

		cin >> d;
		for(int i = 0;i < d;i ++)
		{
			string str;
			cin >> str;
			op[str[0]] = str[1];
			op[str[1]] = str[0];
		}
		cin >> n;
		string str = "";

		for(int i = 0;i < n;i ++)
		{
			char ch;
			cin >> ch;
			if(str.size() > 0)
			{
				str += ch;
				string temp = "";
				temp += str[str.size() - 2];
				temp += str[str.size() - 1];


				while(temp != "" && mp.count(temp) > 0)
				{
					str = str.substr(0,str.size() - 2);
					str += mp[temp];
					temp = "";
					if(str.size() > 1)
					{
						temp += str[str.size() - 2];
						temp += str[str.size() - 1];
					}
				}

				if(str.size() > 1 && op.count(str[str.size() - 1]) > 0)
				{
					if(Con(str.substr(0, str.size() - 1),op[str[str.size() - 1]]))
						str = "";
				}

			}
			else
				str += ch;
		}

	    string ret = "";
		if(str.size() > 0)
		{
			for(int i = 0;i < str.size() ;i ++)
			{
				if(i > 0)
					ret += ", ";
				ret += str[i];
			}
		}
		ret = "[" + ret + "]";
		
		out <<"Case #" << count ++ << ": " <<  ret << endl;
	}



	return 0;
}