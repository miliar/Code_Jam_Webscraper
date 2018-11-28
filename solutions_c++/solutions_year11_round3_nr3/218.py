#include<stdio.h>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>
#include<set>
#include<map>
#include<vector>
using namespace std;
__int64 a[10000];
int main()
{
    freopen("C-small-attempt0.in.txt","r",stdin);
    freopen("1.txt","w",stdout);
    int Total;
    int i,j,n;__int64 L,H;
    scanf("%d",&Total);
    for(int Case=1;Case<=Total;Case++){
        printf("Case #%d: ",Case);
        scanf("%d%I64d%I64d",&n,&L,&H);
        for(i=0;i<n;i++){
            scanf("%I64d",&a[i]);
        }__int64 x;
        for( x=L;x<=H;x++){
            bool ok=1;
            for(i=0;i<n;i++){
                if(x%a[i]&&a[i]%x){ok=0;break;}                 
            } 
            if(ok){
                printf("%I64d\n",x);
                break;       
            }          
        }
        if(x>H)puts("NO");
    }
        
}
