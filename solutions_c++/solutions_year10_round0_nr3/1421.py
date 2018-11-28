#include<iostream>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<set>
#include<fstream>
#include<algorithm>
#include<cstring>
#include<cassert> 
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;



#define debug(x) cout << #x << " = " << x << "\n";
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)
#define mem(a, n) memset(a, n, sizeof(a))
typedef vector<int> VI;
typedef long long LL;
typedef vector<string> VS;
typedef stringstream SS; 
int r, k, n;
long long int solve() {
	int a[n];
	int i;
	long long c = 0;
	fr(i, n) 
		scanf("%d", &a[i]);
	i = 0;
	while(r--) {
		int g = i;
		long long tmp = 0;
		while(tmp+a[i]<=k) {
			tmp += a[i];
			i++;
			if(i>=n) 
				i = 0;
			if(g==i)
				break;
		}
		c += tmp;	
				
	}
	return c;
}
int main() {
	int t;
	int c = 0;
	scanf("%d", &t);
	while(t--) {
		c++;
		scanf("%d %d %d", &r, &k, &n);
		printf("Case #%d: %lld\n", c, solve());	
			
	}
}
