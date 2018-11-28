#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <deque>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <queue>
#include <cstring>
#include <stack>
#include <assert.h>
using namespace std;

#define IT(c) typeof((c).begin())

#define For(i, a, b) for(int (i) =  int(a); i < int(b); ++i)
#define rep(x, n) For(x,0,n)
#define foreach(i, c) for(IT(c) i = (c).begin(); i != (c).end(); ++i)

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef long long ll;

int main(){
int np;cin>>np;
rep(tp,np){
	map<int,int> D;
	int n; cin>>n;
	vector<int> v;
	int sum = 0;
	int asum = 0;
	rep(i,n){
		int t;cin>>t;
		v.pb(t);
		sum ^= t;
		asum += t;
	}
	sort(v.begin(), v.end());
	printf("Case #%d: ", tp+1);
	if(sum) printf("NO\n");
	else
		printf("%d\n", asum - v[0]);
}
}
