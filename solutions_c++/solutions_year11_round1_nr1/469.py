#line 5 "code.cpp"
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define sqr(x) (x)*(x)
#define For(i,n,m) for(int i=n;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef vector<vector<pair<int,int> > > adjL;
ll gcd(ll a,ll b)
{
	if(b==0)
		return a;
	return gcd(b,a%b);
}
bool isValid(ll n,int d,int c)
{
	if(d==100)
		if(c==0)
			return false;
		else
			return true;
	else if(d==0)
		if(c==100)
			return false;
		else
			return true;
	else
	{
		if(c==100)
			if(d==100)
				return true;
			else
				return false;
		else if(c==0)
			if(d==0)
				return true;
			else 
				return false;
		int makam=100/gcd(100,d);
		if(n>=makam)
			return true;
		return false;
	}

}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cases;
	cin>>cases;
	rep(a,cases)
	{
		ll n,d,c;
		cin>>n>>d>>c;
		cout<<"Case #"<<a+1<<": ";
		if(isValid(n,d,c))
			cout<<"Possible\n";
		else
			cout<<"Broken\n";
	}
}