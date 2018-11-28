#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <algorithm>
//#include <sys/time.h>
using namespace std;
#define li        long long int
#define rep(i,to) for(li i=0;i<((li)(to));++i)
#define pb        push_back
#define sz(v)     ((li)(v).size())
#define bit(n)    (1ll<<(li)(n))
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define MP        make_pair
#define F         first
#define S         second



#define MAX 1050
li n, X, Y;
vector<pair<li, li> > r;
vector<pair<li, li> > ans;
set<pair<li, li> > used;
pair<li, li> tmp[MAX];

bool recur(li x, li y, li index)
{
	if(X < x + r[index].F || Y < y + r[index].F) return false;
	if(used.find(MP(x, y)) != used.end()) return false;
	used.insert(MP(x, y));
	li xx = x + r[index].F * 2;
	li yy = y + r[index].F * 2;
	bool found = false;
	rep(i, index){
		li LEFT  = max( x, ans[i].F - r[i].F);
		li RIGHT = min(xx, ans[i].F + r[i].F);
		li UPPER = min(yy, ans[i].S + r[i].F);
		li LOWER = max( y, ans[i].S - r[i].F);
		if(LEFT < RIGHT && LOWER < UPPER){
			found = true;
			bool flag = rand() % 2;
			if(flag) { if(recur(ans[i].F + r[i].F, y, index)) return true; } 
			if(recur(x, ans[i].S + r[i].F, index)) return true;
			if(!flag){ if(recur(ans[i].F + r[i].F, y, index)) return true; }
		}
	}
	if(found) return false;
	ans.pb(MP(x + r[index].F, y + r[index].F));
	return true;
}
		


int main()
{


	li T;
	cin >> T;
	rep(turn, T){
		cin >> n >> X >> Y;
		r = vector<pair<li, li> >(n);
		rep(i, n) cin >> r[i].F;
		rep(i, n) r[i].S = i;
		sort(all(r));
		reverse(all(r));
		while(true){
			bool ok = true;
			ans.clear();
			rep(i, n){
				used.clear();
				if(!recur(-r[i].F, -r[i].F, i)){
					ok = false;
					break;
				}
			}
			if(ok) break;
			rep(i, n) swap(r[i], r[rand() % (i + 1)]);
		}
		
		
		cout << "Case #" << turn + 1 << ":";
		rep(i, n) tmp[r[i].S] = ans[i];
		rep(i, n) printf(" %0.1lf %0.1lf", (double)tmp[i].F, (double)tmp[i].S);
//		rep(i, n) cout << " " << tmp[i].F << " " << tmp[i].S;
		cout << endl;
	}
}
