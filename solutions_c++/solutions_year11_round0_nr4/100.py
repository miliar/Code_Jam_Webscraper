#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int ans = 0;
	int cases;
	cin >> cases;
	int n;
	int tmp;
	for (int i = 0 ; i < cases; i++)
	{
		ans = 0;
		cin >> n;
		for (int j = 1 ; j <= n ; j++)
		{
			cin >> tmp;
			if (tmp != j) ans++;
		}
		cout << "Case #" << i+1 << ": " << showpoint << (double)ans << endl;
	}
}
