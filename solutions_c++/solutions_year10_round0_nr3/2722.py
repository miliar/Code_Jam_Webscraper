/*
 *  ThemePark.cpp
 *
 *  Created by Josh Deprez on 8/05/10.
 *
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
typedef long long ll;
typedef unsigned int uint;
using namespace std;

int main()
{
	
	int T;
	cin >> T;

	for (int t=0; t<T; ++t) {
		
		vector<ll> g;
		ll R, k, N;
		cin >> R >> k >> N;
		
		g.resize(N);
		for (int i=0; i<N; ++i)
		{
			cin >> g[i];
		}
		
		ll S = 0, A, C;
		int i=0, j;
		
		for (C=0; C<R; C++)
		{
			ll Q = 0;
			int m=0;
			for (j=i; Q<k && m<N; j=(j+1)%N, m++)
			{
				Q += g[j];
			}
			if (Q > k) 
			{
				j = (N+j-1)%N;
				Q -= g[j];
			}
			i=j;
			S += Q;
			//if (i==0) { C++; break; }
		}
		A = S;
		/*A = S * (R / C);
		//cout << "Provisional: " << A << endl;
		for (i=0; i<R%C; ++i)
		{
			ll Q = 0;
			j=0;
			for (; Q<k; j=(j+1)%N)
			{
				Q += g[j];
			}
			if (Q > k) 
			{
				j = (N+j-1)%N;
				Q -= g[j];
			}
			A += Q;
		}*/
		
		
		cout << "Case #" << (t+1) << ": " << A << endl;
	}
	 
	return 0;
}

