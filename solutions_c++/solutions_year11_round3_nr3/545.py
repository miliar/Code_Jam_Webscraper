#include<stdio.h>

int N, L , H;
int a[10010];
int main(){
    int T;
    int g, i, k;
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d %d %d ", &N, &L, &H);
        for(i=0; i<N; i++)
            scanf("%d ", &a[i]);

        int bizu=0;int resp=0;
        for(i=L; i<=H; i++){
            int pau=0;
            for(k=0; k<N; k++){
                if(i>a[k]){
                    if((i%a[k])!=0){
                        pau=1;
                        break;
                    }
                }
                else{
                    if((a[k]%i)!=0){
                        pau=1;
                        break;
                    }

                }
            }
            if(pau==0){
                    bizu=1;
                    resp=i;
                    break;
            }
               
        }
        printf("Case #%d: ", g);
        if(bizu==1)
            printf("%d\n", resp);
        else printf("NO\n");
    }
    return 0;
}
