#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>

using namespace std;

#define RP(i,j,k) for(int i=j; i<k; ++i)
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

long double v[60];
int S, D;

long double sv(int c)
{
	long double &m=v[c];
	if(m>-.5) return m;
	if(c==S) return m=0;
	
	m=0;
	long double p0=0;
	
	// have c/S
	int gg=0, gg2=0;
	RP(i,0,(1<<S)){
		if(D == __builtin_popcount(i)){
			++gg2;
			int ct=0;
			RP(j,0,S) if(i&(1<<j))
			{
				if(j>=c) ++ct;
			}
			if(ct)
				++gg;
		}
	}
	
	RP(i,0,(1<<S))
	{
		if(D == __builtin_popcount(i))
		{
			int ct=0;
			RP(j,0,S) if(i&(1<<j))
			{
				if(j>=c) ++ct;
			}
			if(ct){
				m+=sv(ct+c)*1./(gg);
				//P(sv(ct+c));
				//P(ct+c)
			}
			else
				p0+=1./(gg2);
		}
	}

	return m=m+1/(1-p0);
}

int main()
{
	int C;
	cin >> C;
	for(int cs=1; cs<=C; ++cs)
	{
		
		cin >> S >> D;
		RP(i,0,60) v[i]=-1;
		
		double pp=sv(0);
		
		printf("Case #%d: %.7f\n",cs,pp);
	}
	
	return 0;
}
