#include <fstream>
using namespace std;

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("a.out");
	int t, n, k;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cin >> n >> k;
		if ((k + 1) % (1 << n))
			cout << "Case #" << i << ": OFF" << endl;
		else
			cout << "Case #" << i << ": ON" << endl;
	}
	return 0;
}