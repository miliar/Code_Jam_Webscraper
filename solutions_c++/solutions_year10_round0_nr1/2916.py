#include<iostream>
#include<cmath>
using namespace std;
int main()
{
    int cases;
    scanf("%d",&cases);
    int n,k;
    for(int ca=1;ca<=cases;ca++)
    {
        scanf("%d%d",&n,&k);
        int p=(int)pow(2.0,n);
        printf("Case #%d: ",ca);
        if(k%p==p-1)
        puts("ON");
        else
        puts("OFF");
    }
}
        
