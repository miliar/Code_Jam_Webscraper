#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
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

using namespace std;

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

/*
#define SIZE(X) ((int)X.size())
#define LENGTH(X) ((int)X.length())
#define MP(A,B) make_pair(A,B)
typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define towL(X) (((int64)(1))<<(X))
#define contain(S,X) ((S&two(X))>0)
#define containL(S,X) ((S&towL(X))>0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> void checkmin(T &a,T b) {if (b<a) a=b;}
template<class T> void checkmax(T &a,T b) {if (b>a) a=b;}
template<class T> T sqr(T x) {return x*x;}
int countbit(int n) {return (n==0)?0:(1+countbit(n&(n-1)));}
int lowbit(int n) {return (n^(n-1))&n;}
typedef pair<int,int> ipair;
template<class T> void out(T A[],int n) { for (int i=0; i<n; i++) cout<<A[i]<<" "; cout<<endl;}
template<class T> void out(vector<T> A,int n=-1) { if (n==-1) n=A.size();  for (int i=0; i<n; i++) cout<<A[i]<<" "; cout<<endl;}
template<class T> T gcd(T a,T b){ if (a<0) return gcd(-a,b); if (b<0) return gcd(a,-b); return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(T a,T b){ return a*(b/gcd(a,b));}


*/

#define N 101
#define MOD 10007

int dp[N][N];
bool f[N][N];

int main() {

	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);

	//freopen("D-large.in","r",stdin);
	//freopen("D-large.out","w",stdout);

	int i,j,h,w,r;
	int x,y;

	int C;
	int p;
	int ans;

	while (scanf("%d", &C) != EOF) {

		for (p = 1; p <= C; p ++) {

			memset(f,false,sizeof(f));

			scanf("%d%d",&h,&w);
			memset(dp,0,sizeof(dp));
			dp[1][1] = 1;
			scanf("%d",&r);
			for (i = 0; i < r; i ++) {
				scanf("%d%d",&x,&y);
				f[x][y] = true;
			}
			for (i = 1; i <= h; i ++) {
				for (j = 1; j <= w; j ++) {
					if (i + 2 <= h && j + 1 <= w) {
						if (!f[i+2][j+1]) {

						dp[i+2][j+1] += dp[i][j];
						dp[i+2][j+1] %= MOD;
						}
					}
					if (i + 1 <= h && j + 2 <= w) {
						if (!f[i+1][j+2]) {
						dp[i+1][j+2] += dp[i][j];
						dp[i+1][j+2] %= MOD;
						}
					}
				}
			}
		/*	for (i = 1;  i <= h; i ++) {
				for (j = 1; j <= w; j ++) {
					printf("%d ",dp[i][j]);
				}
				printf("\n");
			}*/


	
			printf("Case #%d: %d\n", p,dp[h][w]);
		}

	}
	return 0;
}
