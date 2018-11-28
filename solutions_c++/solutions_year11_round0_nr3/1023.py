#include <iostream>
#include <queue>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int dp[102][102][102];
int d[] = {-1,0,1};

struct Q
{
	int i,j,k;
	Q(int a,int b,int c):i(a),j(b),k(c){}
};

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc ++)
	{
		int n;
		cin >> n;
		vector <int> a(n);
		int s = 0;
		int sum = 0;
		for (int i = 0; i < n; i ++)
		{
			cin >> a[i];
			s ^= a[i];
			sum += a[i];
		}
		sort(a.begin(),a.end());		
		if (s != 0)
			cout << "Case #" << tc <<": NO" << endl;
		else
			cout << "Case #" << tc <<": " << sum-a[0] << endl;

	}

	return 0;
}
