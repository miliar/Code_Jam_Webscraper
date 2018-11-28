#include <iostream>
using namespace std;
#include <cstdio>
#include <algorithm>
#include <deque>
#include <map>
#include <set>
typedef pair<int,int> pii;
typedef long long ll;
#include <vector>
typedef vector<int> vi;
typedef vector<ll> vll;
#include <queue>
#include <stack>
#define For(i,a,b) for(int i=(a);i<(b);++i)

#define ForI(i,a,b) for(int i=(a);i<=(b);++i)
#define ForAll(it,set) for(typeof(set.begin()) it = set.begin(); it!=set.end(); ++it)

const ll oo = 9999999999999999LL;
typedef stack<int> si;
typedef queue<int> qi;


int main(){
	int t;
	cin>>t;
	ForI(tt,1,t){
		ll c,d;
		cin>>c>>d;
		//multiply all by two?
		d *= 2;
		vll vals;
		
		For(i,0,c){
			int x,n;
			cin>>x>>n;
			x *= 2;
			For(i,0,n)
				vals.push_back(x);
		}
		sort(vals.begin(),vals.end());
		ll high = d * vals.size();
		ll low = 0;
		const ll len = vals.size();
		while(low <= high){
			ll mid = (low+high)/2;
			ll leftmost = -oo;
			bool possible = true;
			For(i,0,len){
				ll next = max(leftmost + d, vals[i] - mid);
				if(next > vals[i] + mid){
					possible = false;
					break;
				}
				leftmost = next;
				
			}
			if(possible)
				high = mid - 1;
			else
				low = mid+1;	
		}
		printf("Case #%d: %.1lf\n", tt,double(low)/2);	
	
	}

	return 0;
}
