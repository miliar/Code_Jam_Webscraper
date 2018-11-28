#include <cstdio>
#include <utility>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int N;
int permutation[1001];
// int state[1001];

int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        
        scanf("%d", &N);
        for(int i = 0; i < N; ++i)
            scanf("%d", permutation + 1 + i);
        
        /**
        for(int i = 1; i <= N; ++i)
            state[i] == -1;
        
        int lens = 0;
        
        for(int i = 1; i <= N; ++i)
        {
            if(state[i] == -1)
                lens += dfs(i);
        }
        **/
        
        double ans = 0;
        
        for(int i = 1; i <= N; ++i)
            if(permutation[i] != i)
                ans += 1.0;
            
        printf("%.6lf\n", ans);
    }
    
    return 0;
}