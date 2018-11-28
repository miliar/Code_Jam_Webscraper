#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 1505;

int a[MAX];
int p;
int len;

int num()
{
	int res = 0;
	for(int i = 0; i < len; i++)
		if(a[i])  res++;
	return res;
}

int go()
{
	int per = len;
	int res = 0;
	while(num())
	{
		int num = len / per;
		for(int i = 0; i < num; i++)
		{
			int flag = 0;
			for(int j = i * per; j < (i + 1) * per; j++)
			{
				if(a[j])
				{
					a[j]--;
					flag = 1;
				}
			}
			if(flag)  res++;
		}
		per /= 2;
	}
	return res;
}

int main()
{
	freopen("d:\\B-small-attempt0.in", "r", stdin);
	freopen("d:\\B-small-attempt0.out", "w", stdout);

	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &p);
		len = 1 << p;
		for(int i = 0; i < (1 << p); i++) 
		{
			scanf("%d", &a[i]);
			a[i] = p - a[i];
		}
		for(int i = 0; i < p; i++)
		{
			int t;
			int up = 1 << (p - 1 - i);
			for(int j = 0; j < up; j++)  scanf("%d", &t);
		}
		printf("Case #%d: %d\n", ++c, go());
	}
}