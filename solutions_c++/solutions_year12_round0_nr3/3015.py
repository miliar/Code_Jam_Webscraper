#include <iostream>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int i = 1; i <= T; ++i)
	{
		int A,B;
		cin>>A>>B;

		int digits = 1;
		int tmp = A;
		while(tmp/10)
		{
			++digits;
			tmp /= 10;
		}

		int ret = 0;
		for(int j = A; j <= B; ++j)
		{
			int n = j;		
			int left = pow(10.0,digits-1);
			int right = 10;
			int pm = 0;
			for(int k = 1; k < digits; ++k)
			{
				int m = n%(right)*left + n/right;
				if(m > n && m <= B && m != pm)
				{
					++ret;
					pm = m;
				}
				right *= 10;
				left /= 10;
			}
		}

		cout<<"Case #"<<i<<": "<<ret<<endl;
	}
}