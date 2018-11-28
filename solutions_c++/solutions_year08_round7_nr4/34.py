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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;




#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(i, v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define PB push_back
#define CLEAR(a, b) memset(a, (b), sizeof(a))
#define SZ(v) (int)((v).size())
#define MP make_pair
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define UNIQ(v) (v).erase(unique(ALL(v)),(v).end())

int tst;
int r,c;
char in[20][20];

int dp[1<<16][5][5];

int go(int mask,int cr,int cc){
    int& ret = dp[mask][cr][cc];
    if(ret>=0) return ret;
    ret=0;
    for(int i=-1;i<2;++i) for(int j=-1;j<2;++j){
        int tr = cr+i;
        int tc = cc+j;
        if(tr<0||tr>=r) continue;
        if(tc<0||tc>=c) continue;
        if(in[tr][tc]!='.') continue;
        int cur = tr*c+tc;
        if((mask&(1<<cur))!=0) continue;
        int newmask = mask|(1<<cur);
        if(!go(newmask,tr,tc)){
            ret = 1;
            return ret;
        }
    }
    return ret;
}



int main(){
    freopen("D-small-attempt0.in","rt",stdin);
    freopen("dout.txt","wt",stdout);
    scanf("%d",&tst);
    for(int cas=1;cas<=tst;++cas){
        scanf("%d%d",&r,&c);
        REP(i,r) scanf("%s",in[i]);
        memset(dp,-1,sizeof(dp));
        int cr,cc;
        REP(i,r) REP(j,c){
            if(in[i][j]=='K'){
                cr=i;cc=j;
            }
        }
        int cur = cr*c+cc;
        cout<<"Case #"<<cas<<": ";
        if(go(1<<cur,cr,cc)){
            cout<<"A\n";
        }
        else{
            cout<<"B\n";
        }
    }
    return 0;
}
