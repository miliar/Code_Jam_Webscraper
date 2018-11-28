#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int mabs(int num)
{
	return num > 0? num: -num;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	//scanf("%d", &t);
	cin >> t;
	for(int test = 1; test <= t; test++)
	{
		int n, p;
		char c;
		//scanf("%d", &n);
		cin >> n;
		vector< pair<char, int> > v;
		for(int i = 0; i < n; i++)
		{
			//scanf("%c%d", &c, &p);
			cin >> c >> p;
			v.push_back(make_pair(c, p));
		}
		int curo = 1, curb = 1;
		int add = 0;
		int moveso = 0, movesb = 0;
		int total = 0;
		for(int i = 0; i < (int)v.size(); i++)
		{
			pair<char, int> cur = v[i];
			if(cur.first == 'O')
			{
				add = max(0, mabs(cur.second - curo) - movesb) + 1;
				total += add;
				curo = cur.second;
				moveso += add;
				movesb = 0;
			}
			if(cur.first == 'B')
			{
				add = max(0, mabs(cur.second - curb) - moveso) + 1;
				total += add;
				curb = cur.second;
				movesb += add;
				moveso = 0;
			}
		}
		printf("Case #%d: %d\n", test, total);
	}
	return 0;
}