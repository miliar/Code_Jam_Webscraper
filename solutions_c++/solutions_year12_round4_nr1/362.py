// {{{
// vim:filetype=cpp foldmethod=marker foldmarker={{{,}}}
#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <climits>
#include <complex>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#define ALL(A)		(A).begin(),(A).end()
#define DUMP(A)    cout<<#A<<"="<<(A)<< endl
#define SIZE(A)    (int)((A).size())
#define MP  make_pair
#define PB  push_back
using namespace std;
typedef long long ll;

int vx[]={1,0,-1,0},vy[]={0,1,0,-1};
// }}}
ll ds[10000],ls[10000],dp[10000];
int main(){
    int T;
    scanf("%d",&T);
    for(int ix=0;ix<T;ix++){
        printf("Case #%d: ",ix+1);
        int N;
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%lld%lld",&ds[i],&ls[i]);
        }
        ll D;
        scanf("%lld",&D);
        dp[0]=ds[0];
        for(int i=1;i<N;i++){
            dp[i]=0;
            for(int j=0;j<i;j++){
                if(ds[j]+dp[j]>=ds[i]){
                    dp[i]=max(dp[i],min(ls[i],ds[i]-ds[j]));
                }
            }
        }
        bool is=false;
        for(int i=0;i<N;i++){
            if(ds[i]+dp[i]>=D) is=true;
        }
        if(is) printf("YES\n");
        else printf("NO\n");
    }
}
