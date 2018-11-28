#include <iostream>
using namespace std;

int main()
{
	unsigned int t, k, f[32], base[32];
	int i;
	for(i=0;i<32;i++)
	{
		base[i] = 1 << i;
		f[i] = base[i] - 1;
	}

	int num,size;
	cin >> size;
	for(num = 1; num <= size; num++)
	{
		cin >> t >> k;
		cout << "Case #" << num << ": ";
		if( k >= f[t] && (k - f[t])%base[t] == 0 )
		{
			cout<< "ON" << endl;
		}else
		{
			cout<< "OFF" << endl;
		}
	}
	
	return 0;
}
