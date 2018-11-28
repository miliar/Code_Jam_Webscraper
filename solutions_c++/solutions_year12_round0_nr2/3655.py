#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
    int t;
    scanf("%d\n",&t);
    int aux = t; 
    while(t--) {
        int n,s,p;
        scanf("%d %d %d",&n,&s,&p);
        if (p != 0) p = p + p-1 + p-1;
        int min = p-2;
        if(min < 0) min = 1;
        int sum;
        int res = 0;
        for(int i = 0;i < n;i++) {
            scanf("%d",&sum);
            if(sum >= p) res++;
            else if(sum >= min && s >= 1) {
                res++;
                s--;
            }
            //printf("r = %d e s = %d\n e p = %d e min = %d\n",res,s,p,min);
        }
        printf("Case #%d: %d\n",aux-t,res);
    }
    return 0;
}
