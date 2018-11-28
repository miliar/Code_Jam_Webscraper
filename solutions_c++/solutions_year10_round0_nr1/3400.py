#include <fstream>

using namespace std;

ifstream cin ("input.txt"); ofstream cout ("output.txt");


int main ()
{
	long long t;
	long long n , k;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i+1 << ": ";
		cin >> n >> k;
		if (! ((k + 1) % (1 << n))) cout << "ON" ; else cout << "OFF";
		cout << endl;
	}

	return 0;
}