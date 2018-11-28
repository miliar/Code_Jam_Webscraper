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


bool happy(int i,int j)
{
	set<int> iset;
	int remain;
	int sum=i;
	while(1)
	{
	remain=sum;
	sum=0;
	while(remain!=0)
	{
		int t= remain%j;
		sum+=t*t;
		remain=remain/j;
	}
	if(sum==1)
		return true;
	if(iset.count(sum)!=0)
		return false;
	else
		iset.insert(sum);
	}
}
int res[100000];
void init()
{
	memset(res,0,sizeof(0));
	int i;
	for(i=2;i<100000;i++)
	{
		For(j,2,10)
	{
		if(happy(i,j))
			res[i]|=1<<j;
	}
		if(res[i]==0x7fc)
			break;
	}
	return ;
}
void solve(int test)
{
	char buf[90];
	gets(buf);
	int i=0;
	int search=0;
	int ans=0;
	while(buf[i]!='\0')
	{
		if((buf[i]>'1')&&(buf[i]<='9'))
			search|=1<<(buf[i]-'0');
		if(buf[i]=='1')
		{
			search|=1<<10;
			i++;
		}

		i++;
	}
	fprintf(stderr,"test=%d\n",test);
	For(i,2,100000)
	 if((res[i]&search)==search)
	 {
		 ans=i;
		 break;
	 }
	cout<<"Case #"<<test<<": "<<ans<<endl;
}


int main() {
	freopen("a.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	init();
	cin>>N;
	char buf[90];
	gets(buf);
	For(test,1,N)
	{
		solve(test);	
	}
}