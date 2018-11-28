
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

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void CMAX(T &a,T b){if(b>a) a=b;} 
template<class T> inline void CMIN(T &a,T b){if(b<a) a=b;}
#define FOR(a,b,c) for(a=b;a<c;++a)
#define REP(a,b) for(a=0;a<b;++a)

int X[10240];

int Y[10240];

int top;
int N;
int cnt[100100];
int main()
{
    //freopen("B_S0.in", "r", stdin);freopen("B_S0.out", "w", stdout);
    freopen("B-large.in", "r", stdin);freopen("B-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;

    scanf("%d", &T);
    while(T--)
    {
      memset(cnt, 0, sizeof(cnt));
	  top = 0;

       scanf("%d", &N);
		if(N == 0)
		{
			printf("Case #%d: %d\n", ++cs, 0);
			continue;
		}
	   REP(i, N)
	   {
		   scanf("%d", &j);
		   cnt[j]++;
	   }

	   int res = 10000;

	   FOR(i, 1, 10010)
	   {
		   if(cnt[i] < cnt[i-1])
		   {
			   int d = cnt[i-1] - cnt[i];
		       for(j = i - 1; cnt[j] >= d; --j)
			   {
				    cnt[j] -= d;
			   }
			   if(i - j - 1 < res) res = i - j - 1;
		   }
	   }
	   printf("Case #%d: %d\n", ++cs, res);
    }
	return 0;
}

