#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int cases;
    char map[5][5];
    int i,j;
    int t1,t2;
    int t;
    int ans;
    scanf("%d",&cases);
    t=1;
    while(cases--)
    {
        printf("Case #%d: ",t);
        t++;
        ans=0;
        for(i=0;i<4;++i)
        {
            scanf("%s",map[i]);
        }
        for(i=0;i<4;++i)
        {
            if(ans>0)
                break;
            t1=0;
            t2=0;
            for(j=0;j<4;++j)
            {
                if(map[i][j]=='X')
                    t1++;
                if(map[i][j]=='O')
                    t2++;
                if(map[i][j]=='T')
                {
                    t1++;
                    t2++;
                }
            }
            if(t1==4)   ans=1;
            if(t2==4)   ans=2;
        }
        for(i=0;i<4;++i)
        {
            if(ans>0)
                break;
            t1=0;
            t2=0;
            for(j=0;j<4;++j)
            {
                if(map[j][i]=='X')
                    t1++;
                if(map[j][i]=='O')
                    t2++;
                if(map[j][i]=='T')
                {
                    t1++;
                    t2++;
                }
            }
            if(t1==4)   ans=1;
            if(t2==4)   ans=2;
        }
        t1=0;
        t2=0;
        for(i=0;i<4;++i)
        {
            if(ans>0)
                break;
            if(map[i][i]=='X')
                t1++;
            if(map[i][i]=='O')
                t2++;
            if(map[i][i]=='T')
            {
                t1++;
                t2++;
            }
        }
        if(t1==4)   ans=1;
        if(t2==4)   ans=2;
        t1=0;
        t2=0;
        for(i=0;i<4;++i)
        {
            if(ans>0)
                break;
            if(map[i][3-i]=='X')
                t1++;
            if(map[i][3-i]=='O')
                t2++;
            if(map[i][3-i]=='T')
            {
                t1++;
                t2++;
            }
        }
        if(t1==4)   ans=1;
        if(t2==4)   ans=2;
//        printf("ans=%d\n",ans);
        if(ans==0)
        {
            if(ans>0)
                break;
            for(i=0;i<4;++i)
            {
                for(j=0;j<4;++j)
                {
                    if(map[i][j]=='.')
                    {
                        ans=-1;
                        break;
                    }
                }
            }
        }
        if(ans==0)  printf("Draw\n");
        if(ans==-1)  printf("Game has not completed\n");
        if(ans==1)  printf("X won\n");
        if(ans==2)  printf("O won\n");
    }
    return 0;
}
