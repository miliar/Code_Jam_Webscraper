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

void run(int cnum){
    int N;
    cin >> N;
    vector<pii> otsk,btsk;
    int on = 0, bn = 0;
    int opos = 1, bpos = 1;
    REP(i,N){
        string s;
        int but;
        cin >> s >> but;
        if(s[0] == 'O')
            otsk.PB(make_pair(i,but));
        else
            btsk.PB(make_pair(i,but));
    }
    int czas = 0;
    int done = 0;
    while(on != otsk.size() || bn != btsk.size()){
        bool got = false;
        if(on != otsk.size()){
            if(otsk[on].SE != opos){
                opos += (otsk[on].SE < opos ? -1 : 1);
            } else {
                if(otsk[on].FI == done){
                    got = true;
                    on++;
                }
            }
        }

        if(bn != btsk.size()){
            if(btsk[bn].SE != bpos){
                bpos += (btsk[bn].SE < bpos ? -1 : 1);
            } else {
                if(btsk[bn].FI == done && !got){
                    got = true;
                    bn++;
                }
            }
        }

        if(got) done++;
        czas++;
    }
    cout << "Case #" << cnum << ": " << czas << "\n";
}

int main(){
    ios::sync_with_stdio(0);
    int C;
    cin >> C;
    REP(i,C) run(i+1);
    return 0;
}

