#include <iostream>

using namespace std;

int main()
{
	int num;

	cin >> num;
	for (int i = 0; i < num; i++)
	{
		cout << "Case #" << (i+1) << ": ";
		unsigned int n = 1, k = 0;
		cin >> n >> k; 
		n = 1 << n;
		if ((k+1) % n == 0)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}

	return 0;
}
