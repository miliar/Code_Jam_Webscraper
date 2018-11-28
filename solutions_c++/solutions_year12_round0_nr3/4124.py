#include<stdio.h>

int getLen(int x){
    int n=1;
    while((x=x/10)>0)n++;
    return n;
}
int pow(int b,int p){
    int i;
    int ans=1;
    for(i=0;i<p;i++)ans*=b;
    return ans;
}
int main(){
    int t;
    scanf("%d",&t);
    int i;
    for(i=0;i<t;i++){
        int num=0;
        int min,max;
        scanf("%d %d",&min,&max);
        int j;
        for(j=min;j<=max;j++){
            int k=0;
            if(getLen(j)%2==0){
                int a = j/(pow(10,getLen(j)/2));
                int b = j%(pow(10,getLen(j)/2));
                if(a==b) k=getLen(j)/2;
            }
            int b=j;
            while(k<(getLen(j)-1)){
                b=(pow(10,(getLen(j)-1)))*(b%10)+b/10;
                k++;
                if(b>=min&&b<=max&&j!=b){num++;}
            }
        }
        printf("Case #%d: %d\n",i+1,num/2);
    }
}

