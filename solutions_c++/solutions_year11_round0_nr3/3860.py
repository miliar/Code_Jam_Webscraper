/*  
	NAME:
	PROG:
	LANG:C++
*/

#define REP(_i_,_a_) for(unsigned int _i_ = 0,_X_ = _a_;_i_ < _X_;_i_++)
#define FOR(_i_,_a_,_b_) for(int _i_ = _a_,_X_ = _b_;_i_ <= _X_;_i_++)
#define FORD(_i_,_a_,_b_) for(int _i_ = _a_,_X_ = _b_;_i_ >= _X_;_i_--)
#define FE(_i_,_a_) for(__typeof(_a_.begin()) _i_ = _a_.begin();_i_ != _a_.end();_i_++)
#define LOOP for(;;)

#define iofile(_a_,_b_) freopen(_a_,"r",stdin);freopen(_b_,"w",stdout)
#define ioclose fclose(stdin);fclose(stdout)
#define isOn(_x_,_i_) (bool)((1<<_i_)&_x_)

#define mp make_pair
#define pb push_back
#define fi first
#define se second

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cstring>

#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <list>
#include <algorithm>
#include <utility>
#include <iostream>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;

void solve(int tc){
	int N;
	vector<int> X;
	scanf("%d",&N);
	REP(i,N){
		int x;scanf("%d",&x);
		X.pb(x);
	}
	int ans = -1;
	FOR(x,1,(1<<N)-2){
		int asli1 = 0,asli2 = 0;
		int bodo1 = 0,bodo2 = 0;
		REP(i,N){
			if(isOn(x,i)){
				asli1 += X[i];
				bodo1 ^= X[i];
			} else {
				asli2 += X[i];
				bodo2 ^= X[i];
			}
		}
		if(bodo1 == bodo2){
			ans = max(ans,max(asli1,asli2));
		}
	}
	printf("Case #%d: ",tc);
	if(ans == -1) printf("NO\n");
	else          printf("%d\n",ans);
}

int main(){
	int tc;scanf("%d",&tc);
	int x = tc;
	while(tc--) solve(x - tc);
	return 0;
}
