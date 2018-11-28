#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <deque>
#include <stack>
#include <cctype>
#include "assert.h"
#include <cstdlib>
#include <iostream>

#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-9
using namespace std;
typedef long long ll;

pair<int,int> R[2001];
int mp[2001];

struct elem{
	ll lft;
	ll rgt;
	ll tp;
	bool lst;
	elem(int a, int b, int c, bool d) : lft(a), rgt(b), tp(c), lst(d)  {
	};
};

ll X[2001];
ll Y[2001];

int main() {
	int T;
	scanf("%d",&T);
	FR(i,T) {
		cout << "Case #" << i+1 << ": ";
		int N, W,L;
		cin >> N >> W >> L;
		FR(i,N) {
			cin >> R[i].first;
		}
		FR(i,N) {
			R[i].second = i;
		}
		
		sort(&R[0],&R[N]);
		FR(i,N) {
			mp[R[i].second]=i;
		}
		
		int idx = N-1;
		deque<elem> que;
		que.push_back(elem(-R[idx].first,W+R[idx].first,-R[idx].first, true));
		
		while(!que.empty()) {
			if(idx==-1) break;
			elem el = que.front();
			que.pop_front();
			ll lft_b = el.lft;
			ll rgt_b = el.rgt;
			bool created=false;
			for(;;) {
				ll cnt_x = max(0LL,lft_b+R[idx].first);
				ll cnt_y = max(0LL,el.tp+R[idx].first);			
				if(cnt_x>W||cnt_y > L || (!el.lst&&cnt_x+R[idx].first > rgt_b)) {
					break;
				}
				X[idx] = cnt_x;
				Y[idx] = cnt_y;
				lft_b=cnt_x+R[idx].first;
				if(created&&el.lst) {
					elem el2=que.back();
					assert(el2.lst==true);
					que.pop_back();
					el2.lst=false;
					que.push_back(el2);
				}
				que.push_back(elem(cnt_x-R[idx].first,cnt_x+R[idx].first,cnt_y+R[idx].first,el.lst));				
				created=true;
				idx--;	
				if(idx==-1) break;
			}
			
			
		}
		
		if(idx>=0) assert(false);
		
		FR(i,N) {
			cout << X[mp[i]] << " " << Y[mp[i]] << " ";
		}
		cout << endl;
	}
	
	
}