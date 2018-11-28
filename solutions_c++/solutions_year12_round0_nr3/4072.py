#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		int a, b, sum = 0;
		cin >> a >> b;
		for(int j = a; j <= b; j++)
		{
			int tmp = j, length = 1;
			while(tmp /= 10) length++;
			tmp = j;
			int len = length;
			while(length-- > 1)
			{
				int n = (tmp + (tmp % 10) * pow(10, len)) / 10;
			
				if(n <= b && n >= a && n != tmp)
					sum++;
				tmp = n;
			}
		}
		cout << "Case #" << i << ": " << sum / 2 << endl;
	}
	return 0;
}