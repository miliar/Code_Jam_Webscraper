/*
 *  SnapperChain.cpp
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
	for (int t=0; t<T; ++t)
	{
		ll N, K;
		cin >> N >> K;
		
		bool on = true;
		for (ll i=0; i<N && on; i++, K>>=1)
		{
			on = K&1;
		}
		
		cout << "Case #" << (t+1) << ": " << (on ? "ON" : "OFF") << endl;
		
	}
	
	return 0;
}

