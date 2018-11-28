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
#define INF 999999999

#define N 10000 + 100

struct NODE
{
	int g;
	int c;
	int val;
}node[N];


int dp[N][2];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int C;
	int p;
	int ans;
	int i,j;
	int m,v;
	int g,c;
	int val;
	while (scanf("%d",&C) != EOF) {

		for (p = 1; p <= C; p ++) {
			ans = 0;
			scanf("%d%d",&m,&v);

			for (i = 1; i <= (m - 1)/2; i ++) {
				scanf("%d%d",&g,&c);
				node[i].g = g;
				node[i].c = c;
			}
			for (i = 1; i <= m; i ++) {
				for (j = 0; j < 2; j ++) {
					dp[i][j] = INF;
				}
			}
			//memset(dp,100,sizeof(dp));
			for (i = (m-1)/2 + 1; i <= m; i ++) {
				scanf("%d",&val);
				node[i].val = val;
				dp[i][val] = 0;
			}

			

			for (i = m; i >= 1; i -= 2) {
				if (i == 7)
					i = i;

				// i i-1;
				// fart = (i-1)/2
				int fart = (i-1)/2;
			//	int val_and = node[i].val & node[i-1].val;
			//	int val_or = node[i].val | node[i-1].val;

				if (node[fart].g == 1) { // and
					if (node[fart].c == 1) { // ¿Échange
						if (dp[i][0] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][0]);
						} 
						if (dp[i][0] != INF && dp[i-1][1] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][1]);
						} 
						if (dp[i][1] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][1]+dp[i-1][0]);
						} 
						if (dp[i][1] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][1]);
						} 

						// change or

						if (dp[i][0] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][0]+1);
						} 
						if (dp[i][0] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][0]+dp[i-1][1]+1);
						} 
						if (dp[i][1] != INF && dp[i-1][0] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][0]+1);
						} 
						if (dp[i][1] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][1]+1);
						} 
					} else {
						if (dp[i][0] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][0]);
						} 
						if (dp[i][0] != INF && dp[i-1][1] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][1]);
						} 
						if (dp[i][1] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][1]+dp[i-1][0]);
						} 
						if (dp[i][1] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][1]);
						} 
					}
				} else {
					if (node[fart].c == 1) { // ¿Échange
						if (dp[i][0] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][0]);
						} 
						if (dp[i][0] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][0]+dp[i-1][1]);
						} 
						if (dp[i][1] != INF && dp[i-1][0] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][0]);
						} 
						if (dp[i][1] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][1]);
						} 

						// change and

						if (dp[i][0] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][0]+1);
						} 
						if (dp[i][0] != INF && dp[i-1][1] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][1]+1);
						} 
						if (dp[i][1] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][1]+dp[i-1][0]+1);
						} 
						if (dp[i][1] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][1]+1);
						} 
					} else {
						if (dp[i][0] != INF && dp[i-1][0] != INF) {
							dp[fart][0] = min(dp[fart][0],dp[i][0]+dp[i-1][0]);
						} 
						if (dp[i][0] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][0]+dp[i-1][1]);
						} 
						if (dp[i][1] != INF && dp[i-1][0] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][0]);
						} 
						if (dp[i][1] != INF && dp[i-1][1] != INF) {
							dp[fart][1] = min(dp[fart][1],dp[i][1]+dp[i-1][1]);
						} 
					}

				}
			}
			if (dp[1][v] == INF) {
				printf("Case #%d: IMPOSSIBLE\n",p);

			} else {
				printf("Case #%d: %d\n",p,dp[1][v]);
			}
		}

	}
	return 0;
}
