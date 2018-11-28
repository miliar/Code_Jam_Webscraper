#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int h,w;

bool check(int cur, int prv){
    for (int i=0;i<w;++i) if ((cur>>i)&1){
        if (i>0 && (prv>>(i-1))&1) return 0;
        if (i+1<w && (prv>>(i+1))&1) return 0;
    }
    return 1;
}

bool adj(int x){
    for (int i=0;i<w;++i) if ((x>>i)&(x>>i+1)) return 1;
    return 0;
}

int ones(int x){
    int ret=0;
    for (;x;x>>=1) ret+=(x&1);
    return ret;
}

void show_bits(int x){
    for (int i=0;i<w;++i,x>>=1) cerr<<(x&1);
    cerr<<endl;
}

int main(){
    int C;
    cin>>C;
    for (int cC=0;cC<C;++cC){
        cin>>h>>w;
        vector<int> v(h,0);
        for (int i=0;i<v.size();++i){
            string s;
            cin>>s;
            for (int j=0;j<s.size();++j) if (s[j]=='x'){
                v[i]|=(1<<j);
            }
        }
        vector<vector<int> > dp(h,vector<int>(1<<w,0));
        for (int i=0;i<dp[0].size();++i) if (!(i&v[0]) && !adj(i)){
            dp[0][i]=ones(i);
        }
        for (int i=1;i<h;++i){
            for (int bm=0;bm<dp[i].size();++bm) if (!(bm&v[i]) && !adj(bm)){
                for (int prv=0;prv<dp[i-1].size();++prv){
                    bool ok=check(bm,prv);
                    if (ok){
                        dp[i][bm]>?=dp[i-1][prv]+ones(bm);
                    }
                }
            }
        }
        int ans=*max_element(dp[h-1].begin(),dp[h-1].end());
        cout<<"Case #"<<cC+1<<": "<<ans<<endl;
    }
}
