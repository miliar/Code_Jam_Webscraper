#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int pd,pg;
long long n;

bool check()
{
    for(int i=1;i<=n;++i)
    {
        if(i*pd%100==0)return true;
    }
    return false;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cases=1;
    scanf("%d",&t);
    while(t--)
    {
        cin>>n>>pd>>pg;
        printf("Case #%d: ",cases++);
        if(pg==100)
        {
            if(pd==100)
                puts("Possible");
            else
                puts("Broken");
        }
        else if(pg==0)
        {
            if(pd==0)
                puts("Possible");
            else
                puts("Broken");
        }
        else if(n>=100)
        puts("Possible");
        else
        {
            if(check())puts("Possible");
            else puts("Broken");
        }
    }
    return 0;
}
