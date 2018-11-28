#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int N;
    int Case=1;
    int T;
    scanf("%d", &N);
    while( N-- ){
        scanf("%d", &T);
        vector<int> v;
        for(int i=0;i<T;i++){
            int a;
            scanf("%d", &a);
            v.push_back(a);
        }
        
        bool found = false;
        int ans = 0, sum = 0;
        for(int i=1;i<(1<<T)-1;i++){
            int a = 0, b = 0, aa = 0, bb = 0;
            vector<int> vi, vo;
            for(int j=0;j<T;j++){
                if( ( i & (1<<j)) > 0 ) {
                    aa += v[j];
                    a ^= v[j];
                } else {
                    bb += v[j];
                    b ^= v[j];
                }
            }
            
            if( a == b ){
                ans = max(ans, max(aa,bb));
                found = true;
            }
        }
        
        printf("Case #%d: ", Case++);
        if( !found ) puts("NO");
        else printf("%d\n", ans );
    }
    
    return 0;
}
