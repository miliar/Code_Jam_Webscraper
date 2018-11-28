#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <cstring>
#include <map>
using namespace std;

int a[1 << 10][1 << 10][12];

int findMin(int l, int p, int c)
{
	if(a[l][p][c] != -1)
		return a[l][p][c];
	int minCut = (1 << 30);
	if(l * c >= p)
		return 0;
	for(int i = l + 1; i < p; i++)
	{
		int tmp1 = findMin(l, i, c);
		int tmp2 = findMin(i, p, c);
		int cut = max(tmp1, tmp2) + 1;
		if(cut < minCut)
			minCut = cut;
	}
	a[l][p][c] = minCut;
	return minCut;
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	memset(a, -1, sizeof(a));
	for(int nt = 1; nt <= T; nt++)
	{
		int l, p, c;
		cin >> l >> p >> c;
		cout << "Case #" << nt << ": " << findMin(l, p, c) << endl;
	}

	return 0;
}