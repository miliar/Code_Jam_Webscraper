#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(ll (i)=0;(i)<(n);(i)++)
#define dbg(args...) {debug,args; cerr << endl;}

#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define P1(a) (a).first
#define P2(a) (a).second
#define T1(a) (a).first
#define T2(a) (a).second.first
#define T3(a) (a).second.second
#define INF 1000000000
#define EPS 1e-8

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<int,pii> tiii;

class debu{
	public:
	template<class someClass>
	debu & operator,(someClass arg){
		cerr << arg << " ";
		return *this;
	}
} debug;


void init(){
    cout << setprecision(8)<< fixed;
}

ll N;
ll see[1005];
ll height[1005];
ll hidden[1005];

void solve(){
    memset(hidden,0,sizeof hidden);
    memset(see,0,sizeof see);
    memset(height,0,sizeof height);
    cin >> N;
    rep(i,N-1){
        cin >> see[i];
        see[i]--;
    }
    
    height[N-1]=INF;
    height[N]=INF;
    for(ll i=N-2;i>=0;i--){
        //dbg(i,see[i]);
        if (hidden[see[i]] || see[i]<=i) {
            cout << " Impossible";
            return ;
        }
        
        ll next,prev;
        for(next=see[i]+1;hidden[next];next++);
        for(prev=see[i]-1;hidden[prev];prev--);
        
        ll h1=height[see[i]]+((double)height[next]-height[see[i]])/((double)next-see[i])*(i-see[i]);
        ll h2;
        if (prev!=i){
            h2=height[see[i]]+((double)height[prev]-height[see[i]])/((double)prev-see[i])*(i-see[i]);
        }
        if (prev==i){
            height[i]=h1*1999/(2000);
        }else{
            height[i]=(h1+h2)/2;
        }
        
        for(ll k=i+1;k<see[i];k++) hidden[k]=1;
    }
    
    rep(i,N){
        cout << " " << height[i];
    }
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i << ":";
        solve();
        cout << "\n";
    }
    
    
    return 0;
}
