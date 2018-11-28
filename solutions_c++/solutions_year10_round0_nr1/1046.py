#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;

int main()
{
     freopen("A-large.in","r",stdin);
     freopen("out.txt","w",stdout);
    int t,n,k,i,flag;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        scanf("%d%d",&n,&k);
        k%=(long long)pow(2,n);
        printf("Case #%d: ",i);
        if(k==(long long)pow(2,n)-1) printf("ON\n");
        else printf("OFF\n");
    }
   // system("pause");
    return 0;
}
