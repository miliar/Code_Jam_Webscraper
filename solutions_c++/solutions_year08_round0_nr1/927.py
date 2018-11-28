#include<stdio.h>
#include<string>
#include<iostream>
#include<set>

using namespace std;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cases,s,q,i,ii,an,uds;
    char f[102];
    string kw;//key word
    
    scanf("%d",&cases);
    fprintf(stderr,"cases=%d\n",cases);
    //while(1);
    for(ii=1;ii<=cases;ii++)
    {
        //fprintf(stderr,"ii=%d\n",ii);
        set<string> ud;
        an=0;
        scanf("%d\n",&s);
        for(i=1;i<=s;i++)gets(f);
        scanf("%d\n",&q);
        uds=0;
        for(i=1;i<=q;i++)
        {
            gets(f);
            kw=f;
            if(ud.find(kw)==ud.end())
            {
                if(uds+1==s)an++,ud.clear(),uds=0;
                uds++;
                ud.insert(kw);
            }
            //fprintf(stderr,"i=%d kw=%s uds=%d\n",i,kw.c_str(),uds);
        }
        printf("Case #%d: %d\n",ii,an);
    }
    //while(1);
    return 0;
}
