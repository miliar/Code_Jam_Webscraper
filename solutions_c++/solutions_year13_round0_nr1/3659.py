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

string solve(int testnr){
    bool free = false;
    char c;
    vector<int> xrow(4), orow(4), xcol(4), ocol(4);
    int xd1 = 0, xd2 = 0, od1 = 0, od2 = 0;
    rep(i,4) rep(j,4){
        cin >> c;
        if (c=='.') free = true;
        if (c=='X' || c=='T'){
            xrow[i]++;
            xcol[j]++;
            if (i==j) xd1++;
            if (i+j==3) xd2++;
        }
        if (c=='O' || c=='T'){
            orow[i]++;
            ocol[j]++;
            if (i==j) od1++;
            if (i+j==3) od2++;
        }
    }
    
    rep(i,4){
        if (xrow[i]==4) return "X won";
        if (orow[i]==4) return "O won";
        if (xcol[i]==4) return "X won";
        if (ocol[i]==4) return "O won";
    }
    if (xd1 == 4) return "X won";
    if (od1==4) return "O won";
    if (xd2==4) return "X won";
    if (od2==4) return "O won";
    
    if (free) return "Game has not completed";
    return "Draw";
}

int main(){

    init();
    
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
        cout << "Case #" << i << ": " << solve(i) << "\n";
    }
    
    return 0;
}
