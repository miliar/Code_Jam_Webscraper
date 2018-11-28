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
#include <cstring>
#include <complex>
#include <climits>
#include <queue>
#include <ctime>
#include <ext/numeric>
#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

long long sp[1001];
long long pos[1001];
long long x;
int can[1001];

int main(){
    freopen("in.in","rt",stdin);
    freopen("out.out","wt",stdout);
    
    long long t,n,k,b,T;
    
    cin>>t;//scanf("%d",&t);
    rep(tt,0,t){
        //scanf("%d %d %d %d",&n,&k,&b,&T);
        cin>>n>>k>>b>>T;
        memset(can,0,sizeof(can));
        rep(i,0,n)
            cin>>pos[i];//scanf("%d",&pos[i]);
        rep(i,0,n){
            cin>>sp[i];//scanf("%d",&x),sp[i]=x;
            long long xx = sp[i]*T+pos[i];
//            cout<<xx<<endl;
            if(xx>=b)
                can[i]=1;
        }
        int cnt = count(can,can+n,1);
        printf("Case #%d: ",tt+1);
        if(cnt<k)
            printf("IMPOSSIBLE\n");
        else{
            int cc=0,res=0,ccc=0;
            for(int i  = n-1;i>=0;--i){
                if(cc==k)
                    break;
                if(!can[i]){
                    ccc++;
                }
                if(can[i])
                    res+=ccc,cc++;
            }
            printf("%d\n",res);
        }
    }
    return 0;
}
