#include <iostream>
#include <cstdlib>
using namespace std;

#define INF 1500000

int main()
{
	long long r, x, T, N, minor, sum;
	
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		sum = x = 0; minor = INF;
		cin >> N;
		while(N--)
		{
			cin >> r;
			x ^= r;
			sum += r;
			if(r < minor) minor = r;
		}
		
		cout << "Case #" << t << ": ";
		if(x) 	cout << "NO\n";
		else 	cout << (sum-minor) << endl;
	}
	
	return 0;
}

