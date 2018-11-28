#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cstring>
#include <set>
#include <stack>
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define FE(a,b) for(__typeof((b).end()) a=(b).begin(); a!=(b).end(); ++a)
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

int t, n, k, dc;
int D[10010];
int L[10010];
int H[10010];
bool ans;

int main(){
	scanf("%d", &t);
	FWD(ttt,1,t+1){
		scanf("%d", &n);
		printf("Case #%d: ", ttt);
        FWD(i,0,n)
            scanf("%d %d", &D[i], &L[i]);
        scanf("%d", &dc);
        ans = 0;
        H[0] = D[0];
        FWD(i,1,n)
            H[i] = -1;
        FWD(i,0,n){
            //printf("%d %d\n", i, H[i]);
            if(H[i] == -1) continue;
            if(D[i] + H[i] >= dc) ans = 1;
            k = i + 1;
            while(k < n && D[i] + H[i] >= D[k]){
                H[k] = max(H[k], min(D[k]-D[i], L[k]));
                ++k;
            }
        }
		if(!ans)
            printf("NO\n");
        else
            printf("YES\n");
	}
	return 0;
}
