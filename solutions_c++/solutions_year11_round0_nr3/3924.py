#include <cstdio>

using namespace std;

int br[20];
int main(){
    int t;
    scanf("%d",&t);
    for(int test = 0;test < t; ++test){
        int n;
        scanf("%d",&n);
        int sol = -1;
        for(int i = 0;i < n; ++i)
            scanf("%d",&br[i]);
        for(int i = 0;i < (1<<n); ++i){
            bool isokseta = false, isoksetb = false;
            int seta = 0, setb = 0, sola = 0, solb = 0;
            for(int x = 0; x < n; ++x){
                if( ((1<<x)&i) > 0 ){
                    isokseta = true;
                    seta = seta^br[x];
                    sola += br[x];
                }else{
                    isoksetb = true;
                    setb = setb^br[x];
                    solb += br[x];
                }
            }
            if( isokseta && isoksetb && seta == setb && sola > sol) sol = sola;
        }
        printf("Case #%d: ", test+1);
        if( sol <= 1 ) printf("NO\n"); else printf("%d\n",sol);
    }
    return 0;
}
