
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

int solve()
{
	int n,  s , p , res=0, pos=0;
	cin>>n>>s>>p;
	vector<int> v(n) , tmp;
	REP(i,n)
		cin>>v[i];
	
	REP(i,n)
	{
		int k = v[i]/3;
		int r = v[i] - 3*k;
		if (k>=p || (r>0 && (k+1)>=p))
			res++;
		else
			tmp.push_back(v[i]);
	}


	REP(i,tmp.size())
	{
		int k = tmp[i]/3;
		int r = tmp[i] - 3*k;

		if (r==0)
		{
			if (k<1)
			{
				if (k>=p) pos++;
			}
			else
			{
				if (k+1>=p) pos++;
			}
		}
		else if (r==1)
		{
			if (k+1>=p) pos++;
		}
		else if (r==2)
		{
			if (k+2>=p) pos++;
		}
	}

	return res + min(s,pos);
}

int main()
{
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output_b.txt","w",stdout);
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