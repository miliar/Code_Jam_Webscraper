#include <iostream>
#include <map>
using namespace std;
long long mod = 1000000007;
long long bigN;
map<long long,long long> ways[71][2];
int biggestsum;
int sums[5000][71];
long long pick[100][100];
int B;
long long get(long long N, int x, int havezero) {
    map<long long,long long>::iterator it = ways[x][havezero].find(N);
    if (it!=ways[x][havezero].end()) return it->second;
    
    bool debug = false;//N==1 && x==3 && havezero==1;
    
    if (N==0) {
        return ways[x][havezero][N] = (havezero?0:1);
    }
    //printf("Get[%I64d][%d][%d]\n",N,x,havezero);
    // how many ways are there to get a sum of X in this column using zero / not using zero
    long long ret = 0;
    
    int low = (N==bigN?x:1);
    for (int y=low; y<=x; y++) {
        if (debug) printf("Use %d numbers\n",y);
        // use y numbers here; the rest become nothing
        // case 1: none of these digits is 0
        
        for (int i=N%B; i<=biggestsum && i<=N; i+=B) {
            long long wayswithout = sums[i][y];
            long long wayswith = sums[i][y-1];
            if (wayswithout==0 && wayswith==0) continue;
            
            if (debug) printf("Make column sum to %d\n",i);
            // make this column add to i

            long long here1 = get((N-i)/B,y,0);
            long long here2 = get((N-i)/B,y,1);
            
            long long mult1 = (wayswithout*here1)%mod;
            long long mult2 = (wayswith*here2)%mod;
            
            long long mult = (mult1+mult2)%mod;
            long long order;
            if (N==bigN) {
                order = 1;   
            } else {
                order = ((pick[x][y] - (havezero?pick[x-1][y]:0))%mod+mod)%mod;
            }
            mult = (mult*order)%mod;
            ret = (ret+mult)%mod;
            if (debug) printf("Which contributes %I64d\n",mult);
        }
    }    
    //printf("get(%I64d,%d,%d) = %I64d\n",N,x,havezero,ret);
    ways[x][havezero][N] = ret;
    return ret;
}
int main() {
    for (int i=0; i<100; i++) {
        pick[i][0]=1;
        pick[i][1]=i;
        for (int j=2; j<=i; j++) {
            pick[i][j] = (pick[i][j-1] * (i-j+1))%mod;
        }
    }
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);
        long long N; scanf("%I64d",&N); bigN = N;
        scanf("%d",&B);
        for (int i=0; i<71; i++)
        for (int j=0; j<2; j++) ways[i][j].clear();   
        biggestsum = (B-1)*B/2;
        memset(sums,0,sizeof(sums));
    
        sums[0][0]=1;
        
        for (int i=1; i<B; i++) {      
            for (int sum=biggestsum; sum>=i; sum--) {
                for (int j=B; j>=1; j--) {
                    // make up sum 'sum' using j digits
                    sums[sum][j] += sums[sum-i][j-1];
                    sums[sum][j]%=mod;
                }
            }
        }      
        long long sum = 0;
        for (int i=1; i<=B; i++) {
            sum += get(N,i,0);
            sum %= mod;
        }

        printf("%I64d\n",sum);
    }
}
