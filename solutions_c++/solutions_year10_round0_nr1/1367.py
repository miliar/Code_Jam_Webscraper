#include <iostream>
#include <vector>
#include <stdint.h>

using namespace std;

void snapper(int n, uint64_t k)
{
	if (n > 63)
	{
		cout << "OFF" << endl;
		return;
	}
	for (int i = 0; i < n; i++)
	{
		if (!((k >> i) & 1))
		{
			cout << "OFF" << endl;
			return;
		}
	}
	cout << "ON" << endl;
}


int main()
{
	int ncases = 0;
	cin >> ncases;
	if (!cin) return -1;
	
	for (int i = 0; i < ncases; i++)
	{
		int n, k;
		cin >> n >> k;
		if (!cin) return -1;
		cout << "Case #" << (i+1) << ": ";
		snapper(n, k);
	}
	return 0;
}

