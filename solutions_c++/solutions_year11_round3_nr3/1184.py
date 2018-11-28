#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main(){
    int cases,k,i,j;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    while(~scanf("%d",&cases)) {
        int n,l,h;
        int fre[10010];
        for(k=1; k<=cases; k++){
            scanf("%d%d%d",&n,&l,&h);
            for(i=0; i<n; i++){
                scanf("%d",&fre[i]);
            }
            bool flag = false;
            int ans = 0;
            for(i=l;i<=h;i++){
                flag = false;
                for(j=0;j<n;j++){
                    if(i%fre[j] != 0&&fre[j]%i!=0){
                        flag = true;
                        break;
                    }
                }
                if(!flag){
                    ans = i;
                    break;
                }
            }
            printf("Case #%d: ",k);
            if(!flag){
                printf("%d\n",ans);
            }
            else{
                printf("NO\n");
            }
        }
    }
    return 0;
}
