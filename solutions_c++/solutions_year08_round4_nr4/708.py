#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <complex>
#include <valarray>
#include <deque>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;

#define RI( i, o ) for(typeof(o.begin()) i= (o).begin(); i!=(o).end(); ++i)
#define RP3( x, y, z ) RP( i, 0, x ) RP( j, 0, y ) RP( k, 0, z )
#define RP( i, s, e ) for(typeof(s) i=(s); i<(e); ++i)
#define R( i, x ) RP(i,0,(x).size())
#define pB push_back

int k; string m;
vi p;
int ans;
int test()
{
	string c=m;
	char last='8';
	int cost=0;
	for(int i=0; i<c.size()/k; ++i)
	{
		for(int j=0; j<k; ++j)
			c[i*k+j]=m[i*k+p[j]];
	}
	
	R(i, c)
	{
		if(c[i]!=last) ++cost;
		last=c[i];
	}
	
	//cout<< p[0] << p[1] << p[2] << p[3] << c << " "<< cost << endl;
	return cost;
}

int ss(int t)
{
	if(t==k)
	{
		ans=min(ans,test());
	}
	else
	{
		for(int i=0; i<k; ++i)
		{
			for(int j=0; j<t; ++j)
				if(i==p[j]) goto tt;
			p[t]=i;
			ss(t+1);
			tt:;
		}
	}
}

int main()
{
	int N;
	cin >> N;
	for(int cn=1; cn<=N; ++cn)
	{
		cin >> k >> m;
		ans=1<<20;
		p=vi(5,0);
		ss(0);
		
		
		cout << "Case #" << cn << ": " << ans << endl;
	}
	return 0;
}
