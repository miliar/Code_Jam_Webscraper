#include<iostream>
using namespace std;

int T;
int D,I,M,N;
int a[110];
int dp[110][256];

int main(){
    int i,j,k,l;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    cin>>T;
    int cas = 0;
    while(T--){
        cin>>D>>I>>M>>N;
        for(i=0;i<N;++i) cin>>a[i];
        
        for(i=0;i<N;++i){
            for(j=0;j<256;++j){
                dp[i][j] = i*D+abs(j-a[i]);
                for(k=0;k<i;++k){
                    if(M==0){
                        int t1 = dp[k][j]+D*(i-k-1)+abs(j-a[i]);
                        dp[i][j]<?=t1;
                    }
                    else{
                        int st = j-M;
                        int ed = j+M;
                        int cnt = 0;
                        int mn = 1<<30;
                        for(l=(st>?0);l<=(ed<?255);++l){
                            mn<?=dp[k][l];
                        }
                        while(true){
                            int t1 = mn+D*(i-k-1)+I*cnt+abs(j-a[i]);
                            dp[i][j]<?=t1;
                            if(st<0&&ed>255) break;
                            ++cnt;
                            int nst = st-M;
                            int ned = ed+M;
                            for(l=nst>?0;l<st;++l) mn<?=dp[k][l];
                            for(l = ed+1;l<=(ned<?255);++l) mn<?=dp[k][l];
                            st = nst;
                            ed = ned;
                        }
                    }
                }
            }
        }
        int res = 1<<30;
        for(i=0;i<N;++i){
            for(j=0;j<256;++j){
                int t1 = dp[i][j]+(N-i-1)*D;
                res<?=t1;
            }
        }
        ++cas;
        cout<<"Case #"<<cas<<": "<<res<<endl;
    }
    
    return 0;
}
