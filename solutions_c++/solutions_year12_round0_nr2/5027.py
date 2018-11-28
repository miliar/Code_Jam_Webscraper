#include<stdio.h>

int main(){
    int tes,n,s,p;
    
    scanf("%d",&tes);
    
    for(int i=1;i<=tes;i++){
        scanf("%d %d %d",&n,&s,&p);
        int isi,hasil;
        hasil=0;
        for(int j=1;j<=n;j++){
            scanf("%d",&isi);
            if(isi>=(p*3-2)){
                hasil++;
            }
            else if(s>0){
                int temp= p*3-4;
                if(isi>=(p*3-4) && temp>0){
                    hasil++;
                    s--;   
                }
            }
        }
        printf("Case #%d: %d\n",i,hasil);
    }
 
 while(getchar()!=EOF);
 return 0;   
}
