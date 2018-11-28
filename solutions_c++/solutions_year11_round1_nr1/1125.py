#include <iostream>
using namespace std;

int gcd(int a, int b)
{
	long long t;
	while(b != 0)
	{
		t = b;
		b = a%b;
		a = t;
	}
	return a;
}	

bool check_pd(int n, int pd)
{
	for(int i = 1; i <= n; i++)
	{
		int x = i*pd;
		if(x%100 == 0)
			return true;
	}
	return false;
}

int main()
{	
	int t,pD,pG;
	long long N;
	
	cin >> t;
	for(int z = 1; z <= t; z++)
	{
		cin >> N >> pD >> pG;
		int x = gcd(pD,100LL);
		int y = 100/x;
		cout << "Case #" << z << ": ";
		if(y > N)
			cout << "Broken";
		else if(pG == 100 && pD != 100)
			cout << "Broken";
		else if(pG == 0 && pD != 0)
			cout << "Broken";
		else
			cout << "Possible";
		//cout << " " << check_pd(N,pD) << endl;
		cout << endl;
	}
}