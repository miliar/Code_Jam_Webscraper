#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>

using namespace std;

int L,D,N,i,j,k,p,val;
string data[5009],s[19];
char c;
bool fix[5009],b;

main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d%d%d%c",&L,&D,&N,&c);
    for(i=0;i<D;i++)
    {
        data[i]="";
        for(j=0;j<L;j++)
        {
            scanf("%c",&c);
            data[i]+=c;
        }
        scanf("%c",&c);
    }
    for(i=0;i<N;i++)
    {
        val=D;
        for(j=0;j<L;j++)
        {
            s[j]="";
            scanf("%c",&c);
            if(c=='(')
            {
                while(c!=')')
                {
                    scanf("%c",&c);
                    if(c==')') break;
                    s[j]+=c;
                }
            } else s[j]+=c;
        }
        scanf("%c",&c);
        memset(fix,true,D);
        for(j=0;j<L;j++)
        {
            for(k=0;k<D;k++)
            {
                b=false;
                for(p=0;p<s[j].size();p++)
                    if(data[k][j]==s[j][p]) { b=true; break; }
                if(fix[k]==true && b==false) { val--; fix[k]=false; }
            }
        }
        printf("Case #%d: %d\n",i+1,val);
    }
}
