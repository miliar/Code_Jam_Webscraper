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
int nn, k;
void solve() {
	long long int i;
	long long n = (long long) nn;
	int c = 0;
	fr(i, n) 
		if(k&(1ll<<i))
			c++;
	
	if(c==n)
		printf("ON\n");
	else
		printf("OFF\n");
		
}
int main() {
	int t;
	scanf("%d", &t);
	int c = 0;
	while(t--) {
		c++;
		scanf("%d %d", &nn, &k);	
		printf("Case #%d: ", c);
		solve();
	}
}
