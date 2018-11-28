#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int numcases, curcase;
	long numsnappers, numsnaps, tpow;
	cin >> numcases;
	for (int i = 0; i < numcases; i++)
	{
		cin >> numsnappers >> numsnaps;
		tpow = 1;
		for (int j = 0; j < numsnappers; j++ )
			tpow <<= 1;
			// cout << i << ' ' << numsnappers << ' ' << numsnaps << ' ' << tpow << ' ';
		cout << "Case #" << i+1<<": ";
		if (((numsnaps+1) % tpow) == 0)
			cout << "ON\n";
		else
			cout << "OFF\n";
	}
	return 0;
}
