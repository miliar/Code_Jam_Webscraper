#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////

int gcd(int a, int b)
{
	if(b==0) return a;
	return gcd(b, a%b);
}

int T, A1,A2,B1,B2;

bool f(int a, int b)
{
	int c=gcd(a,b);
	a/=c;
	b/=c;
	
	int p=max(a,b), q=min(a,b);
	int ret=1;
	while(true)
	{
		if( p>=2*q ) return ret;
		ret=1-ret;
		int tmp=p%q;
		p=q;
		q=tmp;
	}
}

int main()
{
	cin>>T;
	REP(index, T)
	{
		cin>>A1>>A2>>B1>>B2;
		int cnt=0;
		for(int i=A1; i<=A2; i++) for(int j=B1; j<=B2; j++) if(f(i,j)) cnt++;
		cout<<"Case #"<<index+1<<": "<<cnt<<endl;
	}
	

	return 0;
}
