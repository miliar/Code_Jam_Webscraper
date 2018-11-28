#include <string>
#include <iostream>
using namespace std;

string solve(int n, int k)
{
	long long p = 1;
	for( int i = 0; i < n; i++)
		p *=2;
	if(k != 0 && (k+1) % p == 0 )
		return "ON";
	else
		return "OFF";
}

int main()
{
	FILE *stream = freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int count;
	cin >> count;
	for(int i = 0; i < count; i++)
	{
		int n,k;
		cin >> n;
		cin >> k;
		cout << "Case #" << i+1 << ": " << solve(n,k) << endl;
	}
}