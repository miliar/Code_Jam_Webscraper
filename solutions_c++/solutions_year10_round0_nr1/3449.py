#include<iostream>
#include<math.h>
#include<vector>
using namespace std;


int main()
{
	int T;
	cin >> T;
	for(int t = 0; t < T;t++)
	{
		long long n, k;
		cin >> n >> k;
		long long x = pow(2,n);

		k = k % x;
		//cout << "k is " << k << endl;
		long long y = pow(2,n);
		y--;
		//cout << "y is " << y << endl;
		cout << "Case #" << (t+1) << ": ";
		if(y ^ k)
			cout << "OFF" << endl;
		else
			cout << "ON" << endl;
	


	}




}
