#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int a[1000];
bool b;
int max;

void separate(int i,int patrick1,int patrick2,int sean1,int sean2,int n){
    if(i==n){
        if(patrick1==patrick2&&patrick1!=0) 
        {
            sean1 = sean1 > sean2 ? sean1 : sean2;
            if(max<sean1) max = sean1;
            b=true;
        } 
    }
    else{
        separate(i+1,patrick1^a[i],patrick2^a[i],sean1,sean2+a[i],n);
        separate(i+1,patrick1,patrick2,sean1+a[i],sean2,n);
    }
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,k,i,j,n;
    scanf("%d",&t);
    for(k=0;k<t;k++){
        scanf("%d",&n);
        b=false;
        max = 0;
        int sum=0;
        for(i=0;i<n;i++){
            scanf("%d",&a[i]);
            sum^=a[i]; 
        }
        printf("Case #%d: ",k+1);
        separate(0,0,sum,0,0,n);
        if(!b) printf("NO\n");
        else printf("%d\n",max);
    }
    return 0;
    
}
