#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	ifstream cin("a.large.in");
	ofstream cout("a.large.out");

	int cases = 0;
	cin >> cases;
	for(int i = 0; i < cases; ++i)
	{
		int width = 0;
		int count = 0;
		cin >> width >> count;

		int mask = int(pow(double(2), width)) - 1;
		count = count % (mask + 1);
		if(count == mask)
		{
			cout << "Case #" << i + 1 << ": ON" << endl;
		}
		else
		{
			cout << "Case #" << i + 1 << ": OFF" << endl;
		}
	}
	return 0;
}