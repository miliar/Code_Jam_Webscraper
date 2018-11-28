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
int q,m;
double in[10][4];
double p[50000];
int pc;

void go(int h,double cur){
    if(h==m){
        p[pc] = cur;
        ++pc;
        return;
    }
    for(int i=0;i<4;++i){
        go(h+1,cur*in[h][i]);
    }
}


int main(){
    freopen("C-small-attempt0.in","rt",stdin);
    freopen("out.txt","wt",stdout);
    scanf("%d",&tst);
    for(int cas=1;cas<=tst;++cas){
        scanf("%d%d",&q,&m);
        for(int i=0;i<m;++i){
            for(int j=0;j<4;++j){
                scanf("%lf",&in[i][j]);
            }
        }
        pc=0;
        go(0,1);
        sort(p,p+pc);
        reverse(p,p+pc);
        double res = 0;
        double mul = 1.0;
        double sum=1.0;
        for(int i=0;i<pc&&i<q;++i){
            if(sum<=0.0) break;
            res = res+(mul*p[i])/sum;
            mul = mul*(1.0-((p[i])/sum));
            sum-=p[i];
            
        }
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
    return 0;
}
