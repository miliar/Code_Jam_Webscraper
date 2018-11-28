// Snapper Chain
//

#include <iostream>
#include <iomanip>

using namespace std;



int powerOf2(int n)
{  return 1 << n; }


bool isOn(int n, int k)
{  return ((k + 1) % powerOf2(n)) == 0;  }


int main()
{
	int t;
	cin >> t;

	for (int nLine = 0; nLine != t; ++nLine) {
		int n, k;
		cin >> n >> k;
		cout << "Case #" << (nLine + 1)
			<< ": " << (isOn(n, k) ? "ON " : "OFF")
			<< endl;
	}

	return 0;
}
