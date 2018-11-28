#include<iostream>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,k;
    int x;
    scanf("%d",&t);
    for(x=0;x<t;x++)
    {
                    scanf("%d%d",&n,&k);
                    if((k+1)%(1<<n)==0)
                    printf("Case #%d: ON\n",x+1);
                    else
                    printf("Case #%d: OFF\n",x+1);
                    }
    //scanf(" ");
    return 0;
    }
