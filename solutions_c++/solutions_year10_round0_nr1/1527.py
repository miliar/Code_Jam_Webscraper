#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <math.h>
#include <string>
#include <string.h>
using namespace std;

long long a[2048];
int n;
long long d;
long long ans;

bool Solve()
{
	int n, k;
	cin >> n >> k;
	if(k > (1 << n))
		return (k - (1 << n) + 1) % (1 << n) == 0;
	else
		return k == (1 << n) - 1;
}

int main()
{
	freopen("d:\\test.in", "r", stdin);
	freopen("d:\\test.out", "w", stdout);
	int C;
	cin >> C;
	for(int r = 1; r <= C; r++)
	{
		cout << "Case #" << r << ": " << (Solve() ? "ON" : "OFF") << endl;
	}
	return 0;
}
