#include <iostream>

using namespace std;

int gcd(int a, int b)
{
	if (!(a && b)) return a+b;
	return gcd(b, a%b);		
}

int main()
{
	int c;
	cin >> c;

	for(int i=0; i<c; ++i)
	{
		int n;
		int num[3];

		cin >> n;
		for(int j=0; j<n; ++j) cin>>num[j];
		if (n==2) num[2] = num[1];

		int a = abs(num[0]-num[1]);
		int b = abs(num[1]-num[2]);
		int c = abs(num[2]-num[0]);
			
		int T = max(gcd(a,b),max(gcd(a,c),gcd(c,b)));

		int y = T - num[0]%T;	
		y %= T;

		cout << "Case #"<<i+1<<": "<<y<<endl;
	}	

	return 0;
}