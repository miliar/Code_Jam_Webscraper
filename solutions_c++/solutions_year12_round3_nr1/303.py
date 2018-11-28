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

ll memo[1001][1001];
bool solve(ll org, ll next, const vector < pair<ll,ll> > &p){
	bool res=false;
	if(memo[org][next]!=0)return true;

	memo[org][next]=1;
	for(int i=0;i<p.size();++i){
		if(p[i].first==next){
			res=solve(org,p[i].second,p);
			if(res)return true;
		}
	}
	return res;
}


int main()
{
	ifstream ifs("data.txt");ofstream ofs("output.txt");
	ll cases; ifs>>cases;
	for(ll cas=0;cas<cases;++cas){
		ofs<<"Case #"<<cas+1<<": ";
		cout<<"Case #"<<cas+1<<": ";
		memset(memo,0,sizeof(memo));

		double result=0;
		ll N;
		ifs>>N;vector <ll> M;
		vector < pair<ll,ll> > p;
		for(int i=0;i<N;++i){
			ll tmp; ifs>>tmp; M.push_back(tmp);
			for(int j=0;j<M[i];++j){
				ifs>>tmp;
				p.push_back(make_pair(i+1,tmp));
			}
		}

		//for(int i=0;i<p.size();++i)cout<<p[i].first<<";"<<p[i].second<<endl;
		int count=0;
		for(count=0;count<p.size();++count){
			if(solve(p[count].first,p[count].second,p)){
				ofs<<"Yes"<<endl;	break;
			};
		}
		
		if(count==p.size())ofs<<"No"<<endl;
		
		//ofs<<result<<endl;		
		
	}
	
	return 0;
}



