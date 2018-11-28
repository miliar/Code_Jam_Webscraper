#include <iostream>

using namespace std;

int main()
{
    freopen("in2.txt","r",stdin);
    freopen("out.txt","w",stdout);
    unsigned long long n,m,k,val,i;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>m>>k;
        val=1<<m;
        if(k==0)
            printf("Case #%d: OFF\n",i+1);
        else
            if((k+1)%val==0)
                printf("Case #%d: ON\n",i+1);
            else
                printf("Case #%d: OFF\n",i+1);
    }
    return 0;
}
