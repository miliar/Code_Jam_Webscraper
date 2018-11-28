#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>

#define all(x) (x).begin(),(x).end()

using namespace std;

int dir(int x)
{
	if (x > 0) return 1;
	if (x < 0) return -1;
	return 0;
}

int n;

void solve(int _case)
{
	scanf("%d",&n);
	vector <int> q1;
	vector <int> q2;
	vector <int> t1;
	vector <int> t2;
	for (int i = 0; i < n; i ++)
	{
		char c; int e;
		scanf(" %c %d",&c,&e);
		if (c == 'O')
		{
			q1.push_back(e);
			t1.push_back(i);
		}
		else
		{
			q2.push_back(e);
			t2.push_back(i);
		}
	}
	reverse(all(q1));
	reverse(all(t1));
	reverse(all(q2));
	reverse(all(t2));
	int cur1 = 1;
	int cur2 = 1;
	int time = 0;
	int cur = 0;
	while (q1.size() || q2.size())
	{
		time ++;
		int dcur = 0;
		if (q1.size())
		{
			if (q1.back() == cur1 && t1.back() == cur)
			{
				q1.pop_back();
				t1.pop_back();
				dcur = 1;
			}
			else
				cur1 += dir(q1.back() - cur1);
		}
		if (q2.size())
		{
			if (q2.back() == cur2 && t2.back() == cur)
			{
				t2.pop_back();
				q2.pop_back();
				dcur = 1;
			}
			else
				cur2 += dir(q2.back() - cur2);
		}
		cur += dcur;
	}
	printf("Case #%d: ",_case);
	printf("%d\n",time);
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; i ++)
		solve(1+i);
	return 0;
}
