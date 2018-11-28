/*
 TASK:
 LANG: C++
 */
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>
#include <valarray>
//#include "vc.h"
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

template<class key>
struct hashtemp {

	enum {
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};

using namespace std;
#ifndef M_PI
const long double M_PI=acos((long double)-1);
#endif
#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO = 0;
const long double INF = 1 / ZERO, EPSILON = 1e-12;
#define all(c) (c).begin(),(c).end()
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
#define let(x,y) __typeof(y) x(y)

#define rrep(i,n) for(int  i=((int)n)-1;i>=0;--i)
#define rall(c) (c).rbegin(),(c).rend()
#define rrep2(i,a,b) for(int i=(a);i>=((int)b);--i)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define rep2d(i, j, v) rep(i, sz(v)) rep(j, sz(v[i]))
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
char arr[50][51];
char arr2[50][51];

int di[] = { 1, 0, 1, 1 };
int dj[] = { 0, 1, 1, -1 };
int main() {
#ifndef ONLINE_JUDGE
	//freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-large.in","rt",stdin);
	//freopen("1.in", "rt", stdin);
	freopen("1.out", "wt", stdout);
#endif

	int T;
	cin >> T;
	rep(t,T) {
		printf("Case #%d: ", t + 1);
		//cout<<"Case #"<<t+1<<": ";

		int R, C, K,N;
		cin >> N >> K;
		R = C = N;
		rep(i,R) {
			cin >> arr[i];
		}
		memset(arr2,'.',sizeof(arr2));


		rrep(i,R)
		rrep(j,C)
		{

					if (arr[i][j] != '.') {
						int k = 0;
						while (j >= 0  )
						{
							if(arr[i][j] != '.')
								arr2[k++][i] = arr[i][j];
							j--;
						}
						cout<<"";
						break;
					}

			}
		bool b = 0;
		bool r = 0;
		rep(i,C)
			rep(j,R)
				if (arr2[i][j] == 'B' || arr2[i][j] == 'R') {

					char c=arr2[i][j];
					rep(k,4)
					{
						int cnt=0;
						int ni = i, nj = j;
						while (ni < R && nj < R && nj >= 0 && ni >= 0
								&& arr2[ni][nj] == c)
						{
							ni += di[k];
							nj += dj[k];
							cnt++;
						}
						if (cnt >=K)
							(c == 'B' ? b : r) = 1;
					}
				}
		if(b&&r)
				printf("Both\n");
		else if(r)
				printf("Red\n");
		else if(b)
				printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}
