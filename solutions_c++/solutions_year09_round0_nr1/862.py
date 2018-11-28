// alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int L, D, N;
vector<string> dict;

int _tmain(int argc, _TCHAR* argv[])
{
	cin >> L >> D >> N;
	char buf[65536];
	cin.getline(buf, 65536);
	for (int i=0;i<D;i++)
	{
		cin.getline(buf, 65536);
		string s = buf;
		dict.push_back(s);
	}
	vector<string> res;
	for (int i=0;i<N;i++)
	{
		cin.getline(buf, 65536);
		string s = buf;
		vector<int> Let(L, 0);
		int idx = 0;
		int br = 0;
		for (int j=0;j<s.length();j++)
		{
			if (s[j]=='(') 
			{
				br++;
				continue;
			}
			if (s[j]==')') 
			{
				br--;
				idx++;
				continue;
			}
			if (s[j]>='a' && s[j]<='z')
			{
				Let[idx] |= (1<<(s[j]-'a'));
				if (br==0) idx++;
			}
		}

		int cnt = 0;
		for (int j=0;j<D;j++)
		{
			bool bOk = true;
			for (int k=0;k<L;k++)
				if ((Let[k]&(1<<(dict[j][k]-'a')))==0)
				{
					bOk = false;
					break;
				}
			if (bOk) cnt++;
		}
		stringstream ss;
		ss << "Case #" << (i+1) << ": " << cnt;
		res.push_back(ss.str());
	}
	for (int i=0;i<res.size();i++)
		cout << res[i] << endl;

	return 0;
}

