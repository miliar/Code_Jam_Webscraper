//C:\Users\Shubham\Documents\Visual Studio 2005\Projects
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		int N, K;
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		if ((K & (1 << N) - 1) == (1 << N) - 1)
			cout << "ON\n";
		else
			cout << "OFF\n";
	}
	return 0;
}
