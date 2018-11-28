#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int n,k;
    int i,j;
    int tmp;
    cin>>t;
    int cases=1;
    while(t--)
    {
        int flag=0;
        scanf("%d%d",&n,&k);
        tmp = (1<<n);
        k=k%tmp;
//        cout<<k<<" "<<tmp<<endl;
        if(k+1==tmp)
            flag=1;
        else
            flag=0;
        if(flag)
            printf("Case #%d: ON\n",cases++);
        else
        printf("Case #%d: OFF\n",cases++);
    }
}
