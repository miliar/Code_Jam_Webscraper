#include <iostream>

using namespace std;

int t, n, k;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	cin >> t;
	for (int l=1;l<=t;l++)
	{
		cin >> n >> k;
		int p =(1<<n); 
		if ((k+1)%p == 0)
		{
			cout << "Case #" << l << ": ON\n";
		} else
		{
			cout << "Case #" << l << ": OFF\n";
		}
	}

	fclose(stdin);
	fclose(stdout);
}
