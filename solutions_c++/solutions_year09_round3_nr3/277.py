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

int size;
int vm[5];
int m;
#define MAX 10000
int resc()
{
	int vt[9];
	int res=0;
	For(i,0,8)
	{
		vt[i]=1000;
	}
	vt[0]=0;vt[1]=m;
	int p,k;
	For(i,0,size-1)
	{
		For(j,0,size+1)
		{
			if(vt[j]>vm[i])
			{
				p=vt[j-1];
				k=vt[j];
				break;
			}
		}
		res+=(k-vm[i]-1)+(vm[i]-p-1);
		vt[7]=vm[i];
		sort(&vt[0],&vt[8]);
	}
	return res;
}
void solve(int test)
{

	int P,Q;
	cin>>P>>Q;
	m=P+1;
	For(i,0,Q-1)
	{
		int t;
		cin>>t;
		vm[i]=t;
	}
	size=Q;
	sort(&vm[0],&vm[Q-1]);
	int ans=MAX;
	do{
		int t=resc();
		if(t<ans)
			ans=t;

	}while(next_permutation(&vm[0],&vm[Q]));
	fprintf(stderr,"test=%d\n",test);
	cout<<"Case #"<<test<<": "<<ans<<endl;
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