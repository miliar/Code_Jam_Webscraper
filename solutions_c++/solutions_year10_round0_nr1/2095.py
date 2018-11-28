#include <iostream>
using namespace std;
int main()
{
	long x;
	cin >> x;
	for(long i=0; i < x; i++)
	{
		long n;
		long k;
		long nn;
		cin >> n;
		cin >> k;
		
		nn = (1 << n);
		if(k % nn == nn - 1)
		{
			cout << "Case #" << i+1 << ": " << "ON\n";
		}
		else
		{
			cout << "Case #" << i+1 << ": " << "OFF\n";
		}
	}
	
	return 0;

}
