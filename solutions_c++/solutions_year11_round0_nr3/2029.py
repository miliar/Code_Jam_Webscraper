#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long lint;
typedef vector<int> vi;
typedef pair<int, int> pii;
const int Inf = 0x7fffffff;

int Solution(int test)
{
	int n;
	cin >> n;
	int s = 0, m = Inf;
	vi cnt(20);
	for(int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		m = min(x, m);
		s += x;
		int j = 0;
		while(x)
		{
			if(x & 1)
				cnt[j]++;
			x >>= 1;
			++j;
		}
	}
	bool flag = true;
	for(int i = 0; i < 20; ++i)
		if(cnt[i] & 1)
		{
			flag = false;
			break;
		}
	cout << "Case #" << test << ": ";
	if(flag)
		cout << s - m << endl;
	else
		cout << "NO" << endl;
	return 0;
}

#define debug

int main()
{
#ifdef debug
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
		Solution(i);
#ifdef debug
	system("@pause");
#endif
	return 0;
}
