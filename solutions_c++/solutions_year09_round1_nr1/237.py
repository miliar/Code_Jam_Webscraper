// A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

char buf[1000];
map<int, int> mp[100];

int main()
{
	void solve(int);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin>>t;
	getchar();
	for(int i = 0;i<t;i++)
	{
		solve(i + 1);
	}

	return 0;
}

void solve(int cas)
{
	int judge(int, int);
	vector<int> vec;
	gets(buf);
	int tmp ;
	istringstream iss(buf);
	while(iss >> tmp)
	{
		vec.push_back(tmp);
	}

	tmp = 2;
	while(1)
	{
		int i;
		for(i = 0;i<(int)vec.size();i++)
		{
			mp[vec[i]].clear();
			if(judge(tmp, vec[i]) == 0)
				break;
		}
		if(i == (int)vec.size())
		{
			printf("Case #%d: %d\n",cas, tmp);
			return;
		}
		tmp ++;
	}
}

int judge(int num, int base)
{
	//cout<<"in "<<num<<" "<<base<<endl;
	if(num == 1)
		return 1;
	if(mp[base][num] > 0)
		return 0;
	mp[base][num] = 1;
	int ans = 0;
	int remain;
	for(int tmp = num;tmp != 0;)
	{
		remain = tmp % base;
		ans += remain * remain;
		tmp /= base;
	}
	return judge(ans, base);
}
