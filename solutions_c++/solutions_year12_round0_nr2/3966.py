#include<cstdio>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<limits>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second
#define PP system("PAUSE");

using namespace std;

int score[110];

int main(void){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    int N, S, P;
    for(int i = 1; i <= T; i++){
        int ans = 0;
        scanf("%d%d%d", &N, &S, &P);
        for(int j = 0; j < N; j++) scanf("%d", &score[j]);
        int GAP = P*3-2;
        for(int j = 0; j < N; j++){
            if(score[j]<=0){
                if(P == 0) ans++;
                continue;
                }
            if(score[j] >= GAP) ans++;
            else if(score[j]>=GAP-2 && S) ans++, S--;
            }
        printf("Case #%d: %d\n", i, ans);
        }

    return 0;
    }
