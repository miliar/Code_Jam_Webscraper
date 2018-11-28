#define _CRT_SECURE_NO_WARNINGS

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


#define ASSERT(X) {if (!(X)) {printf("\n assertion failed at line %d\n",__LINE__);exit(0);}}

const int maxn=1000+5;

int n;
double length,S,R,leftTime;
double L[maxn],P[maxn];

inline int GetRecycledNumber(int val, int b)
{
	int r = 0;
	char buf[8];
	itoa(val, buf, 10);
	for (int l = 1; l < strlen(buf); l++)
	{
		char last = buf[strlen(buf)-1];
		for (int i = strlen(buf) -1; i>=1; i--)
		{
			buf[i] = buf[i-1];
		}
		buf[0] = last;
		if (buf[0] != '0')
		{
			int ans = atoi(buf);
			if ((ans > val) && (ans <= b))
			{
				r++;
				//printf("%d - %d\n", val, ans);
			}
		}
	}
	return r;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		printf("Case #%d: ",case_id);
		int a, b;
		scanf("%d %d",&a,&b);
	
		long int r = 0;
		for (int i = a; i <= b; i++)
		{
			r += GetRecycledNumber(i, b);
		}

		printf("%d\n", r);
		fflush(stdout);
	}
	return 0;
}