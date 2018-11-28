#include <iostream>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int A,B,t;
	long long ans;

	cin >>t;

	for(int c = 1;c <= t;++c)
	{
		cin >> A >> B;

		ans = 0;

		for (int n = A;n <= B;++n)
		{
			int temp = n,len = 0;

			while (temp > 9) {
				temp /= 10;
				len ++;
			}
			len++;

			int power = 1;
			
			for (int i = 1;i < len;++i) power *= 10;

			temp = n;

			for (int i = 1;i < len;++i)
			{
				int m = temp / 10 + temp % 10 * power;

				if (m > n && m <= B) ans++;

				temp = m;
			}
		}

		cout <<"Case #"<<c<<": "<<ans <<endl;
	}

	return 0;
}