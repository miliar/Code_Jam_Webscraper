#include<stdio.h>
#include<string.h>
#include<math.h>

int main(){
    int T,N,arr[150],arrc[50];
    char s[1];
    int temp;
    int hasil,pointo,pointb,tempo,tempb,jalano,jalanb;
    
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        scanf("%d",&N);
        pointo=pointb=1;
        hasil=0;
        tempo=tempb=0;
        jalano=jalanb=0;
        for(int j=0;j<N;j++){
            //fflush(stdin);
            scanf("%s",s);
            scanf("%d",&arr[j]);
            int ya=s[0];
            if(ya==79){
                tempo++;
                tempb=0;
                if(tempo==1){
                    if(arr[j]==pointo){
                        hasil=hasil+1;
                        jalanb++;
                        jalano=0;  
                    }
                    else if((fabs(arr[j]-pointo))>jalano){
                        temp=fabs(arr[j]-pointo)-jalano;
                        hasil=hasil+temp+1;
                        pointo=arr[j];
                        jalanb=jalanb+temp+1;
                        jalano=0;
                    } 
                    else{
                        hasil=hasil+1;
                        pointo=arr[j];  
                        jalanb++;
                        jalano=0;
                    }  
                }
                else{
                    temp=fabs(arr[j]-pointo);
                    hasil=hasil+temp+1; 
                    pointo=arr[j];
                    jalanb=jalanb+temp+1;
                }
                //printf("%d %d %d\n",hasil,jalanb,pointo);
            }
            else{
                tempb++;
                tempo=0;
                if(tempb==1){
                    if(arr[j]==pointb){
                        hasil=hasil+1; 
                        jalano++;
                        jalanb=0;
                    }
                    else if((fabs(arr[j]-pointb))>jalanb){
                        temp=fabs(arr[j]-pointb)-jalanb;
                        hasil=hasil+temp+1;
                        pointb=arr[j];
                        jalano=jalano+temp+1;
                        jalanb=0;
                    } 
                    else{
                        hasil=hasil+1;
                        pointb=arr[j];
                        jalano++;
                        jalanb=0;  
                   }
                }
                else{
                    temp=fabs(arr[j]-pointb);
                    hasil=hasil+temp+1;
                    pointb=arr[j];
                    jalano=jalano+temp+1;   
                }
                //printf("%d %d %d\n",hasil,jalano,pointb);    
            }
        }  
        printf("Case #%d: %d\n",i+1,hasil);
        
        
    }
    
    
 
 
 while(getchar()!=EOF);
 return 0;   
}
