#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>

using namespace std;

typedef long long LL;
const LL MOD = 100003;
LL Comb[501][501];
LL dp[501][501];
int N;
void pre_cal()
{
    Comb[0][0]=1;
    for(int n=1;n<=500;n++) {
        Comb[n][0]=1;
        for(int r=1; r<=n;r++) {
            Comb[n][r]=(Comb[n-1][r-1]+Comb[n-1][r])%MOD;
        }
    }

}

LL solve()
{

    for(int i = 2; i <= N; i++) dp[i][1]=1;
    for(int i = 2; i <= N; i++) {
        for(int rank = 2; rank < i; rank++) {
            int cur = i, prev = rank;
            int totalBetween = cur-prev-1;
            LL &ret = dp[i][rank];
            ret = 0;
            for(int new_rank = 1; new_rank < rank; new_rank++) {
                ret = (ret + dp[rank][new_rank]*Comb[totalBetween][rank-new_rank-1])%MOD;
            }
            //if(i==N&&rank==4) cout<<ret<<endl;
        }
    }
    LL ret = 0;
    for(int i = 1; i < N; i++) ret=(ret+dp[N][i])%MOD;

    return ret;
}

int main()
{
   // freopen("test.in","r",stdin);
    //freopen("test.out","w",stdout);
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    //double cl = clock();
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    pre_cal();
    int T;
    cin>>T;
    for(int tc=1;tc<=T;tc++) {
        cin>>N;
        LL ret = solve();
        cout<<"Case #"<<tc<<": "<<ret<<endl;
    }
    //cl=clock()-cl;
    //cout<<cl/1000<<endl;
    return 0;
}
