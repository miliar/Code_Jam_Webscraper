#include <stdio.h>
#include <string.h>
#include <iostream>

using namespace std;

int main()
{
//    freopen("inA1.in","r",stdin);
//    freopen("outA1.txt","w",stdout);
    int T,ncase = 0,c[5],r[5],d[2];
    char str[6];
    scanf("%d",&T);
    while(T--)
    {
        bool has_point = false;
        memset(c,0,sizeof(c));
        memset(r,0,sizeof(r));
        memset(d,0,sizeof(d));
        for(int i=0;i<4;i++)
        {
            scanf("%s",str);
            for(int j=0;str[j];j++)
            {
                if(str[j] == 'T')
                    continue;
                if(str[j] == '.')
                {
                    has_point = true;
                    r[i] = -100;
                    c[j] = -100;
                    if(i == j)
                        d[0] = -100;
                    if(i+j == 3)
                        d[1] = -100;
                    continue;
                }
                r[i] += str[j]=='X' ? 1 : -1;
                c[j] += str[j]=='X' ? 1 : -1;
                if(i==j)
                    d[0] += str[j]=='X' ? 1 : -1;
                if(i+j == 3)
                    d[1] += str[j]=='X' ? 1 : -1;
            }
        }
        int ans = 0;
        for(int i=0;i<4;i++)
        {
            if(r[i]==3 || r[i]==4 || c[i]==3 || c[i]==4)
                ans = 1;
            if(r[i]==-3 || r[i]==-4 || c[i]==-3 || c[i]==-4)
                ans = -1;
        }
        if(d[0]==3 || d[0]==4 || d[1]==3 || d[1]==4)
            ans = 1;
        if(d[0]==-3 || d[0]==-4 || d[1]==-3 || d[1]==-4)
            ans = -1;
        printf("Case #%d: ",++ncase);
        if(!ans)
            puts(has_point?"Game has not completed":"Draw");
        else
            puts(ans>0?"X won":"O won");
    }
    return 0;
}
