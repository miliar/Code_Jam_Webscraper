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

int max(int a, int b)
{
	if(a > b)
		return a;
	return b;
}

int min(int a, int b)
{
	if(a < b)
		return a;
	return b;
}


bool check(int a, int b)
{
	if(a == b)
	{
		return false;
	}

	if(a == 1 || b == 1)
	{
		return true;
	}

	if(max(a, b) - min(a, b) == 1)
	{
		return false;
	}
	
	if(max(a, b) - min(a, b) < min(a,b))
	{
		return(!check(min(a, b), max(a, b) - min(a, b)));
	}
	return true;
}

int main()
{
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int inp, kase, i, j, k;
	int a1, a2, b1, b2, cnt;
	scanf("%d", &inp);
	
	for(kase = 1; kase <= inp; kase++)
	{
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
		cnt = 0;
		for(i = a1; i <= a2; i++)
		{
			for(j = b1; j <= b2; j++)
			{
				if(check(i, j))
				{
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n", kase, cnt);
	}
	
	return 0;

}
