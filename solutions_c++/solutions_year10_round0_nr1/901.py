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
#pragma warning(disable : 4996)

int N, K;

void init()
{
	scanf("%d %d", &N, &K);
}

bool solve()
{
	long n2 = 0x1<<N;
	long k2 = K%n2;
	return (k2==n2-1);
}

int main()
{
//	freopen("..\\A-sample.in","r",stdin);freopen("..\\A.out","w",stdout);
//	freopen("..\\A-small-attempt0.in","r",stdin);freopen("..\\A-small.out","w",stdout);
	freopen("..\\A-large.in","r",stdin);freopen("..\\A-large.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		init();
		if (solve())
			printf("ON\n");
		else
			printf("OFF\n");
		
		fflush(stdout);
	}
	return 0;
}

