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

using namespace std;

#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int (i)=0;(i)<(n);(i)++)
#define dbg(args...) {debug,args; cerr << endl;}

#define mp make_pair
#define mt(a,b,c) mp(a,mp(b,c))
#define P1(a) (a).first
#define P2(a) (a).second
#define T1(a) (a).first
#define T2(a) (a).second.first
#define T3(a) (a).second.second
#define INF 2000000000
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

vector<pii> v;
vector<int> m;
int N,D;

string solve(int testnr){
    v.clear();
    m.clear();
    pii p;
    cin >> N;
    rep(i,N){
        cin >> P1(p) >> P2(p);
        v.push_back(p);
    }
    cin >> D;
    v.push_back(mp(D,0));
    m.resize(N+1,-INF);
    m[0]=P1(v[0]);
    rep(i,N){
        if (m[i]==-INF) return "NO";
        for(int j=i+1;j<=N;j++){
            if (m[i]+P1(v[i])>=P1(v[j])){
                m[j]=max(m[j],min( P1(v[j])-P1(v[i]),P2(v[j]) ));
            }
            else break;
        }
    }
    if (m[N]>=0) return "YES";
    return "NO";
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i << ": " << solve(i) << "\n";
   //     for(int j=0;j<=N;j++) dbg(m[j]);
    }
    
    return 0;
}
