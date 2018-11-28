#include<iostream>
using namespace std;

int main() {
    freopen("in.txt","r",stdin);
    freopen("in1.txt","w",stdout);
    int i,cas,ax,ay,bx,by,n;
    scanf("%d",&cas);
    for(i = 1;i <= cas;i ++) {
        scanf("%d",&n);
        printf("Case #%d: ",i); 
        if(n == 1) {
            scanf("%d%d",&ax,&ay);
            printf("0\n");
        }
        else {
            scanf("%d%d%d%d",&ax,&ay,&bx,&by);
            if((bx > ax && by < ay) || (bx < ax && by > ay)) {
                printf("1\n");
            }
            else {
                printf("0\n");
            }
        }
    }
}
