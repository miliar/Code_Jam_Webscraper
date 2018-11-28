#include <iostream>
#include <cmath>

using namespace std;


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
//			cout<<n<<", orig: "<<orig<<endl;
			x++;
		}
	}
	return x;
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
			ans += rotateAndCount(i, A, B);			
		}

		cout<<"Case #"<<count<<": "<<ans<<endl;
	}

	return 0;
}
