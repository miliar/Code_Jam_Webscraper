#include<stdio.h>
#include<math.h>

int main(){
    int tes;
    
    scanf("%d",&tes);
    
    for(int i=1;i<=tes;i++){
        int a,b;
        scanf("%d %d",&a,&b);
        int arr[b+1],count,temp,yaa;
        for(int j=a;j<=b;j++){
            arr[j]=1;
        }
        count=0;
        for(int j=a;j<b;j++){
            if(arr[j]==1){
                arr[j]=0;
                temp=j;
                int dig=1;
                int hit=1;
                while(temp/10>0) {
                    dig=dig*10;
                    hit++;
                    temp=temp/10;
                }
                //printf("%d\n",dig);
                temp=j;
                int kom=1;
                for(int k=1;k<=hit;k++){
                    int x;
                    x=temp%10;
                    temp=temp/10;
                    while(x==0){
                        x=temp%10;
                        temp=temp/10;
                        k++; 
                    }
                    x=x*dig;
                    x=x+temp;
                    //printf("%d ",x);
                    if(x!=j && x<=b && arr[x]==1){
                        kom++;
                        arr[x]=0;   
                    }
                    temp=x;
                } 
                kom=(kom*(kom-1))/2;
                count+=kom;
            }
        }
        printf("Case #%d: %d\n",i,count);
        
    }
    
 
 
 while(getchar()!=EOF);
 return 0;   
}
