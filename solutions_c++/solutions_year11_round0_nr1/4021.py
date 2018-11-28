#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
    int z;
    scanf("%d", &z);
    for(int j=1; j<=z; j++){
        int n;
        scanf("%d", &n);
        int timeo=0, poso=1;
        int timeb=0, posb=1;
        for(int i=0; i<n; i++){
            int t;
            char s[10];
            scanf("%s%d", s, &t);
            if(s[0]=='O'){
                //robot O
                timeo=max(timeb+1, timeo+abs(poso-t)+1); 
                poso=t;
                //printf("Robot zero, %d %d\n", timeo, poso);
            }else{
                //robot B
                timeb=max(timeo+1, timeb+abs(posb-t)+1);
                posb=t;
                //printf("Robot b, %d %d\n", timeb, posb);
            }
        }
        printf("Case #%d: %d\n", j,  max(timeo, timeb));
    }
    return 0;
}
