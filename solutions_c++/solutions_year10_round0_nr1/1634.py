#include<iostream>
using namespace std;

long n,k,t;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
            scanf("%d%d",&n,&k);
            bool flag=true;
            for(int j=0;j<n;j++)
                    if(((k>>j)&1)==0) { flag=false; break; }
            printf("Case #%d: ",i);
            if(flag) printf("ON\n");
                else printf("OFF\n");
    }
    return 0;
}
