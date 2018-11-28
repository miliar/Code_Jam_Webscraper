#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <queue>
#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define rep(i,X,n) for( int (i) = (X) ; (i)<(n) ; (i) ++)
#define repit(it,X,n) for(__typeof((X)) it = (X) ; (it) != (n) ; (it)++)
#define PRINT(...) fprintf(stdout,__VA_ARGS__)
#define ALL(X) (X).begin(),(X).end()

string que[1001];
string eng[101];

int memo[1001][101];
int n,m;

int f(int qind,int engind)
{
	if(qind == m)
		return 0;
	
	int&x = memo[qind][engind];
	
	if(x!=-1)
		return x;
	
	int r = (1<<30);
	if(eng[engind] != que[qind])
		r = f(qind+1,engind);
	
	int xx;
	rep(i,0,n)
	{
		if( i == engind )
			continue;
		if(eng[i] != que[qind])
		{
			xx = f(qind+1,i)+1;
			r = min(r,xx);
		}
	}
	
	return x = r;
}

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("out.out","wt",stdout);
	
	int t;
	string s;
	
	cin>>t;
	rep(tt,0,t)
	{
		cin>>n;
		getline(cin,s);
		rep(i,0,n)
		{
			getline(cin,eng[i]);
		}
		cin>>m;
		getline(cin,s);
		rep(i,0,m)
		{
			getline(cin,que[i]);
		}
		int mm= (1<<30),x;
		memset(memo,-1,sizeof(memo));
		rep(i,0,n)
		{
			x = f(0,i);
			mm = min(mm,x);
		}
		
		cout<<"Case #"<<tt+1<<": "<<mm<<endl;
	}
	
	return 0;
}
