#include <iostream>
using namespace std;

long long pow(long long a, long long b)
{
	long long res = 1;
	while(b--)
		res *= a;
	return res;
}

int main()
{
	long long T, n, k;
	cin >> T;
	for(int i=0; i<T; i++)
	{
		cin >> n >> k;
		printf("Case #%d: ", i+1);
		if(k == 0)
			cout << "OFF\n";
		else if((k+1)%pow(2, n) == 0)
			cout << "ON\n";
		else
			cout << "OFF\n";
	}
	return 0;
}
