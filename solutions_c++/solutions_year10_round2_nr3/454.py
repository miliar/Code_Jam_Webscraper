#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
#define MOD 100003
map<pair<int, int>, int> M;
//int a[1000] = {0, 1, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 140268, 268066, 513350, 984911, 1892875, 3643570, 7023562, 13557020, 26200182, 50691978, 98182666, 190353370, 369393466, 717457656};
int f(int n, int m)
{
	if(M.find(make_pair(n, m)) != M.end()) return M[make_pair(n, m)];
	if(n == 0) return 1;
	if(n < 0 || m == 0) return 0;
	int ret = 0;
	for(int i = n - 1; i >= n - m; i--)
	{
		ret = (ret + f(i, m)) % MOD;
	}
	M[make_pair(n, m)] = ret;
	return ret;
}
int main()
{
//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("Clarge.txt", "w", stdout);
	//a(n)=2a(n-1)+a(n-2)-2a(n-3)-a(n-4)+a(n-6)
	/*for(int n = 500; n >= -1; n--)
	for(int m = 500; m >= 0; m--)
	{
		f(n, m);
	}*/
	int T;
	cin>>T;
	int Case;
	for(Case = 1; Case <= T; Case++)
	{
		int N;
		cin>>N;
		int ans = 0;
		for(int i = -1; i < N; i++)
			ans = (ans + f(i, N-1-i)) % MOD;
		printf("Case #%d: %d\n", Case, ans);
	}
	return 0;
}