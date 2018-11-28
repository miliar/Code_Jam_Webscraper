#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 512;

long long tab[MAXN][MAXN];
long long sum[MAXN][MAXN];
long long srow[MAXN][MAXN];
long long scol[MAXN][MAXN];

long long cjrow[MAXN][MAXN];
long long cicol[MAXN][MAXN];

long long ci[MAXN][MAXN];
long long cj[MAXN][MAXN];

int main(){
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp){
        int m,n,d;
        cin >> m >> n >> d;
        for(int i=1;i<=m;++i){
            string line;
            cin >> line;
            for(int j=1;j<=n;++j){
                tab[i][j] = line[j-1] - '0';
            }
        }
        
        for(int i=1;i<=m;++i){
            srow[i][0] = 0;
            cjrow[i][0] = 0;
            for(int j=1;j<=n;++j){
                srow[i][j] = srow[i][j-1] + tab[i][j];
                cjrow[i][j] = cjrow[i][j-1] + j*tab[i][j];
            }
        }
        
        for(int j=1;j<=n;++j){
            scol[0][j] = 0;
            cicol[0][j] = 0;
            for(int i=1;i<=m;++i){
                scol[i][j] = scol[i-1][j] + tab[i][j];
                cicol[i][j] = cicol[i-1][j] + i*tab[i][j];
            }
        }
        
        int resp = 0;
        
        for(int i=1;i<=m-2;++i){
            for(int j=1;j<=n-2;++j){
                sum[i][j] = srow[i][j+2] - srow[i][j-1];
                sum[i][j] += srow[i+1][j+2] - srow[i+1][j-1];
                sum[i][j] += srow[i+2][j+2] - srow[i+2][j-1];
                
                ci[i][j] = cicol[i+2][j] - cicol[i-1][j];
                ci[i][j] += cicol[i+2][j+1] - cicol[i-1][j+1];
                ci[i][j] += cicol[i+2][j+2] - cicol[i-1][j+2];
                
                cj[i][j] = cjrow[i][j+2] - cjrow[i][j-1];
                cj[i][j] += cjrow[i+1][j+2] - cjrow[i+1][j-1];
                cj[i][j] += cjrow[i+2][j+2] - cjrow[i+2][j-1];
            }
        }
        
        for(int k=3;k<=min(m,n);++k){
            for(int i=1;i+k<=m+1;++i){
                for(int j=1;j+k<=n+1;++j){      
                    long long ti = ci[i][j] - tab[i][j]*i - tab[i][j+k-1]*i - tab[i+k-1][j]*(i+k-1) - tab[i+k-1][j+k-1]*(i+k-1);
                    long long tj = cj[i][j] - tab[i][j]*j - tab[i][j+k-1]*(j+k-1) - tab[i+k-1][j]*j - tab[i+k-1][j+k-1]*(j+k-1);
                    
                    long long s = sum[i][j] - tab[i][j] - tab[i][j+k-1] - tab[i+k-1][j] - tab[i+k-1][j+k-1];
                    //printf("%d %d %d\n",ti,tj,s);
                    
                    if((2*ti == s*(i+i+k-1)) && (2*tj == s*(j+j+k-1))){
                        resp = k;
                    }
                    
                    if(i+k < m+1 && j+k < n+1){
                        sum[i][j] += srow[i+k][j+k] - srow[i+k][j-1];
                        sum[i][j] += scol[i+k][j+k] - scol[i-1][j+k];
                        sum[i][j] -= tab[i+k][j+k];
                        
                        ci[i][j] += (i+k)*(srow[i+k][j+k] - srow[i+k][j-1]);
                        ci[i][j] += cicol[i+k][j+k] - cicol[i-1][j+k];
                        ci[i][j] -= tab[i+k][j+k]*(i+k);
                        
                        cj[i][j] += (j+k)*(scol[i+k][j+k] - scol[i-1][j+k]);
                        cj[i][j] += cjrow[i+k][j+k] - cjrow[i+k][j-1];
                        cj[i][j] -= tab[i+k][j+k]*(j+k);
                    }
                    
                }
            }
        }
        
        printf("Case #%d: ",lp);
        if(resp == 0){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n",resp);
        }
        
    }
    return 0;
}
