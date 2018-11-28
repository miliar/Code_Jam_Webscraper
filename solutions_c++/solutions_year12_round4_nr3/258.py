#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <cstring>
#include <set>
#include <climits>
#include <ctime>
#include <cstdlib>

using namespace std;

#define mp make_pair
#define F first
#define S second

int num[10];
int lol[10];
int n;

int prod(int a[2], int b[2])
{
	return a[0]*b[1]-a[1]*b[0];
}

bool check()
{
	for (int i = 0; i < n-1; ++i)
	{
		for (int j = i+1; j < num[i]; ++j)
		{
			int a[2] = {num[i]-i, lol[num[i]]-lol[i]};
			int b[2] = {j-num[i], lol[j]-lol[num[i]]};
			if (prod(a, b) >= 0) return false;
		}
		for (int j = num[i]+1; j < n; ++j)
		{
			int a[2] = {num[i]-i, lol[num[i]]-lol[i]};
			int b[2] = {j-num[i], lol[j]-lol[num[i]]};
			if (prod(a, b) > 0) return false;
		}
	}
	return true;
}

int main()
{
	int t;
	scanf("%d", &t);
	//srand(time(NULL));
	
	for (int q = 1; q<= t; ++q)
	{
		printf("Case #%d:", q);
		scanf("%d", &n);
		for (int i = 0; i < n-1; ++i)
			scanf("%d", &num[i]);
		for (int i = 0; i < n-1; ++i)
			num[i]--;
		
		bool good = 0;
		for (int i = 0; i < 100000000 && !good; ++i)
		{
			for (int j = 0; j < n; ++j)
				lol[j] = rand()%10000+1;
			good = check();
			if (good)
			{
				//printf("yey\n");
			}
		}
		
		if (good)
		{
			for (int i = 0; i < n; ++i)
				printf(" %d", lol[i]);
			printf("\n");
		}
		else
		{
			printf(" Impossible\n");
		}
	}
	
	return 0;
}

