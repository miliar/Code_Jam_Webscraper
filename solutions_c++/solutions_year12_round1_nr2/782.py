
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

bool ss(PII a , PII b)
{
	return a.second<b.second;
}

int solve(int n, vector<PII> v)
{
	sort(v.begin(), v.end(),ss);
	vector<int> state(n);
	int stars = 0,c;

	while(true)
	{
		c=0;
		REP(i,n) if (state[i]>=2) c++;
		if (c==n) break;

		bool ok = false;

		REP(i,n)
		{
			if ((state[i]==0) && v[i].second<=stars)
			{
				state[i] = 2;
				stars+= 2;
				ok = true;
				break;
			}
		}

		if (!ok)
		{
			REP(i,n)
			{
				if ((state[i]==1) && v[i].second<=stars)
				{
					state[i] += 2;
					stars+= 1;
					ok = true;
					break;
				}
			}
		}

		if (!ok)
		{
			FORD(i,n-1,0)
			{
				if ((state[i]==0) && v[i].first<=stars)
				{
					state[i]=1;
					stars+=1;
					ok=true;
					break;
				}
			}
		}
		if (!ok) break;
	}
	int res=0;
	c=0;
	REP(i,n)
	{
		if (state[i]>=2) 
		{
			c++;
			if (state[i]==3) res+=2;
			else res++;
		}
	}

	if (c!=n) return -1;
	return res;
}

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output_b_hard.txt","w",stdout);
//#endif

	int T;
	cin>>T;

	REP(t,T)
	{
		int n;
		cin>>n;
		vector<PII> v(n);
		REP(i,n)
			cin>>v[i].first>>v[i].second;

		int res = solve(n,v);
		if (res!=-1)
			printf("Case #%d: %d\n",t+1,res);
		else
			printf("Case #%d: Too Bad\n",t+1);

	}

#ifdef LocalHost
	//cout<<endl<<endl<<"TIME: "<<clock()<<endl;
#endif

}