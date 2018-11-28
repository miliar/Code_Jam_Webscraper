/*

 E-Mail : ahmed.aly.tc@gmail.com

 Just For You :)

 */

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;


int N;
int n;
int D,I,M;
int nums[100];
int dp[100][256][2];
int calc(int cur,int prev,int fst){
	if(cur==n)
		return 0;
	if(dp[cur][prev][fst]!=-1)
		return dp[cur][prev][fst];
	int ret=oo;
	if(fst){
		ret=calc(cur+1,nums[cur],0);
		ret=min(ret,calc(cur+1,0,1)+D);
		rep(i,256)
			ret=min(ret,calc(cur+1,i,0)+abs(i-nums[cur]));
	}else{
		if(abs(nums[cur]-prev)<=M)
			ret=calc(cur+1,nums[cur],0);
		ret=min(ret,calc(cur+1,prev,0)+D);
		rep(i,256)
			if(abs(i-prev)<=M)
				ret=min(ret,calc(cur+1,i,0)+abs(i-nums[cur]));
		if(abs(nums[cur]-prev)>M && M!=0){
			int is=abs(nums[cur]-prev)/M;
			if(abs(nums[cur]-prev)%M==0)
				is--;
			ret=min(ret,is*I+calc(cur+1,nums[cur],0));
		}
	}
	return dp[cur][prev][fst]=ret;
}

#define SMALL
//#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

	cin >> N;
	rep2(nn,1,N+1) {
		cin>>D>>I>>M>>n;
		rep(i,n)
			cin>>nums[i];
		mem(dp,-1);
		int ret=calc(0,0,1);
		printf("Case #%d: %d\n", nn,ret);
	}
	return 0;
}
