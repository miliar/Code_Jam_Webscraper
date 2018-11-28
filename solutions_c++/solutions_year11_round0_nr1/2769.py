//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;


int abs (int a,int b)
{
    if(a>b)return a-b;
    return b-a;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int kas,cas;
    cin>>kas;
    for(cas=1;cas<=kas;cas++)
    {
        int n,m,p=1,q=1,cur=0,mp=0,mq=0;
        cin>>n;
        string ch;
        for(int i=0;i<n;i++)
        {
            cin>>ch>>m;
            if(ch[0]=='O')
            {
                mp+=abs(p,m);
                p=m;
                mp++;
                if(cur+1>mp)
                {
                    mp=cur+1;
                    cur++;
                }
                else cur=mp;
            }
            else{
                mq+=abs(q,m);
                q=m;
                mq++;
                if(cur+1>mq)
                {
                    mq=cur+1;
                    cur=cur+1;
                }
                else cur=mq;
            }
        }
        //cur=max(cur,max(mp,mq));
        printf("Case #%d: %d\n",cas,cur);
    }
}
