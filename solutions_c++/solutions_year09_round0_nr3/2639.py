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

int Res[1 << 20];
int I[32];

int ans=0;
char d[501];
const char * pat="welcome to code jam";
const int len=19;
int value[501][len];
int main() {
	freopen("a.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	char buf[50];
	gets(buf);
	For(test, 1, atoi(buf)) {
		gets(d);
		int length=strlen(d);
		memset(value,0,sizeof(value));
		if(d[0]==pat[0])
			value[0][0]=1;
		For(i,1,(length-1))
			For(j,0,(len-1))
		{
			if(j==0){
				if(d[i]==pat[j])
				value[i][j]=(value[i-1][j]+1)%10000;
				else
				value[i][j]=value[i-1][j];
			}
			else {if(d[i]==pat[j])
				value[i][j]=(value[i-1][j]+value[i-1][j-1])%10000;
			else
				value[i][j]=value[i-1][j];
			}
		}

		cout<<"Case #"<<test<<": ";
		if(value[length-1][len-1]>999)
			cout<<value[length-1][len-1];
				else if(value[length-1][len-1]>99)
			cout<<"0"<<value[length-1][len-1];
						else if(value[length-1][len-1]>9)
			cout<<"00"<<value[length-1][len-1];
						else
									cout<<"000"<<value[length-1][len-1];

		cout<<endl;
		
	}
}