#include<stdio.h>

struct dt{
    int x,y;   
};

int main(){
    dt data[1010];
    int nt,n;
    scanf("%d",&nt);
    for(int t=1;t<=nt;t++){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d %d",&data[i].x,&data[i].y);
        }   
        int tot=0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                if(data[i].x<data[j].x){
                    if(data[i].y>data[j].y){
                        tot++;
                    }   
                }
                else{
                    if(data[i].y<data[j].y){
                        tot++;                        
                    }
                }
            }   
        }
        
        printf("Case #%d: %d\n",t,tot);
    }
    return 0;   
}
