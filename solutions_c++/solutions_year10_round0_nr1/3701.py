#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int tests;
	cin >> tests;
	for(int i = 0; i < tests; i++)
	{
		long long N, K;
		cin >> N >> K;
		cout << "Case #" << i+1 << ": ";
		if((K+1)%(1<<N)==0)
			cout << "ON" << endl;
		else
		{
			cout << "OFF" << endl;
		}
	}
}