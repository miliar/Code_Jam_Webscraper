#include <iostream>
#include <cmath>

using namespace std;

int pairs[300][2] = { 0 };
int g = 0;

bool ifExists(long n, long checker[])
{
	for(int i = 0; i < 20; i ++)
	{
		if(n == checker[i])
			return true;
	}
	return false;
}

int numberOfDigits(long n)
{
	int d = 0;
	while(n != 0)
	{
		d++;
		n /= 10;
	}
	return d;
}

long rotateAndCount(long n, long A, long B)
{
	long orig = n, x = 0;
	int d = numberOfDigits(n);
	int rotC = 0;

	long checker[20] = { 0 };	

	while(rotC++ < d)
	{
		int digit = n % 10;
		int mul = pow(10, d - 1);
		n = n / 10;
		
		if(digit == 0)
		{
			digit = (n % 10) * 10;
			n /= 10;
			mul /= 10;
			rotC++;
		}

		n = digit * mul + n;

//		if(orig == 12)
//			cout<<n<<endl;
		if(n <= B && n >= A && n != orig && n < orig) 
		{
			if(!ifExists(n, checker))
				x++;
			checker[x] = n;
		}
	}
	return x;
}

void check()
{
	for(int i = 0; i < g; i ++)
	{
		for(int j = 0; j < i; j ++)
		{
			if(i == j)
				continue;

			if((pairs[i][0] == pairs[j][0] && pairs[i][1] == pairs[j][1]) || (pairs[i][0] == pairs[j][1] && pairs[i][1] ==pairs[j][0]))
			{
				cout<<pairs[i][0]<<"  "<<pairs[i][1]<<endl;
				cout<<pairs[j][0]<<"  "<<pairs[j][1]<<endl;
				cin.get();
			}
		}
	}
}


int main()
{
	int T, count = 0;
	cin>> T;

	while(count++ < T)
	{
		long A, B;
		cin>>A>>B;

		long ans = 0;

		for(long i = A; i <= B; i ++)
		{
			if(i % 100000 == 0)
				cout<<"i: "<<i<<endl;
			ans += rotateAndCount(i, A, B);			
		}

		cout<<"Case #"<<count<<": "<<ans<<endl;

	}

	return 0;
}
