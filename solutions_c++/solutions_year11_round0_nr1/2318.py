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
	queue<pair<int,int> > st[2];
	int tn; char tc;
	int n; cin>>n;
	rep(t,n){
		cin>>tc>>tn;
		int idx = 1;
		if(tc=='O') idx = 0;
		st[idx].push(mp(t,tn));
	}
	int p[2] = {1,1};
	int cost=0;
	while(!(st[0].empty() && st[1].empty())){
		bool delta[2] = {false, false};
		rep(k,2) if(!st[k].empty()){
			if(p[k] < st[k].front().S){
				p[k]++;
				delta[k] = true;
			} else if(p[k] > st[k].front().S){
				p[k]--;
				delta[k] = true;
			}
		}
		bool push=false;
		rep(k,2) if(!st[k].empty() && !push) if(st[1-k].empty() || st[k].front().F < st[1-k].front().F){
			if(!delta[k]){
				st[k].pop();
				push = true;
			}
		}
		cost++;
	}
	printf("Case #%d: %d\n", tp+1, cost);
}
}
