#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <algorithm>
#include <functional>
#include <queue>
#include <map>
#include <climits>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <set>

using namespace std;

typedef unsigned long long LL;
typedef pair<int, int> PII;
typedef pair<int, LL> PIL;

#define lowbit(a) ((a) & (-a))
#define two(a) (1 << (a))
#define left(a) (((a) <<1) + 1)
#define right(a) (left(a) + 1)

LL gcd(LL a, LL b)
{
	return b == 0LL ? a : gcd(b, a % b);
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		int n;
		cin >> n;
		vector<LL> a;
		while(n--)
		{
			LL tmp;
			cin >> tmp;
			a.push_back(tmp);
		}
		vector<LL> b;
		for(int i = 0; i < a.size(); i++)
			for(int j = 0; j < a.size(); j++) if(a[i] >= a[j])
				b.push_back(a[i] - a[j]);
		LL rt = 0;
		for(int i = 0; i < b.size(); i++) rt = gcd(rt, b[i]);
		if(rt == 1) rt = 0;
		else rt = (rt - (a[0] % rt)) % rt;
		cout << rt << endl;
	}
	return 0;
}