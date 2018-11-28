#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif

#define pb push_back
#define mp make_pair
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<=int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;


const int INF = (int) 1e9;
const long long INF64 = (long long) 1e18;
const long double eps = 1e-9;
const long double pi = 3.14159265358979323846;

int main(){
#ifndef ONLINE_JUDGE
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif
    int cnt;
	scanf("%d", &cnt);
	forn(testcase,cnt){
		int n,s,p;
		scanf("%d%d%d", &n, &s, &p);
		vector <int> t(n);
		forn(i,n)
			scanf("%d", &t[i]);
		int ans = 0;
		forn(i,n){
			vector <int> nums(3);
			forn(j,3)
				nums[j] = t[i]/3;
			int d = t[i] % 3;
			forn(j,d)
				nums[j]++;
			if (nums[0]>=p)
				ans++;
			else{
				nums[0]++; nums[1]--;
				bool ok = true;
				forn(j,3){
					ok = ok && (abs(nums[j]-nums[(j+1)%3])<3);
					ok = ok && (nums[j]>=0 && nums[j]<=10);
				}
				ok = ok && nums[0]>=p;
				if (s!=0 && ok){
					s--;
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", testcase+1, ans);
	}
    return 0;
}
