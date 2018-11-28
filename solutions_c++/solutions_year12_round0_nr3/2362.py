
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <sstream>
#include <iterator>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <limits>
#include<ctime>

using namespace std;

const double EPS = 1e-9;
//const long long  INF = 1000000000000000000;

typedef pair<int, int> PII;
typedef pair<double,double> PDD;
typedef vector<long long> VLL;
typedef vector<int> VI;

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define REP(i,n) FOR(i,0,n)

#define UNIQUE(v) SORT(v), v.erase(unique(v.begin(),v.end()),v.end())
#define SORT(c) sort((c).begin(),(c).end())
#define ll long long

int a , b ;

set<PII> s;

int next(int k,int p)
{
	int r = k%10;
	int m=1;
	REP(i,p-1)
		m*=10;

	k/=10;
	k+= r*m;
	return k;	
}

void add(int q , int w)
{
	if (q>w) swap(w,q);
	s.insert(make_pair<int,int>(q,w));
}

int solve()
{
	s.clear();
	cin>>a>>b;
	int t = a , p=0;

	while(t>0)
	{
		p++;
		t/=10;
	}


	FOR(i,a,b+1)
	{
		int tmp = i;
		
		do
		{
			tmp = next(tmp,p);
			if (tmp>=a && tmp<=b && tmp!=i) add(i,tmp);
		}
		while(tmp!=i);
	}

	return s.size();
}

int main()
{
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output_c.txt","w",stdout);
#endif

	int T;
	cin>>T;
	

	REP(t,T)
	{
		cout<<"Case #"<<t+1<<": "<<solve()<<endl;
	}

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}