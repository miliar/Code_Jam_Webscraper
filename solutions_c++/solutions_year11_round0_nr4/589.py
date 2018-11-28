//      hello world


//DS includes
#include<bitset>
#include<complex>
#include<deque>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

//Other Includes
#include<algorithm>
#include<cassert>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iostream>
#include<sstream>

#define oo 			0xBADC0DE
#define s(n)			scanf("%d",&n)
#define sl(n) 			scanf("%lld",&n)
#define sf(n) 			scanf("%lf",&n)
#define fill(a,v) 		memset(a, v, sizeof a)
#define ull 			unsigned long long
#define ll 				long long
#define bitcount 		__builtin_popcount
#define all(x) 			x.begin(), x.end()
#define pb( z ) 		push_back( z )
#define gcd				__gcd

#define FOR(i,n) for (int i=0; i < (n); i++)

using namespace std;
const int mxn = 1024;
int a[mxn], n;
int vis[mxn], vid;
double dp[mxn];
bool visd[mxn];
double solve(int n) {
	if (n<=1)
		return 0;
	if (visd[n])
		return dp[n];
	//probability that element first element will be part of a cycle of length cycLen
	double ret = 1;
	for (int x=1; x < n; x++) {
		ret += solve(x)/x;
	}
	ret = ret*n/(n-1.0);
	visd[n] = 1;
	return dp[n]=ret;
}

double solveBF(int n) {
	if (n<=1)
		return 0;
	vector<int> a(n);
	
	for (int i=0; i < n; i++) {
		a[i] = i;
	}
	vector<int> count(n+1);
	do {
		vector<bool> vis(n);
		for (int i=0; i < n; i++) {
			if (vis[i]) 
				continue;
			int c = i;
			int len =0;
			while(!vis[c]) {
				vis[c]=1;
				c = a[c];
				len++;
			}
			count[ len ] ++;	
		}
	} while (next_permutation( all(a) ));
	for (int i=1; i <= n; i++) cout<< count[i] << " "; cout<<endl;
	return 0;
}

int main(int argc, char** argv) {
	//freopen("ip.txt", "r", stdin); 
	//freopen("D-small-attempt0.in", "r", stdin); freopen("D-small-attempt0.out", "w", stdout);
	//freopen("D-small-attempt1.in", "r", stdin); freopen("D-small-attempt1.out", "w", stdout);
	//freopen("D-small-attempt2.in", "r", stdin); freopen("D-small-attempt2.out", "w", stdout);
	//freopen("D-small-attempt3.in", "r", stdin); freopen("D-small-attempt3.out", "w", stdout);
	
	freopen("D-large.in", "r", stdin); freopen("D-large.out", "w", stdout);
	
	int runs;
	cin>>runs;
	for (int C=1; C<=runs; C++) {
		printf("Case #%d: ", C);
		cin>>n;
		for (int i=1; i <= n; i++) {
			cin>>a[i];
		}
		++vid;
		double ans = 0;
		for (int i=1; i <= n; i++)
		if (vis[i] != vid) {
			int c = i;
			int len = 0;
			while (vis[c] != vid) {
				vis[c] = vid;
				c = a[c];
				len++;
			} 
			ans += solve(len);
		}
		
		printf("%.10lf\n", ans);
	}
	return 0;
}
