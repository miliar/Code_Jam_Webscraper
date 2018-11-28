// a.cpp : Defines the entry poll for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include<fstream>
#include<vector>
using namespace std;
typedef long long ll;
vector<ll> nums;
int main()
{
	ifstream cin("a.txt");
    ofstream cout("sol.txt");
    ll cases;
    cin >> cases;

	
    for (ll cas = 0; cas < cases; cas++)
    {

        ll P,K,L,F;

        cin >> P>>K>>L;
        for(ll small=0;small<L;small++)
		{
			cin>>F;
		nums.push_back(F);
		}
        sort(nums.begin(),nums.begin()+L);
		ll frac=0;
        ll ans = 0;
		vector<ll>::iterator it=nums.end();
		it--;
		for(ll i=0;i<L;i++)
		{
			if(i%K==0)
				frac++;
			ans=ans+(*it)*frac;
			if(it==nums.begin())
				break;
			it--;
		}
        cout << "Case #" << cas + 1 << ": " << ans << "\n";
	nums.clear();
    }
    return 0;
}


int _tmain(int argc, _TCHAR* argv[])
{
	return 0;
}