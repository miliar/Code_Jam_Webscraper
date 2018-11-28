#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <cstring>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) (a.begin(),a.end())
#define rall(a) (a.rbegin(),a.rend())
#define INF (int)1e9
#define EPS (double)1e-9

typedef unsigned long long ULL;
typedef long long LL;
typedef set <int> si;
typedef pair< int,int > ii;
typedef pair< int, ii > pi;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

LL gcd(LL a, LL b) {
	if (b == 0) return a;
	return gcd(b, a%b);
}

int main() {
	int T = GI;
	FOR(t,1,T+1) {
		int N = GI;
		int L = GL, H = GL;

		cout << "Case #" << t << ": ";
		/*
		if (L == 1) {
			cout << 1 << endl;
			continue;
		}
		*/
//		LL gd, prod = 1;
		vector<int> ip(N);
		REP(i,N) {
			ip[i] = GI;
		//	if (i == 0) gd = ip[i];
		//	else gd = gcd(gd, ip[i]);
		}
		/*
		bool flag = true;
		REP(i,N) {
			if (i == 0) prod = ip[i]/gd;
			else prod *= ip[i];
			if (prod > H) {
				flag = false;
				break;
			}
		}

		LL quo, ans;
		if (flag) {
			quo = (L-1)/prod;
			ans = (quo+1)*prod;
			if (ans <= H) cout << ans << endl;
			else cout << "NO" << endl;
		}
		else {
			cout << "NO" << endl;
		}
		*/

		bool flag;
		int ans = -1;
		FOR(z,L,H+1) {
			flag = true;
			REP(i,N) {
				if (ip[i] != 0 && ip[i]%z != 0 && z%ip[i] != 0) {
					flag = false;
					break;
				}
			}
	
			if (flag == true) {
				ans = z;
				break;
			}
		}

		if (ans == -1) cout << "NO" << endl;
		else cout << ans << endl;
	}	
	return 0;
}
