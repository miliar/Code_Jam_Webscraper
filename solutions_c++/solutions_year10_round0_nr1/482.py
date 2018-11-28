#include <iostream>

using namespace std;

int main()
{
    int t;
//freopen("A-large.in","r",stdin);
//freopen("E:/out.txt","w",stdout);
    scanf("%d",&t);
    for(int o = 1; o <= t; o++)
    {
       int n,k;
       scanf("%d %d",&n,&k);
       int r = 1<<n;
       printf("Case #%d: ",o);
       if(k % r == r-1) printf("ON\n");
       else printf("OFF\n");
    }
    return(0);
}
