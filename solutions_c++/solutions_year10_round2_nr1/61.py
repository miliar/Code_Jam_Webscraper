/*{{{*/
#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <utility>

using namespace std;
//using namespace __gnu_cxx;

typedef long long ll;
typedef double db;
typedef unsigned int uint;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef istringstream is;
typedef ostringstream os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);++(i))
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);--(i))
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();++(i))
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define PRINT(v) for(int (i)=0;(i)<(int)(v).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;
/*}}}*/

vs tab[300];
int *st1, *st2;
int w1,w2;

void run(int cnum){
    int n,m;
    cin >> n >> m;

    int wyn = 0;
    string p;
    REP(i,n){
        cin >> p;
        string h;
        tab[i].clear();
        FORS(j,p){
            if(p[j] == '/'){
                if(h.size() > 0){
                    tab[i].PB(h);
                    h = "";
                }
            }
            else h.PB(p[j]);
        }
        if(h.size() > 0) tab[i].PB(h);
    }
    REP(i,m){
        cin >> p;
        string h;
        tab[n+i].clear();
        FORS(j,p){
            if(p[j] == '/'){
                if(h.size() > 0){
                    tab[n+i].PB(h);
                    h = "";
                }
            }
            else h.PB(p[j]);
        }
        if(h.size() > 0) tab[n+i].PB(h);
        int maxx = 0;
        REP(j,n+i){
            int tmp = 0;
            REP(k,min(tab[n+i].size(), tab[j].size())){
                if(tab[n+i][k] == tab[j][k]) ++tmp;
                else break;
            }
//            cout << "  " << tmp << endl;
            maxx = max(maxx, tmp);
        }
        wyn += tab[n+i].size() - maxx;
    }

  //  REP(i,n+m)
    //    cout << " " << tab[i].size() << endl;
    cout << "Case #" << cnum << ": " << wyn << endl;
}

int main(){
    ios::sync_with_stdio(0);
    int C;
    cin >> C;
    st1 = new int[300];
    st2 = new int[300];
    REP(i,C) run(i+1);
    return 0;
}


