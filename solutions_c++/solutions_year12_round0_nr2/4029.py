#include <cstdio>

const int MAX_N = 100+10;
int t[MAX_N];

int main(){
    int noc;
    scanf("%d",&noc);
    int N,S,p;
    for (int tnoc=1;tnoc<=noc;++tnoc){
        printf("Case #%d: ",tnoc);
        scanf("%d%d%d",&N,&S,&p);
        for (int i=0;i<N;++i){
            scanf("%d",&t[i]);
        }
        int low2 = p-2;
        if (low2<0){
            low2 = 0;
        }
        int low1 = p-1;
        if (low1<0){
            low1 = 0;
        }
        int lowp = p+low2+low2;
        int stdp = p+low1+low1;
        int passCount = 0;
        int midCount = 0;
        for (int i=0;i<N;++i){
            if (t[i]>=stdp){
                ++passCount;
            } else if (t[i]>=lowp){
                ++midCount;
            }
        }
        if (midCount>S){
            passCount += S;
        } else {
            passCount += midCount;
        }
        printf("%d\n",passCount);
    }
    return 0;
}
