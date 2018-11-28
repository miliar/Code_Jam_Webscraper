#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define ll long long

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

ll dp[102][102];
int n,m;
vector<ll> box, toy;
vector<int> kbox, ktoy;

ll solve(int bi, int ti, ll bn, ll tn){
    ll ret=0;
    if(bi >= n || ti >= m) return 0;

    if(kbox[bi] == ktoy[ti]){
        //すぐ捨てる
        ret = max(ret, solve(bi+1, ti+1, box[bi+1], toy[ti+1]) + min(bn,tn));
        //とっておく
        if(bn > tn){
            ret = max(ret, solve(bi, ti+1, bn-tn, toy[ti+1]) + min(bn,tn));
        }else if(bn < tn){
            ret = max(ret, solve(bi+1, ti, box[bi+1], tn-bn) + min(bn,tn));
        }
    }else{
        ret = max(ret, solve(bi+1,ti,box[bi+1], tn));
        ret = max(ret, solve(bi,ti+1,bn, toy[ti+1]));
    }
    return ret;
}

int main(){
    int t;
    cin >> t;
    for(int x=1;x<=t;x++){

        cin >> n >> m;
        ll numtmp=0,ktmp;
        ll kind, num;
        memset(dp,0,sizeof(dp));
        box.clear();
        toy.clear();
        kbox.clear();
        ktoy.clear();
        
        cin >> num >> kind;
        for(int i=1;i<n;i++){
            cin >> numtmp >> ktmp;
            if(ktmp == kind){
                num += numtmp;
            }else{
                box.PB(num);
                kbox.PB(kind);
                num = numtmp;
                kind = ktmp;
            }
        }
        box.PB(num);
        kbox.PB(kind);

        cin >> num >> kind;
        for(int i=1;i<m;i++){
            cin >> numtmp >> ktmp;
            if(ktmp == kind){
                num += numtmp;
            }else{
                toy.PB(num);
                ktoy.PB(kind);
                num = numtmp;
                kind = ktmp;
            }
        }
        toy.PB(num);
        ktoy.PB(kind);

        n = box.size();
        m = toy.size();
        ll ret;
        ret = solve(0,0,box[0],toy[0]);
        printf("Case #%d: %lld\n",x,ret);
    }
}
