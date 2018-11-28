#include <iostream>

using namespace std;

int t,n,i,k;
unsigned int mic[35];

int main()
{
    for(i=1;i<=30;i++)
    {
        mic[i]=2*mic[i-1]+1;
    }
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&n,&k);
        printf("Case #%d: ",i);
        if(k%(mic[n]+1)==mic[n])
        {
            printf("ON\n");
        }
        else
        {
            printf("OFF\n");
        }
    }
    return 0;
}
