#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	int count = 0;
	cin >> count;
	for(int i = 0; i != count; ++i)
	{
		long val, bits;
		cin >> bits >> val;
		cout << "Case #" << (i + 1) << ": "
				<< (~val & ((1 << bits) - 1)
						? "OFF"
						: "ON")
				<< endl;
	}
	return 0;
}
