// Tongue.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <assert.h>
#include <algorithm>
using namespace std;

char map[26];

void run()
{
	string inStr;
	//cin >> inStr;
	char buf[500];
	cin.getline(buf, 500);
	inStr = buf;
	string outStr(inStr);
	for (int i=0; i<inStr.size(); i++)
	{
		char val = inStr[i];
		if (inStr[i]>='a' && inStr[i] <= 'z')
		{
			char mapval = map[val-'a'];
			outStr[i] = mapval;
		}
	}
	cout << outStr << endl;;
}
void calmap(string str1, string str2)
{
	for (int i=0; i<str1.size(); i++)
	{
		char src = str1[i];
		char dst = str2[i];
		if (src>='a' && src<='z')
		{
			assert(map[src-'a'] == '*'|| map[src-'a'] == dst);
			map[src-'a'] = dst;
		}
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	for (int i=0; i<26; i++)
	{
		map[i] = '*';
	}

	string str1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string str2 = "our language is impossible to understand";
	string str3 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string str4 = "there are twenty six factorial possibilities";
	string str5 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string str6 = "so it is okay if you want to just give up";

	calmap(str1, str2);
	calmap(str3, str4);
	calmap(str5, str6);

	for (int i=0; i<26; i++)
	{
		char val = 'a' + i;
		cout << val << " ";
	}

	cout << endl;
	map[25] = 'q';
	map['q'-'a'] = 'z';

	for (int i=0; i<26; i++)
	{
		cout << map[i] << " ";
	}
	string sortmap(map);
	sort(sortmap.begin(), sortmap.end());
	cout << endl;
	for (int i=0; i<26; i++)
	{
		cout << sortmap[i] << " ";
	}
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);
	
	int T;
	cin >> T;
	char buf[100];
	cin.getline(buf, 100);


	for (int i=1; i<=T; i++)
	{
		cout << "Case #" << i << ": ";
		run();
	}
	return 0;
}

