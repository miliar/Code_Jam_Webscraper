#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <map>
#include <set>
#include <math.h>
using namespace std;

int Solve()
{
	int n , l, h;
	cin >> n >> l >> h;
	vector<int>v(n);
	for(int i = 0; i < n; i++)
	{
		cin >> v[i];
	}
	int ans = -1;
	for(int i = l; i <= h; i++)
	{
		bool fl = false;
		for(int  j = 0; j < n; j++)
		{
			if(v[j] % i != 0 && i % v[j] != 0)
			{
				fl = true;
				break;
			}
		}
		if(!fl)
		{
			ans = i;
			break;
		}
	}
	if(ans != -1)
		return ans;
	else
		return 0;
}
int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		int p = Solve();
		if(p != 0)
		{
			cout << "Case #" << i + 1 <<": " << p << endl;
		}
		else
		{
			cout << "Case #" << i + 1 <<": " << "NO\n";
		}
	}
	return 0;

}