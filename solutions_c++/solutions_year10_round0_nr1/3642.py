#include <iostream>
#include <vector>

using namespace std;

int main()
{
	unsigned int t, n, k;
	cin >> t;
	for (unsigned int i=1; i<=t; ++i)
	{
		cin >> n >> k;
		cout << "Case #" << i << ": " << ((((1<<n)-1)==(k&((1<<n)-1))) ? "ON" : "OFF") << endl;
	}
}
