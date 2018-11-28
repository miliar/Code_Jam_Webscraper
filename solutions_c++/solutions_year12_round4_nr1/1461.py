// A.cpp : Defines the entry point for the console application.
//

#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>

using namespace std;
#define ll long long


ll gcd(ll m, ll n)
{
    ll r;
    if (m < n) {swap(m, n);}
    if (n == 0) {return m;}
    if ((r = m % n)) {return gcd(n, r);}
    return n;
}

ll lcm(ll m, ll n)
{
    return (m * n) / gcd(m, n);
}

ll memo[10001];
ll D;
ll solve(ll pos,ll h, vector <ll> l, vector <ll> d){
	//cout<<pos<<endl;
	//if(memo[pos]>=h){return 0;}

	ll lmax=0;ll result=0;
	for(ll i=0;i<d.size();++i){
		if(h>=abs(d[pos]-d[i])){
			if(memo[i]<min(l[i],abs(d[pos]-d[i]))){
				memo[i]=min(l[i],abs(d[pos]-d[i]));

				if(d[i]+memo[i]>=D){
					memo[10000]=1;
					return 1;
				};
				ll tmp;
				if(solve(i, min(l[i],abs(d[pos]-d[i])),l,d)==1)break;
				

			}
		}

	}
	return 0;
	//memo[pos]=l;
	//return lmax;

}

int main()
{
	ifstream ifs("data.txt");
	FILE* fp_out = freopen("small2.txt", "w", stdout);
	//FILE* fp_out = freopen("large.txt", "w", stdout);

	ll cases; ifs>>cases;
	for(ll cas=0;cas<cases;++cas){
		cout<<"Case #"<<cas+1<<": ";
		ll N;
		ifs>>N;
		vector <ll> l,d;
		for(ll i=0;i<N;++i){
			ll ltmp,dtmp;
			ifs>>dtmp>>ltmp;
			l.push_back(ltmp);
			d.push_back(dtmp);
		}
		
		ifs >>D;

		memset(memo,0,sizeof(memo));

	//memo[0]=d[0];
	
		if(d[0]+d[0]>=D){
			memo[10000]=1;
		}else{
			solve(0,d[0],l,d);
		}

		if(memo[10000]==1){
			cout<<"YES"<<endl;
		}else{
			cout<<"NO"<<endl;//cout<<memo[10000]<<endl;
		}
		
	}
	
	return 0;
}



