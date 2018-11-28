#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>

using namespace std ;

#define ALL(x) (x).begin(),(x).end()
#define ll long long

int main ()
{
	int N ;
	cin >> N ;
	for (int cas = 1 ; cas <= N ; cas++)
	{
		int K , P , L ;
		cin >> P >> K >> L ;
		vector < pair <int , int> > freqs (L);
		int i ;
		for (i = 0; i < L ; i++)
		{
			cin >> freqs[i].first ;
			freqs[i].second = i ;
		}
		sort (ALL(freqs))	;
		reverse (ALL(freqs))	;
		int ii = 0 , jj = 0 ;
		ll ret = 0 ;
		for (i = 0 ; i < L ; i++)
		{
			ret += freqs[i].first * (jj + 1);
			ii++ ;
			if (ii >= K)
			{
				ii = 0 ;
				jj++ ;	
			}
		}
		cout << "Case #" << cas << ": " << ret << endl ;
	}
	return 0 ;
}
