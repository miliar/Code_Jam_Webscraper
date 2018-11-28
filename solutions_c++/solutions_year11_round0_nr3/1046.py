#include<cstdio>
#include<vector>
#include<algorithm>
#include<climits>
using namespace std;

int main(){
    
    int T;
    int N;
    int a;    
    scanf("%d",&T);
    for (int k=1; k <= T; ++k){
        scanf("%d",&N);
        int sum = 0;
		int S = 0;
        int mini = INT_MAX;
        for (int i=0; i < N; ++i){
            scanf("%d",&a);
            sum ^= a;
			S += a;
            mini = min(mini,a);
        }
        printf("Case #%d: ",k);
        if (sum) printf("NO\n");
        else {
             printf("%d\n",S-mini);     
        }    
    }    
    return 0;    
}
