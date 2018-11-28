#include <iostream>
using namespace std;

int main()
{
	freopen("A-small.in",  "r",stdin);
	freopen("A-small.out",  "w",stdout);
	int t, c;
	cin >> t;
	for (c = 1;  c <= t; c++)
	{
		int n, k, i;
		cin >> n >> k;
		i =  1 << n;
		if ((k - i + 1) % i)
			cout << "Case #"<< c<< ": OFF" << endl;
		else 
			cout << "Case #"<< c << ": ON" << endl;
	}
	return 0;
}