#include <iostream>
#include <cstdio>

using namespace std;

int t,s,p,n,cas;
int res,v1,v2;

inline int min(int a,int b)
{
    if (a<b) return a;
    return b;
}

int main()
{
    int i,tmp;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d %d %d",&n,&s,&p);
        v1=0;v2=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&tmp);
            if ((p+p+p-2)<=tmp && tmp<=30)
                v1++;
            else if (tmp==(p+p+p-3)&&p-2>=0)
                v2++;
            else if (tmp==(p+p+p-4)&&p-2>=0)
                v2++;
        }
        res=v1+min(v2,s);
        printf("Case #%d: %d\n",cas,res);
    }
    return 0;
}
