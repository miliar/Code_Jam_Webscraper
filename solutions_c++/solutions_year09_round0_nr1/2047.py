// A1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char pattern_name[5500][20];
bool pattern_status[5500];
char test_string[10000];
map<string,string> pattern_map;
string str_solve, str_const;
int tcount, cur_pos;
multimap<char,int> * char2index;
int pattern_len, pattern_num, testcase;
/*
void match(int pos)
{
	int left_pos, right_pos, b_pos;
	b_pos = str_solve.size();
	left_pos = str_const.find_first_of('(', pos);
	right_pos = str_const.find_first_of(')', pos);
	if (left_pos == string::npos || right_pos == string::npos)
	{
		map<string,string>::iterator iter;
		str_solve.append(str_const.substr(pos));
		if ((iter=pattern_map.find(str_solve)) != pattern_map.end())
			tcount++;
		str_solve.erase(b_pos);
	}
	else
	{
		for (int i = left_pos+1; i < right_pos; ++i)
		{
			str_solve.append(str_const.substr(i,1));
			match(right_pos+1);
			str_solve.erase(b_pos);
		}
	}
}
*/
void match(int pos)
{
	int right;
	string str_mid;
	if (pos >= str_const.size())
	{
		for (int i = 0; i < pattern_num; ++i)
		{
			if (pattern_status[i])
				tcount++;
		}
		return;
	}

	if (str_const[pos] == '(')
	{
		right = str_const.find_first_of(')', pos+1);
		str_mid = str_const.substr(pos+1, right-pos-1);
		for (int i = 0; i < pattern_num; ++i)
		{
			if (pattern_status[i])
			{
				if (str_mid.find(pattern_name[i][cur_pos]) == string::npos)
					pattern_status[i] = false;
			}
		}
		cur_pos++;
		match(right+1);
	}
	else
	{
		for (int i = 0; i < pattern_num; ++i)
		{
			if (pattern_status[i])
			{
				if (str_const[pos] != pattern_name[i][cur_pos])
					pattern_status[i] = false;
			}
		}
		cur_pos++;
		match(pos+1);
	}

		
}

int solve()
{
	memset(pattern_status, 1, sizeof(bool)*5500);
	str_solve.clear();
	tcount = 0;
	cur_pos = 0;
	str_const = test_string;
	match(0);
	return tcount;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A1.out","w",stdout);

	scanf("%d %d %d",&pattern_len, &pattern_num, &testcase);
	string map_name;
	for (int p_i = 0; p_i < pattern_num; ++p_i)
	{
		scanf("%s", pattern_name[p_i]);
	}

	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%s", test_string);
		int ret=solve();
		printf("%d\n",ret);
		fflush(stdout);
	}
	return 0;
}

