#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <ctime>
#include <utility>
#include <stdexcept>

using namespace std;

#define inf (1<<30)
#define PB push_back
#define mset(x,a) memset(x,(a),sizeof(x))
#define SIZE(X) ((int)X.size())
#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define rg(x,y) (x=x>y?x:y)
typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<string> VS;
typedef long long LL;
typedef unsigned long long uLL;
#define twoL(X) (((LL)(1))<<(X))
const double PI=acos(-1.0);
const double eps=1e-11;
template <class T> T sqr(T x) {return x*x;}
template <class T> T gcd(T a, T b) {if(a<0) return (gcd(-a,b)); if(b<0) return (gcd(a,-b)); return (b==0)?a:gcd(b,a%b);}
template <class T> T lcm(T a, T b) {return a*b/gcd(a,b);}
LL toLL(string s) { istringstream sin(s); LL t; sin>>t; return t;}
int toInt(string s) {istringstream sin(s); int t; sin>>t; return t;}
string toString(LL v) {ostringstream sout; sout<<v; return sout.str();}
string toString(int v) {ostringstream sout; sout<<v; return sout.str();}
#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) ((x).begin(), (x).end())
#define cross(a, b, c)  ((c).x-(a).x)*((b).y-(a).y)-((b).x-(a).x)*((c).y-(a).y)
#define sq_dist(p, q) ((p).x-(q).x)*((p).x-(q).x)+((p).y-(q).y)*((p).y-(q).y)
#define FF(i,n) for(int i = 0; i < n; ++i)

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);//文件输入
    freopen("C-small-attempt0.out", "w", stdout);//文件输出
	int T, cnt = 0, sum, cnd;
	scanf("%d", &T);
	while( T-- ) {
		int R, k, N;
		scanf("%d%d%d", &R, &k, &N);
		queue<int> q;
		for( int i = 0; i < N; ++i ) {
		    int temp;
			scanf("%d", &temp);
			q.push(temp);
		}
		int ans = 0;
		for( int i = 0; i < R; ++i ) {
			cnd = 0, sum = 0;
			while( cnd < N && sum < k ) {
				//cout << cnd << " " << N << " " << sum << " " << k << endl;
			    int cur = q.front();
				if( sum+cur <= k ) {
					sum += cur;
					q.pop();
					q.push(cur);
					cnd++;
					//cout << sum << endl;
				}
				else {
					break;
				}
			}
			ans += sum;
			//cout << "ok " << ans << endl;
		}
		printf("Case #%d: %d\n", ++cnt, ans);
	}
	return 0;
}
