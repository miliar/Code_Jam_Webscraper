#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <set>
#include <stack>
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define BCK(a,b,c) for(int a=(b); a>(c); --a)
#define FE(a,b) for(__typeof((b).end()) a=(b).begin(); a!=(b).end(); ++a)
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

int t, n, k, h;
int P[10000];
int H[10000];

bool test(){
    FWD(i,1,n)
        FWD(j,i+1,P[i])
            if(P[j] > P[i])
                return 0;
    return 1;
}

int main(){
	scanf("%d", &t);
	FWD(ttt,1,t+1){
        scanf("%d", &n);
        printf("Case #%d:", ttt);
        FWD(i,1,n){
            scanf("%d", &P[i]);
            H[i] = -1;
        }
        if(!test()){
            printf(" Impossible\n");
            continue;
        }
        h = H[n] = 100000000;
        P[n] = n+1;
        H[n+1] = H[n];
        BCK(i,n-1,0)
            H[i] = H[P[i]] - (H[P[P[i]]] - H[P[i]]) * (P[i]-i) / (P[P[i]] - P[i]) - n;
        FWD(i,1,n+1)
            printf(" %d", H[i]);
        printf("\n");
	}
	return 0;
}
