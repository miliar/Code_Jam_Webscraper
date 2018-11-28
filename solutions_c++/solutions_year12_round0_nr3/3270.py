#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int power(int a,int b){
    int ans=1;
    for(int i=0;i<b;i++){
        ans*=a;
    }
    return ans;
}
int check(int n,int max,int digit){
    int a=n;
    int ans=0;
    //printf("%d ",n);
    int t,temp;
    for(int i=1;i<digit;i++){
        temp=(a%10);
        t=power(10,digit-1);
        //printf("%d+(%d*%d)=",a/10,temp,t);
        a=(a/10)+(temp*t);
        //printf("%d ",a);
        if(a>n&&a<=max)ans++;
    }
    //printf("%d \n",ans);
    return ans;
}
int numDigit(int n){
    int d=1;
    while(1){
        if(n<power(10,d))break;
        else d++;
    }
    return d;
}
int main(){
    int t;
    int min,max,ans,digit;
    scanf("%d",&t);
    for(int j=0;j<t;j++){
        ans=0;
        scanf("%d %d",&min,&max);
        for(int i=min;i<max;i++){
            digit=numDigit(i);
            //printf("digit=%d\n",digit);
            ans+=check(i,max,digit);
        }
        printf("Case #%d: %d\n",j+1,ans);
    }
    return 0;
}
