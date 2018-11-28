#include <iostream>
#include <fstream>

using namespace std;


int N, S, p, score;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;    
    scanf("%d",&T);
    for(int t = 0;t<T;++t) {
        scanf("%d %d %d",&N,&S,&p);
        int res = 0;
        for(int i = 0;i<N;++i) {
            scanf("%d",&score);
            int currBest = (score == 0)?(0):((score-1)/3 + 1);
            if(currBest >= p ) ++res;
            else if(currBest + 1 >= p && S && score%3 != 1 && currBest > 0) {  
                --S;
                ++res;
            }
        }
        printf("Case #%d: %d\n", t+1, res);
    }
    return 0;
}
