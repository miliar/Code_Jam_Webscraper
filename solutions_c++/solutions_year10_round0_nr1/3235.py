#include <iostream>
#include <string>
using namespace std;

long long pow(long long a, long long n)
{
	if(n==0) return 1;
	else return a*pow(a,n-1);
}

int main()
{
	long long N,I;
	cin >> N;
	for(I=0;I<N;I++)
	{
		long long n,k,p;
		string ans;
		cin >> n >> k;

		p = pow(2,n);
		if((k+1)%p==0) ans = "ON";
		else ans = "OFF";

		cout << "Case #" << I+1 << ": " << ans << endl;
	}
	return 0;
}

