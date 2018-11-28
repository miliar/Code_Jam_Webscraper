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


struct Point
{
	int x,y;
};
int mul(Point p0,Point p1,Point p2) { 
	return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y); 
}

int main()
{

	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int C;
	int p;
	int n,m,A;
	int i,j,x,y;
	long long int ans;
	while (scanf("%d",&C) != EOF) {

		for (p = 1; p <= C; p ++) {

		scanf("%d%d%d",&n,&m,&A);

		Point a,b,c;
		a.x = 0;
		a.y = 0;

		bool fif = false;

		for (i = 0; i <= n; i ++) {
			for (j = 0; j <= m; j ++) {
				for (x = 0; x <= n; x ++) {
					for (y = 0; y <= m; y ++) {

						b.x = i;
						b.y = j;
						c.x = x;
						c.y = y;
						if (mul(a,b,c) == A) {
							fif = true;
							goto OUT;
						}
					}
				}
			}
		}
OUT:
		if (fif) {

			printf("Case #%d: %d %d %d %d %d %d\n",p,a.x,a.y,b.x,b.y,c.x,c.y);
		} else {
			printf("Case #%d: IMPOSSIBLE\n",p);
		}
		}
	

	}
	return 0;
}
