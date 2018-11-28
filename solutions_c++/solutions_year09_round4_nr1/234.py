#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 40;

int cnt = 0;
int N;
int maxc[MAXN];
int tmp[MAXN];

void read()
{
	cin >> N;
	for(int i=0; i<N; i++)
	{
		string s;
		cin >> s;
		maxc[i] = 0;
		for(int j=0; j<N; j++)
			if (s[j] == '1')
				maxc[i] = j;
	}
}

bool feasible(int r)
{
	memcpy(tmp, maxc, sizeof(int)*(r+1));
	sort(tmp, tmp+r+1);
	for(int i=0; i<=r; i++)
		if (tmp[i] > i)
			return false;
	return true;
}

void solve()
{
	cnt = 0;
	for(int r=N-1; r>=0; r--)
	{
		for(int c=r; c>=0; c--)
		{
			for(int i=c; i<r; i++)
				swap(maxc[i], maxc[i+1]);
			if (feasible(r-1))
				break;
			cnt++;
			for(int i=r; i>c; i--)
				swap(maxc[i], maxc[i-1]);
		}
	}
}

int main()
{
	int T;
	cin >> T;
	for(int ic=0; ic<T; ic++)
	{
		read();
		solve();
		printf("Case #%d: %d\n", ic+1, cnt);
	}
}

