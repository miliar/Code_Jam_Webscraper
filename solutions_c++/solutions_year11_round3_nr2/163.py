#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <string>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define tr(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define all(x) x.begin(),x.end()
#define pb push_back
using namespace std;
const int inf=~0U>>1;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long LL;
template<class T> bool get_max(T&a,T&b){return b>a?a=b,1:0;}
template<class T> bool get_min(T&a,T&b){return b<a?a=b,1:0;}

const int maxn = 1000005;
LL a[maxn],b[maxn],c[maxn];
int L,N,C;
LL t;
LL ans;

void read(){
    cin>>L>>t>>N>>C;
    REP(i,C){
        cin>>a[i];
    }
}

LL solve(){
    ans=0;
    bool ok = true;
    LL tmp=0;
    int m=0,index=-1;
    FOR(i,1,N){
        b[i]=a[(i-1)%C];
        ans+=b[i];
        if(ok&&ans*2>=t){
            ok = false;
            index=i;
            c[m++] = ans-t/2;
        }
    }
    if(!ok){
        FOR(i,index+1,N){
            c[m++]=b[i];
        }
        sort(c,c+m);
        for(int i=m-1,j=0;i>=0&&j<L;i--){
            j++;
            tmp+=c[i];
        }
    }
    return ans*2-tmp;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    int tt=1;
    while(T--){
        read();
        LL re = solve();
        printf("Case #%d: ",tt++);
        printf("%lld\n",re);
    }
    return 0;
}
