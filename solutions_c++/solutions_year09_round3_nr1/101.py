#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<iostream>
#include<sstream>
#include<fstream>
#include<cmath>

using namespace std;

typedef long long int64;
char buf[100];
map<char, int> dic;

void seed()
{
	int n = strlen(buf);
	dic.insert(make_pair(buf[0], 1));
	int cnter = 0;

	for(int i=1; i<n; ++i)
	{
		char ch = buf[i];
		if(dic.find(ch) == dic.end())
		{
			dic.insert(make_pair(ch, cnter));
			if(cnter == 0) cnter = 2;
			else cnter ++;
		}
	}
}
long long calc()
{
//	if(strlen(buf)==1)
//		return 0;

	int base = dic.size();
	if(base == 1)
		base = 2;

	int64 res = 0;
	for(int i=0; i<strlen(buf); ++i)
	{
		res = res * base + dic[buf[i]];
	}
	return res;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		dic.clear();
		scanf("%s", buf);
		seed();
		int64 res = calc();
		printf("Case #%d: %lld\n", c, res);
	}

	return 0;
}
