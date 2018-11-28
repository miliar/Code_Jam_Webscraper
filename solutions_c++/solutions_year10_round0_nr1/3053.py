#include<iostream>
using namespace std;

int main()
{
    freopen("C:\\Users\\lenovo\\Desktop\\A.in","r",stdin);
    freopen("C:\\Users\\lenovo\\Desktop\\AC.out","w",stdout);
    int test,t=0;
    scanf("%d",&test);
    int n,k;
    while(test--)
    {
        scanf("%d%d",&n,&k);
        printf("Case #%d: ",++t);
        if((k+1)%(1<<n)==0)
        puts("ON");
        else
        puts("OFF");
    }
}
