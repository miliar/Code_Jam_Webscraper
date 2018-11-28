// RecycledNumbers.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <vector>
#include <string>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <list>
using namespace std;

int v[2000000];

string parse(int val)
{
	char buf[20];
	sprintf(buf, "%d", val);
	return buf;
}

void run()
{
	string a, b;
	int A, B;
	cin >> A >> B;
	
	memset(v, 0, sizeof(v));

	int num = 0;

	a = parse(A); b = parse(B);

	string str = a;
	for (int i=A; i<=B; i++)
	{
		str = parse(i);
		string tmp(str);
		list<string> buff;
		for (int j=1; j<a.size(); j++)
		{
			rotate_copy(str.begin(), str.begin()+j, str.end(), tmp.begin());
			//if(tmp == str)continue;
			if (tmp > str && tmp<= b)
			{
				buff.push_back(tmp);
			}
		}
		buff.unique();
		num += buff.size();

	}
	cout << num << endl;
}

int main()
{
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);

	int T;
	cin >> T;


	for (int i=1; i<=T; i++)
	{
		cout << "Case #" << i << ": ";
		run();
	}
	return 0;
}
