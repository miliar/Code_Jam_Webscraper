#include <iostream>
#include <cmath>

using namespace std;

int main(void)
{
	int numofp;

	cin >> numofp;
	for(int ncount = 1; ncount <= numofp;ncount++)
	{
		int a,b;
		cin >> a >> b;
		if( (b % (int)pow(2.0f,a)) - (pow(2.0f,a) - 1) == 0)
			cout << "Case #" << ncount << ": ON" << endl;
		else
			cout << "Case #" << ncount << ": OFF" << endl;
	}

	return 0;
}