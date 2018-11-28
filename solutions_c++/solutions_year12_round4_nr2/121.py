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
#define INF 1e20
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

vector<pii> r;
vector<pii> bounds;
vector<tiii> answer;
int N,W,L;

void solve(){
    r.clear();
    answer.clear();
    cin >> N >> W >> L;
    r.resize(N);
    rep(i,N){
        cin >> P1(r[i]);
        P2(r[i])=i;
    }
    sort(r.rbegin(),r.rend());
    
    bounds.clear(); //(x,y) = up to x, blocked till y
    int x=0,y=0;
    bool placed;
    rep(i,N){
    
        placed=false;
        for(int j=0;j<bounds.size();j++){
            if (P2(bounds[j])+P1(r[i])<=L){
                y=P2(bounds[j])+P1(r[i]);
                if (j==0) x=0; else x=P1(bounds[j-1])+P1(r[i]);
                for(int k=0;k<j;k++){
                    P2(bounds[k])=max(P2(bounds[k]),y+P1(r[i]));
                }
                bounds.insert(bounds.begin()+j, mp(x+P1(r[i]),y+P1(r[i])) );
                int k=j+1;
                while (k<bounds.size() && P1(bounds[k])<=x+P1(r[i])) k++;
                if (k<bounds.size()){
                    bounds.erase(bounds.begin()+j+1,bounds.begin()+k);
                }else{
                    bounds.erase(bounds.begin()+j+1,bounds.end());
                }
                placed=true;
                break;
            }
        }
    
        if (bounds.empty()){
            y=x=0;
            bounds.push_back(mp(P1(r[i]),P1(r[i])));
            placed=true;
     //       cout << "Leer" << endl;
        }
        if (!placed){
            y=0;
            x=P1(bounds.back())+P1(r[i]);
            bounds.push_back(mp(x+P1(r[i]),y+P1(r[i])));
   //         cout << "Blub" << endl;
    //        dbg(i,x,y);
        }
    
        answer.push_back(mt(P2(r[i]),x,y));
      //  dbg(P2(r[i]),x,y,P1(r[i]));
      //  rep(i,N){
     //       dbg("Answer:",T1(answer[i]),T2(answer[i]),T3(answer[i]));
     //   }
     //   for(int j=0;j<bounds.size();j++){
     //       dbg(P1(bounds[j]),P2(bounds[j]));
     //   }
    }
    
    sort(all(answer));
    rep(i,N){
       // dbg("Answer:",T1(answer[i]),T2(answer[i]),T3(answer[i]));
        cout << " " << answer[i].second.first << " " << answer[i].second.second;
    }
    return;
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
