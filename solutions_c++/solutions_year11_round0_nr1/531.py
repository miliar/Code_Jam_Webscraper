#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

int n,p,lasto,lastb,ans,op,last,cases=1;
char c[2];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        lasto=lastb=1;
        op=-1;
        ans=last=0;
        for(int i=0;i<n;++i)
        {
            scanf("%s%d",c,&p);
            if(c[0]=='O')
            {
                if(op==0)
                {
                    ans+=abs(p-lasto);
                    last+=abs(p-lasto);
                }
                else
                {
                    op=0;
                    if(abs(p-lasto)>last)
                    {
                        ans+=abs(p-lasto)-last;
                        last=abs(p-lasto)-last;
                    }
                    else
                    last=0;
                }
                ans++;
                last++;
                lasto=p;
            }
            else
            {
                if(op==1)
                {
                    ans+=abs(p-lastb);
                    last+=abs(p-lastb);
                }
                else
                {
                    op=1;
                    if(abs(p-lastb)>last)
                    {
                        ans+=abs(p-lastb)-last;
                        last=abs(p-lastb)-last;
                    }
                    else
                    last=0;
                }
                ans++;
                last++;
                lastb=p;
            }
//            cout<<ans<<endl;
        }
        printf("Case #%d: %d\n",cases++,ans);
    }
    return 0;
}
