#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int T;
int N;
vector<char> a;
vector<int> p;

int solve()
{
	int ro = 1, rb = 1;
	int to = 0, tb = 0;
	int ret = 0;
	for (int i=0; i<N; i++)
	{
		for (int j=i; j<N; j++)
			if (a[j] == 'O')
			{
				to = p[j];
				break;
			}
		for (int j=i; j<N; j++)
			if (a[j] == 'B')
			{
				tb = p[j];
				break;
			}
		if (a[i] == 'O')
		{
			while (ro != to)
			{
				if (to > ro) ro ++;
				else if (to < ro) ro --;
				if (tb > rb) rb++;
				else if (tb < rb) rb--;
				ret++;
			}
			if (tb > rb) rb++;
			else if (tb < rb) rb--;
			ret++;
		}
		else
		{
			while (rb != tb)
			{
				if (to > ro) ro ++;
				else if (to < ro) ro --;
				if (tb > rb) rb++;
				else if (tb < rb) rb--;
				ret++;
			}
			if (to > ro) ro ++;
			else if (to < ro) ro --;
			ret++;
		}
	}
	return ret;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		cin >> N;
		char c;
		int pos;
		p.clear();
		a.clear();
		for (int j=0; j<N; j++)
		{
			cin >> c;
			a.push_back(c);
			cin >> pos;
			p.push_back(pos);
		}
		printf("Case #%d: %d\n", i, solve());
	}
}