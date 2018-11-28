#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

vector<int> candy;
int petricksum(int a, int b) {
    return a ^ b;
}
bool ck[20];
int max_candy;
void dfs(int idx) {
    if(idx == candy.size()) {
        
        int asum = 0, bsum = 0;
        int oria = 0, orib = 0;
        for(int i=0;i<candy.size();i++) {
            if(ck[i]) {
                asum = petricksum(asum, candy[i]);
                oria += candy[i];
            } else {
                bsum = petricksum(bsum, candy[i]);
                orib += candy[i];
            }  
        }
        if(asum == bsum && oria != 0 && orib != 0) {
            if(max_candy < oria)
                max_candy = oria;
            if(max_candy < orib)
                max_candy = orib;
        }
        return;
    }
    ck[idx] = false;
    dfs(idx + 1);
    ck[idx] = true;
    dfs(idx + 1);

}
int main() {
    
    int T, N;
    scanf("%d", &T);
    for(int q=0;q<T;q++) {
        scanf("%d", &N);
        int c;
        candy.clear();
        for(int i=0;i<N;i++) {
            scanf("%d", &c);
            candy.push_back(c);
        }
        memset(ck, 0, sizeof(ck));
        max_candy = -1;
        dfs(0);
        printf("Case #%d: ", q+1);
        if(max_candy == -1)
            printf("NO\n");
        else
            printf("%d\n", max_candy);
    }
    return 0;
}
