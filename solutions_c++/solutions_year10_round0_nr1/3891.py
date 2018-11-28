#include <iostream>
using namespace std;

int main()
{
	freopen("A-large.in",  "r",stdin);
	freopen("A-large.out",  "w",stdout);
	int t, i;
	cin >> t;
	for (i = 1;  i <= t; i++)
	{
		int n, k, b;
		cin >> n >> k;
		b =  1 << n;
		if (! ((k - b + 1) % b) && (k - b + 1 >= 0))
			cout << "Case #"<< i<< ": ON" << endl;
		else 
			cout << "Case #"<< i << ": OFF" << endl;
	}
	return 0;
}