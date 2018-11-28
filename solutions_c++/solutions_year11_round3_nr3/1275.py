#include <cstdio>

int r,l,h,n,m,t[20000];

int main(){
    scanf("%d ", &r);
    for(int i=0; i<r; ++i){
        scanf("%d %d %d", &n, &l, &h);
        for(int j=0; j<=10002; ++j)
            t[j]=0;

        bool f=0;
        for(int j=0; j<n; ++j){
            scanf("%d ", &m);
            for(int k=0; k<=10002; ++k){
                if(k%m==0 || m%k==0){
                    t[k]++;
                //    printf(">>%d\n", k);
                }
            }
        }
        printf("Case #%d: ", i+1);
        for(int j=l; j<=h; ++j){
            if(t[j]==n){
                printf("%d\n", j);
                f=1;
                break;
            }
        }
        if(!f)
            printf("NO\n");
    }
}
