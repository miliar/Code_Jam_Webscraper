#include <iostream>

using namespace std;

int main()
{
	int j;

	cin >> j;

	for(int i=0; i<j; i++)
	{
		int n=0;
		long long int k=0;

		cin >> n >> k;

		long long int cnt =1;

		for(int x=0; x<n; x++)
			cnt *=2;

		if( (k%cnt)+1 == cnt)
			cout << "Case #" << i+1 << ": ON\n";
		else
			cout << "Case #" << i+1 << ": OFF\n";

	}





	return 0;
}