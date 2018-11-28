#pragma warning (disable : 4786)
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <algorithm>
#include <map>
#include <iostream>
#include <sstream>
#include <queue>
#include <cstring>
#include <ctime>
#include <cfloat>

using namespace std;

#define SZ 1005

map<string, string> com;
vector<string> opp;
vector<char> res;

bool oppchk()
{
	int i, j, k;
	char ch = res[res.size() - 1];
	for(i = 0; i < opp.size(); i++)
	{
		if(opp[i][0] == ch)
		{
			for(j = 0; j < res.size() - 1; j++)
			{
				if(res[j] == opp[i][1])
					return true;
			}
		}
		if(opp[i][1] == ch)
		{
			for(j = 0; j < res.size() - 1; j++)
			{
				if(res[j] == opp[i][0])
					return true;
			}
		}
	}
	return false;
}

int main()
{
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);
	int inp, r, kase, n, c, d, k, i, j;
	char buf[SZ];
	string s1, s2;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		com.clear();
		opp.clear();
		res.clear();
		scanf("%d", &c);
		for(i = 0; i < c; i++)
		{
			scanf(" %s", buf);
			s2 = "";
			s2 += buf[2];
			buf[2] = '\0';
			s1 = buf;
			com.insert(make_pair(s1, s2));
			reverse(s1.begin(), s1.end());
			com.insert(make_pair(s1, s2));
		}
		scanf("%d", &d);
		for(i = 0; i < d; i++)
		{
			scanf(" %s", buf);
			s1 = buf;
			opp.push_back(s1);
		}
		scanf("%d", &n);
		scanf(" %s", buf);
		res.push_back(buf[0]);
		for(i = 1; i < n; i++)
		{
			res.push_back(buf[i]);
			if(res.size() > 1)
			{
				s1 = "";
				s1 += res[res.size() - 2];
				s1 += res[res.size() - 1];

				if(com.find(s1) != com.end())
				{
					res.pop_back();
					res.pop_back();
					res.push_back(com[s1][0]);
				}
				if(oppchk())
				{
					res.clear();
				}
			}
		}
		printf("Case #%d: [", kase);
		if(res.size() > 0)
			printf("%c", res[0]);
		for(i = 1; i < res.size(); i++)
		{
			printf(", %c", res[i]);
		}
		printf("]\n");
	}
	return 0;
}

