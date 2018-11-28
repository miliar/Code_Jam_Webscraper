#include<stdio.h>
#include<string.h>
#include<iostream>
#define MAX 1000001
using namespace std;
int prime[200000],P,power[200000];
void init(){
    int i,j,k,flag;
    prime[0]=2,k=1;
    for(i=3;i<=MAX;i+=2){
        flag=1;
        for(j=0;j<k&&prime[j]<=i/prime[j];j++)
            if(i%prime[j]==0){
                flag=0;
                break;
            }
        if(flag)prime[k++]=i;
    }
    P=k;
}
int main(){
    int C,Case=1;
    long long n,min,max;
    init();
    scanf("%d",&C);
    while(C--){
        cin>>n;
        if(n==1){
            printf("Case #%d: 0\n",Case++);
            continue;
        }
        memset(power,0,sizeof(power));
        max=min=0;
        for(int i=0;i<P&&prime[i]<=n/prime[i];i++){
            long long temp=n;
            while(temp>=prime[i]){
                temp/=prime[i];
                power[i]++;
            }
            //cout<<prime[i]<<' '<<power[i]<<endl;
            max+=power[i];
            min++;
        }
        printf("Case #%d: ",Case++);
        cout<<max-min+1<<endl;
    }
}
