#include <cstdio>
#include <cstring>
#include <iostream>
#include <iostream>

using namespace std;

int l,h,a[11000],n;
bool flag;

bool check(int num)
{
    for(int i=0;i<n;++i)
    {
        if(a[i]%num!=0&&num%a[i]!=0)return false;
    }
    return true;
}

int main()
{
    freopen("in.txt","r",stdin);
     freopen("out.txt","w",stdout);
    int t,cases=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d%d",&n,&l,&h);
        for(int i=0;i<n;++i)
        {
            scanf("%d",&a[i]);
        }
        flag=false;
        printf("Case #%d: ",cases++);
        for(int i=l;i<=h;++i)
        {
            if(check(i))
            {
                printf("%d\n",i);
                flag=true;
                break;
            }
        }
        if(!flag)printf("NO\n");
    }
    return 0;
}

