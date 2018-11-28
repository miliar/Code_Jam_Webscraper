#include <iostream>
using namespace std;
bool prov(int k)
{
	for (int i = 2 ;i < k; i++)
		if(k % i == 0)
			return false;
	return true;
}
void test(int T)
{
	int n; 
	cin >> n;
	int ans1= 0, ans2 = 1;
	for (int i = 2; i <= n; i++)
	{
		if (prov(i))
			ans1++;
	}
	
	for (int i = 2 ; i <= n; i++)
	{
		int k = i;
		if(prov(k) == false)
			continue;	
		while(k <= n)
		{
			k*=i;
			ans2++;
		}
	}
	ans1 = max(ans1,1);
	cout << "Case #" << T <<": " << ans2 - ans1 << '\n';
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i = 0 ; i < t; i++)
		test(i + 1);
	return 0;
}