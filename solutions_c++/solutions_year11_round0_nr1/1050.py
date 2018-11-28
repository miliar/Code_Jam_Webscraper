#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int main()
{
    int t,T,n,i,ox,ot,bx,bt,j;
    char s[2];
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        ox=bx=1;
        ot=bt=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s%d",s,&j);
            if(s[0]=='O')
            {
                ot+=abs(ox-j)+1;
                ox=j;
                ot=max(ot,bt+1);
            }            
            else
            {
                bt+=abs(bx-j)+1;
                bx=j;
                bt=max(bt,ot+1);
            }            
        }
        printf("Case #%d: %d\n",t,max(ot,bt));
    }
//system("pause");

    return 0;
}
