//kbriut@yahoo.com
//GNU:Ming@Code:Blocks
#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
#define S 1005
int main(){
    //freopen("1.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int i,j,n,t,txt=0;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        int ans=0;
        for(i=1;i<=n;i++){
            scanf("%d",&j);
            if(j!=i)ans++;
        }
        printf("Case #%d: %d.000000\n",++txt,ans);
    }
    return 0;
}
