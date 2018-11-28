#include <iostream>
using namespace std;
void solve(int test)
{
	int n,l,h;
	cin >> n >> l >> h;
	int mas[100];
	for (int i = 0 ; i < n; i++)
		cin >> mas[i];
	cout <<"Case #" << test <<": ";
	for (int i = l ; i < h + 1; i++)
	{
		bool flag = true;
		for (int j = 0 ; j < n && flag; j++)
			 if (mas[j] % i  != 0  && i % mas[j] != 0)
				 flag = false;
		if (flag)
		{
			cout << i << '\n';
			return;
		}
	}
	cout << "NO\n";
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i = 0 ;i  < t ;i++)
		solve(i + 1);
	return 0;
}