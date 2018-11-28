#include <iostream>
using namespace std;

int main()
{
	int t,n,k,i,j;
	cin >> t;
	for (i = 1; i <= t; i++)
	{
		cin >> n >> k;
		j = (1<<n) - 1;
		k = k & j;
		cout << "Case #" << i << ": " << (k == j ? "ON" : "OFF") <<endl;
	}
	return 0;
}