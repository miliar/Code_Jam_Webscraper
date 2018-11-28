#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end() 
#define rep2(i,a,b) for(long long i=(a);i<=((long long)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))

struct disjointSet {
	vector<int> p, rank;
	void reserve(size_t size) {
		if (size>p.size()) {
			int o=p.size();
			rank.resize(size);
			p.resize(size);
			rep2(i,o,size-1)
				p[i]=i,rank[i]=0;
		}
	}
	void merge(int x, int y) {
		reserve(max(x+1,y+1));
		int px=find(x);
		int py=find(y);
		if(px==py)return;
		if (rank[px]>rank[py])
			p[py]=px;
		else
			p[px]=py;
		if (rank[px]==rank[py])
			rank[py]++;
	}
	int find(int x) {
		reserve(x+1);
		return x!=p[x] ? p[x]=find(p[x]) : p[x];
	}
	void clear()
	{
		p.clear();
		rank.clear();
	}
	void operator()(int x,int y){
		merge(x,y);
	}
	int operator[](int x)
	{
		return find(x);
	}
};


void Factorize(long long m,vector<long long>& p,vector<long long>& q){//m=p1^q1*p2^q2..,np=size of p,q (1-indexed)
	long long a=m; long long i=2;
	while((unsigned long long)i*i<=(unsigned long long)a) {
		if (a%i==0) {
			p.push_back(i); q.push_back(1); a/=i;
			while(a%i==0) {q.back()++; a/=i;}
		}
		i+=i==2?1:2;
	}
	if (a>1) { p.push_back(a); q.push_back(1);}
}
void gen_primes(int MAX,vector<bool> &primes) 
{ 
  int i,j;
  primes.resize(0);
  primes.resize(MAX,true); 
  primes[0]=primes[1]=0;
  for(i=2;i*i<=MAX;i++) 
    if (primes[i]) 
      for(j=i;j*i<MAX;j++) primes[i*j] = 0; 
}
vector<long long> pp;

int main() {
	freopen("a.txt","rt",stdin);
	freopen("b.txt","wt",stdout);
	int T;
	cin>>T;
	vector<bool> primes;
	gen_primes(1000000,primes);
	rep(i,primes.size())
		if(primes[i])
			pp.push_back(i);
	rep(t,T)
	{
		long long a,b,p;
		cin>>a>>b>>p;
		disjointSet ds;
		ds.reserve(b-a+1);
		foreach(i,pp)
		{
			if(*i<p)
				continue;
			
			{
				long long x=((a+(*i)-1)/ (*i))*(*i);
				long long y=x;
				for(;x<=b;x+=(*i))
				{
					ds.merge(x-a,y-a);
				}
			}
		}
		set<int> s;
		rep(i,b-a+1)
			s.insert(ds.find(i));
		cout<<"Case #"<<t+1<<": "<<s.size()<<endl;
	}
	return 0;
}
