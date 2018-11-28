#include<algorithm>
#include<cmath>
#include<iostream>
#include<iterator>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

long gcd(long a, long b)
{
	long t;
	while (b != 0)
	{
		t = b;
		b = a % b;
		a = t;
	}
	return a;
}

int main()
{
	// Meaningful variable names.
	long C, N, T, y, diff, t, lastT;
	cin >> C;
	for (int i=1; i<=C; ++i)
	{
		cin >> N;
		diff = 0;
		T = -1;
		cin >> lastT;
		for (int n=1; n<N; ++n)
		{
			cin >> t;
			diff = fabs(t - lastT);
			if (T < 0)
				T = diff;
			else
				T = gcd(T, diff);
			
		}
		
		y = (T - (t%T))%T;
		
		cout << "Case #" << i << ": " << y << endl;
	}
	
	return 0;
}