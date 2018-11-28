#include <cstdio>
#include <algorithm>

using namespace std;

int c[200];

int main(){
    int t;
    scanf("%d",&t);
    for(int test = 0; test < t; ++test){
        int N,L,H;
        scanf("%d %d %d",&N,&L,&H);
        for(int i = 0; i < N; ++i){
            scanf("%d",&c[i]);
        }
        bool ok = false;
        int sol = 0;
        for(int i = L; i <=H; ++i){
            int br = 0;
            for(int j = 0; j < N; ++j){
                int m = min( c[j], i );
                if( c[j] % m == 0 && i % m == 0 ){
                    ++br;
                }
            }
            if( br == N ){
                ok = true;
                sol = i;
                  break;
            }
        }
        if(ok){
            printf("Case #%d: %d\n", test+1, sol);
        }else{
            printf("Case #%d: NO\n", test+1);
        }
    }
    return 0;
}
