#include<iostream>
#include<cstdio>
using namespace std;

int data[10000];

int main(){
    int T,n,cas=1;
    int temp,ans,min;
    
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        
        temp = ans = 0;
        min = 1e7;
        
        for(int i=0;i<n;i++){
            scanf("%d",&data[i]);
            temp ^= data[i];
            ans += data[i];
            min = min>data[i]?data[i]:min;
        }
        
        if(temp != 0){
            printf("Case #%d: NO\n",cas++);
        }else{
            printf("Case #%d: %d\n",cas++,ans-min);
        }
    }
    return 0;
}
