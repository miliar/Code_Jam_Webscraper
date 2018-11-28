#include <iostream>
#include <cstdlib>
#include <map>
#include <string>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    map<string,int> mp;
    map<string,int>::iterator it;
    char eng[101][111],qu[1001][101],temp;
    int sen=1,cas,S,Q,t,tt,max,swi;
    scanf("%d%c",&cas,&temp);
    while(sen++<=cas)
    {
        scanf("%d%c",&S,&temp);
        for(t=0;t<S;t++)
            gets(eng[t]);
        scanf("%d%c",&Q,&temp);
        for(t=0;t<Q;t++)
            gets(qu[t]);
        max=0;swi=0;
        if(Q==0)
        {
            printf("Case #%d: 0\n",sen-1);
            continue;
        }
        while(1)
        {
            mp.clear();
            for(t=0;t<S;t++)
                mp[(string)eng[t]]=0x7fffffff;
            for(t=max;t<Q;t++)
            {
                if(mp[(string)qu[t]]>t)
                    mp[(string)qu[t]]=t;
            }
            for(it=mp.begin();it!=mp.end();it++)
                if(it->second>max)
                    max=it->second;
            if(max>=Q) break;
            swi++;
        }
        printf("Case #%d: %d\n",sen-1,swi);
    }
    return 0;
}
