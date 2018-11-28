#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
using namespace std;

vector<struct Combine> combineRules;
vector<pair<char, char> > opposeRules;

struct Combine
{
	char x;
	char y;
	char c;

	Combine(char xx, char yy, char cc) :
		x(xx), y(yy), c(cc) 
	{
	}
};

int addSean(int x, int y)
{
	int xx[20];
	int yy[20];
	for (int i=0; i<20; i++)
	{
		xx[i] = x % 2;
		yy[i] = y % 2;
		x /= 2;
		y /= 2;
	}

	int zz[20];
	for (int i=0; i<20; i++)
	{
		zz[i] = xx[i] + yy[i];
		if (zz[i] == 2)
			zz[i] = 0;
	}

	int res = 0;
	for (int i=19; i>=0; i--)
	{
		res <<= 1;
		res += zz[i];
	}

	return res;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t=0; t<T; t++)
	{
		//TODO: implement your algorithm here
		int n;
		cin >> n;
		vector<int> v;
		for (int i=0; i<n; i++)
		{
			int d;
			cin >> d;
			v.push_back(d);
		}

		int checksum = 0;
		for (int i=0; i<v.size(); i++)
		{
			checksum = addSean(checksum, v[i]);
		}
		if (checksum != 0)
		{
			printf("Case #%d: NO\n", t+1);
			continue;
		}

		sort(v.begin(), v.end());
		int sum = 0;
		for (int i=1; i<v.size(); i++)
		{
			sum += v[i];
		}
		
		printf("Case #%d: %d\n", t+1, sum);
		
	}
}