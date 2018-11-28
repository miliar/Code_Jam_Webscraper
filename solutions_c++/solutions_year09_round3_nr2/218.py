#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

long double pos[501][3];
long double speed[501][3];
int size;
long double xyz[3];
long double vxyz[3];
void solve(int test)
{

	cin>>size;
	For(i,0,size-1)
	{
		For(j,0,2)
			cin>>pos[i][j];
		For(j,0,2)
			cin>>speed[i][j];

	}
	For(i,0,2)
		xyz[i]=0.0;
	For(i,0,2)
		vxyz[i]=0.0;
	For(j,0,2)
		For(i,0,size-1)
	{
		xyz[j]+=pos[i][j];
		vxyz[j]+=speed[i][j];
	}
	For(i,0,2)
	{
		xyz[i]=xyz[i]/size;
		vxyz[i]=vxyz[i]/size;
	}
	double a=0.0;
		For(i,0,2)
	{
		a+=vxyz[i]*vxyz[i];
	}
		long double b=0.0;
		For(i,0,2)
	{
		b+=2*xyz[i]*vxyz[i];
	}
	long double c=0.0;
		For(i,0,2)
	{
		c+=xyz[i]*xyz[i];
	}
	long double ans=0.0;
	long double time=0.0;
	if(b>=0.0)
	{
		time=0.0;
		ans=sqrt(c);
	}
	else
	{
		time=(0.0-b)/(2*a);
		ans=a*time*time+b*time+c;
		if(ans<0.0)
		{
			ans=0.0;
			time=((0.0-b)-sqrt(b*b-4*a*c))/(2*a);
		}
		else
			ans=sqrt(ans);
	}
	
	fprintf(stderr,"test=%d\n",test);
	cout<<"Case #"<<test<<": ";
	printf("%.8f",ans);
	cout<<" ";
	printf("%.8f",time);
	cout<<endl;
}


int main() {
	freopen("a.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	cin>>N;
	For(test,1,N)
	{
		solve(test);	
	}
}