#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int te;
	cin >> te;
	for(int t=1 ; t<=te ; t++)
	{
		unsigned n, xsum=0, sum=0, m = 1000001;
		
		cin >> n;
		for(int i=0 ; i<n ; i++)
		{
			unsigned v;
			cin >> v;
			xsum ^= v;
			sum += v;
			m = min(m, v);
		}

		cout << "Case #" << t << ": " ;
		if(!xsum) cout << sum - m;
		else cout << "NO";
		cout << endl;
	}
}
