#include<stdio.h>
#include<iostream>
#include<map>
#include<cstring>

using namespace std;

char ss[1000002],s[1000002];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int ii,cases,n,m,i,j,len,an;
    map<const string,int> ud;
    
    scanf("%d",&cases);
    string nn;
    
    for(ii=1;ii<=cases;ii++)
    {
        ud.clear();
        an=0;
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
        {
            scanf("%s",ss);
            len=0;
            s[len++]='/';
            for(j=1;ss[j];j++)
            {
                if(ss[j]=='/')
                {
                    s[len]=0;
                    //if(map[string(s)]==0)an++;
                    ud[string(s)]=1;
                    s[len++]='/';
                }
                else
                {
                    s[len++]=ss[j];
                }
            }
            s[len]=0;
            //if(map[string(s)]==0)an++;
            ud[string(s)]=1;
        }
        for(i=1;i<=m;i++)
        {
            scanf("%s",ss);
            len=0;
            s[len++]='/';
            for(j=1;ss[j];j++)
            {
                if(ss[j]=='/')
                {
                    s[len]=0;
                    if(ud[string(s)]==0)an++;
                    ud[string(s)]=1;
                    s[len++]='/';
                }
                else
                {
                    s[len++]=ss[j];
                }
            }
            s[len]=0;
            if(ud[string(s)]==0)an++;
            ud[string(s)]=1;
        }
        printf("Case #%d: %d\n",ii,an);
    }
    
    
    
    fprintf(stderr,"END\n");
    while(1);
    return 0;
}
