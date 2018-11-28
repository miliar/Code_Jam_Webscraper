// jam2010_1_1.cpp : Defines the entry point for the console application.
//
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

bool snap(vector<bool>& snapper)
{
	int count=0;
	for(count=0; count<snapper.size(); ++count)
	{
		if(snapper[count] == false)
			break;
	}

	for(int i=0; i<count+1; ++i)
	{
		if(i==snapper.size())
			break;
		snapper[i] = !snapper[i];
	}
	return true;
}

bool isAllSnapperOn(vector<bool>& snapper)
{
	for(int i=0; i<snapper.size(); ++i)
	{
		if (snapper[i] == false)
			return false;
	}
	return true;
}

int main()
{
	freopen("../A-small-attempt0.in","r",stdin);
	freopen("../A-small-attempt0.out","w",stdout);

	int testCase = 0;
	scanf("%d",&testCase);
	for (int testId=1; testId <= testCase; ++testId)
	{
		int result = 0;

		int N = 0;
		int K = 0;
		scanf("%d %d",&N, &K);
		//printf("%d %d\n",N, K);

		vector<bool> snapper;
		for(int i=0; i<N; ++i)
		{
			snapper.push_back(false);
		}

		for(int i=0; i<K; ++i)
		{
			if(i==0)
			{
				snapper[0] = true;
			}
			else
			{
				snap(snapper);
			}
		}

		printf("Case #%d: %s\n", testId, (isAllSnapperOn(snapper))?"ON":"OFF");
	}

	return 0;
}

