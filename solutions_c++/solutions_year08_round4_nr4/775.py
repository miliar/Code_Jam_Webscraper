//D. PermRLE.cpp 

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
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
#include <algorithm>

using namespace std;

const double pi=acos(-1.0);
const double eps=1e-11;

#define SZ(X) ((int)(X.size()))
#define MP(A,B) make_pair(A,B)
#define FOR(i,b,e) for(int i = b;i < e;++i)
#define RE(i,n) FOR(i,0,n)

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))>0)
#define containL(S,X) (((S)&twoL(X))>0)
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;} 
int64 toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;} 
string toString(int64 v){ostringstream sout;sout<<v;return sout.str();} 
string toString(int v){ostringstream sout;sout<<v;return sout.str();} 

template<class T> inline T countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}
template<class T> inline T sqr(T x){return x * x;}
template<class T> inline T gcd(T a,T b){if(a < 0) return gcd(-a,b); if(b < 0) return gcd(a,-b); return (b == 0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b){return a*(b/gcd(a,b));}
template<class T> void out(T A[],int n){for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}
template<class T> void out(vector<T> A,int n = -1){if(n==-1) n = A.size();for(int i = 0;i < n;++i) cout << A[i] << " ";cout << endl;}

const int INF = 1000000;
int k;
string sourcestr;
int ans;

int getcost(string str)
{
	int res = 1;
	RE(i,SZ(str) - 1)
	{
		if(str[i] != str[i + 1]) ++res;
	}
	return res;
}

string ch(vector<int> & vi)
{
	string str = sourcestr;
	for(int i = 0;i * k < SZ(sourcestr);++i)
	{
		RE(j,k)
		{
			str[i * k + j] = sourcestr[i * k + vi[j]]; 
		}
	}
	return str;
}
void solve()
{
	ans = INF;
	vector<int> vi;
	RE(i,k) vi.push_back(i);
	do
	{
		string str = ch(vi);
		int tmp = getcost(str);
		if(tmp < ans)
			ans = tmp;
	}while(next_permutation(vi.begin(),vi.end()));
}
int main() 
{
	//freopen("in.txt","r",stdin);

	//freopen("D-small-attempt0.in","r",stdin);
	//freopen("D-small-attempt0.out","w",stdout);

	/*freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);*/

	int ncase;
	cin >> ncase;
	FOR(i,1,ncase + 1)
	{

		cout << "Case #" << i << ": ";
		cin >> k >> sourcestr;
		solve();
		cout << ans << endl;
	}

	return 0;
}