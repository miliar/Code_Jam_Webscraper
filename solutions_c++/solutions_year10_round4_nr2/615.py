#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
using namespace std;

int n, N, i, j;
int m[2000], p[2000];

int compute(int l, int dl, int &w)
{
	if(l==n)
	{
		w = m[dl];

		return 0;
	}

	int m1, m2, s;
	s = compute(l+1, dl<<1, m1);
	s += compute(l+1, (dl<<1) + 1, m2);
	
	w = max(m1, m2);

	if(w > l)
		++ s;
	return s;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin >> t;
	for(int ti=1;ti<=t;++ti)
	{
		cin >> n;
		N = 1<<n;

		for(i=0;i<N;++i)
		{
			cin >> m[i];
			m[i] = n - m[i];
		}

		for(i=0;i<N-1;++i)
			cin >> j;

		cout << "Case #" << ti << ": " << compute(0, 0, j) << endl;
	}
	return 0;
}
