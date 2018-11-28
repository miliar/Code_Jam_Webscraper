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

ll solve(ll f_pos, ll s_pos, const vector < pair<ll,ll> > &f, const vector < pair <ll,ll> > &s){
	vector < pair<ll,ll> > f_tmp=f;
	vector < pair<ll,ll> > s_tmp=s;
	if(f_pos>=f_tmp.size()||s_pos>=s_tmp.size())return 0;
	ll take=0;
	if(f_tmp[f_pos].first==s_tmp[s_pos].first){
		take=min(f_tmp[f_pos].second,s_tmp[s_pos].second);
		f_tmp[f_pos].second-=take;
		s_tmp[s_pos].second-=take;
	}
	/*if(take==f_tmp[f_pos].second){
		f_pos++;
	}
	if(take==s_tmp[s_pos].second){
		s_pos++;
	}*/
	return take+max(solve(f_pos,s_pos+1,f_tmp,s_tmp),solve(f_pos+1,s_pos,f_tmp,s_tmp));
}
int main()
{
	ifstream ifs("data.txt");ofstream ofs("output.txt");
	ll cases; ifs>>cases;
	for(ll cas=0;cas<cases;++cas){
		ofs<<"Case #"<<cas+1<<": ";
		cout<<"Case #"<<cas+1<<": ";
		ll result=0;
		ll N,M;
		ifs>>N>>M;
		
		vector < pair<ll,ll> > f,s;
		vector <ll> a,A;
		for(ll i=0;i<N;++i){
			ll tmp;ifs>>tmp;
			a.push_back(tmp);
			ifs>>tmp;A.push_back(tmp);
			//cout<<a[i]<<" "<<A[i]<<endl;
			f.push_back(make_pair(A[i],a[i]));
		}

		vector <ll> b,B;
		for(ll i=0;i<M;++i){
			ll tmp; ifs>>tmp;
			b.push_back(tmp);ifs>>tmp;B.push_back(tmp);
			//cout<<b[i]<<" "<<B[i]<<endl;
			bool isInA=false;
			for(int j=0;j<N;++j){
				if(B[i]==A[j]){isInA=true;break;};
			}
			if(isInA)s.push_back(make_pair(B[i],b[i]));
		}
		
		ll f_pos=0,s_pos=0;

		result=solve(0,0,f,s);

		cout<<result<<endl;
		ofs<<result<<endl;		
	}
	
	return 0;
}



