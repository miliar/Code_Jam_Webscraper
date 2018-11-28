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
	scanf("%d",&N);
	queue<char> Q;
	queue<int> qO,qB;
	REP(i,N){
		char a;int b;
		scanf(" %c %d",&a,&b);
		Q.push(a);
		if(a == 'O') qO.push(b);
		else         qB.push(b);
	}
	int ans = 1;
	int tO = 1,tB = 1;
	while(!Q.empty()){
		bool Opush = 0;
		// printf("time = %d : ",ans);
		if(tO < qO.front()){
			tO++;
			// printf("Orange goto %d",tO);
		} else if(tO > qO.front()){
			tO--;
			// printf("Orange goto %d",tO);
		} else{
			if(Q.front() == 'O'){
				Q.pop();
				qO.pop();
				// printf("Orange Push %d",tO);
				Opush = 1;
			} else {
				// printf("Orange stay %d",tO);
			}
		}
		// printf(" : ");
		if(tB < qB.front()){
			tB++;
			// printf("Blue goto %d",tB);
		} else if(tB > qB.front()){
			tB--;
			// printf("Blue goto %d",tB);
		} else {
			if(Q.front() == 'B' && !Opush){
				Q.pop();
				qB.pop();
				// printf("Blue Push %d",tB);
			} else {
				// printf("Blue stay %d",tB);
			}
		}
		// puts("");
		ans++;
	}
	printf("Case #%d: %d\n",tc,ans-1);
}

int main(){
	int tc;scanf("%d",&tc);
	int x = tc;
	while(tc--){
		solve(x - tc);
	}
	return 0;
}
