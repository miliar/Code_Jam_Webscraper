#include<cstdio>
#include<algorithm>

using namespace std;

int F[105][105],Arr[105];

int DP(int l,int r) {
     if (F[l][r] != -1) {
                 return F[l][r];
     }
     
     if (l + 1 == r) {
           F[l][r] = 0;
           return F[l][r];
     }
     F[l][r] = 0x7FFFFFFF;
     
     for(int k = l + 1 ; k < r ; k++) {
             F[l][r] = min(F[l][r],DP(l,k) + DP(k,r) + Arr[r] - Arr[l] - 2);
     }
     return F[l][r];
}

int main() {
//    freopen("test.in","r",stdin);
//    freopen("test.out","w",stdout);
    
    int T,N,M;
    scanf("%d",&T);
    for(int t = 0 ; t < T ; t++) {
            memset(F,-1,sizeof(F));
            scanf("%d%d",&N,&M);
            for(int i = 1 ; i <= M ; i++) {
                    scanf("%d",&Arr[i]);
            }
            
            sort(&Arr[1],&Arr[M + 1]);
            Arr[0] = 0,Arr[M + 1] = N + 1;
            
            
            printf("Case #%d: %d\n",t + 1,DP(0,M + 1));
     /*
            for(int i = 0 ; i <= M + 1 ; i++) {
                    for(int j = 0 ; j <= M + 1 ; j++) {
                            printf("%d ",F[i][j]);
                            }
                            printf("\n");
                    }
     */
    }
    
    return 0;
}
