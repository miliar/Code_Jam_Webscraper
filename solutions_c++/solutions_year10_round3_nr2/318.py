#include<stdio.h>

int main(){
    int nt;
    int l,p,c;
    scanf("%d",&nt);
    for(int t=1;t<=nt;t++){
        scanf("%d %d %d",&l,&p,&c);
        int tot=0;
        while(p>l){
            tot++;
            p=(p+c-1)/c;
        }   
        //printf("%d\n",tot);
        int hasil=0;
        while(tot>1){
            hasil++;
            tot=(tot+1)/2;
        }
        printf("Case #%d: %d\n",t,hasil);
    }
    return 0;    
}   
