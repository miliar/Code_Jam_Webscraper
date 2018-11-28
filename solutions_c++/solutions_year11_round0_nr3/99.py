#include <iostream>
using namespace std;

long long sum;
long long bit;

long long llmin;
int main ()
{
	int cases;
	cin >> cases;
	int n;
	long long tmp;
	for (int i = 0 ; i < cases; i++)
	{
		cout << "Case #" << i+1 << ": ";
		sum = 0; bit = 0; llmin = 1000000;
		cin >> n;
		for (int j = 0 ; j < n ; j++)
		{
			cin >> tmp;
			if (tmp < llmin) llmin = tmp;
			sum += tmp;
			bit ^= tmp;
		}
		if (!bit) cout << sum - llmin << endl;
		else cout << "NO" << endl;
	}
}
