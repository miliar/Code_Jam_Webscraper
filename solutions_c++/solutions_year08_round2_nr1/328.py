//A. Crop Triangles .cpp 

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

int64 n,a,b,c,d;
int64 xx,yy,mod;
int64 res;

int64 cal(int64 n,int64 m)
{
	if(n < m) return 0;
	int64 ans = 1;
	FOR(i,0,m)
	{
		ans = ans * (n - i)/(i + 1);
	}
	return ans;
}
void solve()
{
	int cnt[3][3];
	memset(cnt,0,sizeof(cnt));
	int64 x = xx;
	int64 y = yy;
	cnt[x%3][y%3]++;
	FOR(i,1,n)
	{
		x = (a * x + b) % mod;
		y = (c * y + d) % mod;
		cnt[x%3][y%3]++;
	}
	res = 0;
	/*res += cal(cnt[0][0],3);
	res += cal(cnt[0][1],3);
	res += cal(cnt[0][1],2) * cal(cnt[1][0],1);
	res += cal(cnt[0][1],1) * cal(cnt[1][0],2);
	res += cal(cnt[1][1],3);*/
	RE(i1,3)RE(i2,3)FOR(j1,0,3)FOR(j2,0,3)FOR(k1,0,3)FOR(k2,0,3)
	{
		if(((i1 + j1 + k1) % 3) == 0 && ((i2 + j2 + k2) % 3 == 0))
		{
			int64 t1 = cnt[i1][i2],t2 = cnt[j1][j2],t3 = cnt[k1][k2];
			int64 r1 = 0,r2=0,r3 = 0;
			r1 = max(0,cnt[i1][i2]);
			--cnt[i1][i2];
			r2 = max(0,cnt[j1][j2]);
			--cnt[j1][j2];
			r3 = max(0,cnt[k1][k2]);
			cnt[i1][i2] = t1;
			cnt[j1][j2] = t2;
			res += r1 * r2 * r3;
		}
	}
	res /= 6;
	/*res = 0;
	vector <int64> vx;
	vector <int64> vy;
	vx.push_back(xx);
	vy.push_back(yy);
	int64 x = xx;
	int64 y = yy;
	FOR(i,1,n)
	{
		x = (a * x + b) % mod;
		y = (c * y + d) % mod;
		vx.push_back(x);
		vy.push_back(y);
	}
	RE(i,n)FOR(j,i + 1,n) FOR(k,j + 1,n)
	{
		if((vx[i] + vx[j] + vx[k])%3 == 0)
		{
			int64 tx = (vx[i] + vx[j] + vx[k])/3;
			if((vy[i] + vy[j] + vy[k]) % 3 == 0)
			{
				int64 ty = (vy[i] + vy[j] + vy[k])/3;
				++res;
			}
		}
	}*/
}
int main() 
{

	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);

	int ncase;
	cin >> ncase;
	FOR(i,1,ncase + 1)
	{
		cin >> n >> a >> b >> c >> d >> xx >> yy >> mod;
		cout << "Case #" << i << ": ";
		solve();
		cout << res << endl;
	}
	return 0;
}
