#include<stdio.h>

void sort(int c[],int n);
void inttobin(int c[],int n,int arr[][20]);
void find(int arr[][20],int c[],int n);

int main(){

    int c[1000],n,t,l,m;
    int arr[1000][20];
    int i,j,k;

    scanf("%d",&t);
    for(l=0;l<t;l++){
        scanf("%d",&n);
        for(m=0;m<n;m++)
            scanf("%d",&c[m]);
        sort(c,n);
        //for(i=0;i<n;i++)
        // printf("%d\n",c[i]);
        for(i=0;i<1000;i++)
          for(j=0;j<20;j++) arr[i][j] = 0;
        inttobin(c,n,arr);
        
        printf("Case #%d: ",l+1);
        find(arr,c,n);
        /*for(m=0;m<n;m++){
        for(i=0;i<20;i++)
           printf("%d",arr[m][i]);
        printf("\n");
        }*/
        
        
    }
    return 0;
}

void sort(int c[],int n){
    int i,j,tmp;
    for(i=0;i<n;i++)
        for(j=i+1;j<n;j++)
            if(c[i]<c[j]) 
            {
                tmp = c[i];
                c[i] = c[j];
                c[j] = tmp;
            }
}

void inttobin(int c[],int n,int arr[][20]){
    int i,j,tmp;
    for(i=0;i<n;i++){
        tmp = c[i];
        for(j=19;tmp>0;j--){
            arr[i][j] = tmp%2;
            tmp/=2;             
        }
    }
}

void find(int arr[][20],int c[],int n){
     int i,j,k,tmp=0,sum=0;
     bool check=true;
     
     for(i=0;i<20;i++){
       for(j=0;j<n;j++)
          tmp+= arr[j][i];
       if(tmp%2==1){
          check = false;
          break;
       }
     } 
     if(check==false)printf("NO\n");
     else{
       for(i=0;i<n-1;i++)
         sum +=  c[i];
       printf("%d\n",sum);  
     }                        
}
