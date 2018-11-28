// A3.cpp : Defines the entry point for the console application.
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

int testcase;
const char * welcome = "welcome to code jam";
char input_str[512];


int match(char * input_str, const char * search_str)
{
	char single_str[2];
	char * pos;
	int count(0);
	if (search_str[0] == '\0')
		return 1;
	else if (input_str[0] == '\0')
		return 0;

	single_str[0] = search_str[0];
	single_str[1] = '\0';
	while((pos=strstr(input_str, single_str)) != NULL)
	{
		count += match(pos+1, search_str+1);
		input_str = pos+1;
	}
	return count;
}

int solve()
{
	int ret = match(input_str, welcome);
	return ret;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("..\\C-small-attempt0.in","r",stdin);
	freopen("..\\B1.out","w",stdout);
	scanf("%d\n", &testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		cin.getline(input_str, 511);
		int ret = solve();
		printf("Case #%d: ",caseId);
		printf("%04d\n", ret);
		fflush(stdout);
	}
	return 0;
}


