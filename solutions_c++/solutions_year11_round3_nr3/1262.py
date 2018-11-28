#include <vector>
#include <list>

#include <deque>
#include <queue>
#include <stack>

#include <map>
#include <set>

#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <cstdio>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>

#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef pair<int, pair<int, int> > triple;

#define eps 1e-7
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define MP make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define tr(container, it) for(typeof((container).begin()) it = (container).begin(); it != (container).end(); it++)
#define MT(a,b,c) MP(a,MP(b,c))
int a[100];

ll gcd(ll a, ll b) {
	if (b == 0)
		return a;
	return gcd(b, a % b);
}
ll lcm(ll a, ll b) {
	return a * b / gcd(a, b);
}
int main() {
		freopen("C-small-attempt0.in", "r", stdin);
		freopen("C-small-attempt0.out", "w", stdout);
	int tests;
	scanf("%d\n", &tests);
	for (int test = 1; test <= tests; test++) {
		int n, l, h;
		scanf("%d %d %d\n", &n, &l, &h);
		REP(i,n) {
			scanf("%d ", &a[i]);
		}
		int res=-1;
		FOR(t,l,h+1)
		{
			bool ok=true;
			REP(i,n)
				if(!(t%a[i]==0||a[i]%t==0))
				{
					ok=false;
					break;
				}
			if(ok)
			{
				res=t;
				break;
			}
		}
		if(res==-1)
			printf("Case #%d: NO\n", test);
		else
			printf("Case #%d: %d\n", test,res);
	}

}
