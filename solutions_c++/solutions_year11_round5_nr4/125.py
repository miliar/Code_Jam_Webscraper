
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
typedef long long LL;
const LL MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))
#define FOR(a,b,c) for(a=b;a<c;++a)
#define REP(a,b) for(a=0;a<b;++a)

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void CMAX(T &a,T b){if(b>a) a=b;} 
template<class T> inline void CMIN(T &a,T b){if(b<a) a=b;}

char S[128];
int N;
LL val;
LL res;
#define eps 1e-9
bool P(LL x)
{
	LL y = sqrt(x*1.0) + eps;

	return y * y == x;
}
void dfs(int p, LL v)
{
	if(p == N)
	{
	    if(P(v))
		{
			res = v;
			
		}
		return;
	}
	if(S[p] == '0')
	{
	    dfs(p+1, v*2);
	}
	else if(S[p] == '1')
	{
		dfs(p+1, v*2+1);
	}
	else
	{
		dfs(p+1,v*2);
		dfs(p+1,v*2+1);
	}

}
int main()
{
    freopen("D_S0.in", "r", stdin);freopen("D_S0.out", "w", stdout);
    //freopen("D-large.in", "r", stdin);freopen("D-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;

    scanf("%d", &T);
    while(T--)
    {
	   scanf("%s", S);
	   N = strlen(S);
	   dfs(0, 0);
	   int R[128];
	   for(i = 0; res; i++)
	   {
		   R[i] = res % 2;
		   res /= 2;
	   }
       printf("Case #%d: ", ++cs);
	   while(i--)
	   {
			printf("%d", R[i]);
	   }
	   printf("\n");
    }
	return 0;
}

