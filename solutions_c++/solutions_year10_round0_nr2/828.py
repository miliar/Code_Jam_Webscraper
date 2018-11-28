#include <iostream>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b)
{
	if(a < b) return gcd(b, a);
	while(b != 0)
	{
		long long tmp = a;
		a = b;
		b = tmp%a;
	}
	return a;
}

void work(int n)
{
	long long *t, T, res;
	t = new long long[n+1];

	for(int i=0; i<n; i++)
		cin >> t[i];
	sort(t, t+n);

	T = t[1]-t[0];
	for(int i=1; i<n; i++)
		for(int j=i+1; j<n; j++)
			T = gcd(T, t[j]-t[i]);

	if(t[0]%T == 0)
		res = 0;
	else
		res = ((t[0]/T)+1)*T-t[0];

	for(int i=1; i<n; i++)
		if(t[i]%T != 0)
			res = max(res, ((t[i]/T)+1)*T-t[i]);

	cout << res << endl;
}

int main()
{
	int iCase = 1, n, c;
	cin >> c;
	while(c--)
	{
		cin >> n;
		printf("Case #%d: ", iCase++);
		work(n);
	}
	return 0;
}
