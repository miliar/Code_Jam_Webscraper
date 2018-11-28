#include <iostream>
using namespace std;
bool getState(unsigned long long k,unsigned long long n)
{
	k = k & (0xffffffffffffffffULL >> (64-n));
	if(k == (1ULL<<n)-1)
		return 1;
	else
		return 0;
}

int main()
{
	unsigned long long k,n;
	int t;
	cin >> t;
	for(int i=1 ; i<=t ; i++)
	{
		cin >> n >> k;
		cout << "Case #" << i << ": ";
		if(getState(k,n))
			cout << "ON\n";
		else
			cout << "OFF\n";
	}
}
