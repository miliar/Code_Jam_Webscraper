#include <iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>


int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,k,i,j,co,cx;bool T;char p[6][6];
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        bool full=true;
        for(i=0;i<4;i++)
        {
            scanf("%s",p[i]);
        }
        for(i=0;i<4;i++)
        {

        co=0;cx=0;T=false;
           for(j=0;j<4;j++)
           {
               if(p[i][j]=='.')
               full=false;
               else if(p[i][j]=='O')
               co++;
               else if(p[i][j]=='X')
               cx++;
               else if(p[i][j]=='T')
               T=true;
           }
           if(co==4||(co==3&&T==true))
           {
               printf("Case #%d: O won\n",k);
               goto end;
           }
           else if(cx==4||(cx==3&&T==true))
           {
               printf("Case #%d: X won\n",k);
               goto end;
           }
        }

        for(j=0;j<4;j++)
        {
            co=0;cx=0;T=false;
           for(i=0;i<4;i++)
           {
               if(p[i][j]=='.')
               full=false;
               else if(p[i][j]=='O')
               co++;
               else if(p[i][j]=='X')
               cx++;
               else if(p[i][j]=='T')
               T=true;
           }
           if(co==4||(co==3&&T==true))
           {
               printf("Case #%d: O won\n",k);
               goto end;
           }
           else if(cx==4||(cx==3&&T==true))
           {
               printf("Case #%d: X won\n",k);
               goto end;
           }
        }
        co=0;cx=0;T=false;
        for(i=0;i<4;i++)
        {
            if(p[i][i]=='.')
               full=false;
               else if(p[i][i]=='O')
               co++;
               else if(p[i][i]=='X')
               cx++;
               else if(p[i][i]=='T')
               T=true;

        }
        if(co==4||(co==3&&T==true))
           {
               printf("Case #%d: O won\n",k);
               goto end;
           }
           else if(cx==4||(cx==3&&T==true))
           {
               printf("Case #%d: X won\n",k);
               goto end;
           }
		  co=0;cx=0;T=false;
           for(i=0;i<4;i++)
        {
            if(p[i][3-i]=='.')
               full=false;
               else if(p[i][3-i]=='O')
               co++;
               else if(p[i][3-i]=='X')
               cx++;
               else if(p[i][3-i]=='T')
               T=true;

        }
        if(co==4||(co==3&&T==true))
           {
               printf("Case #%d: O won\n",k);
               goto end;
           }
           else if(cx==4||(cx==3&&T==true))
           {
               printf("Case #%d: X won\n",k);
               goto end;
           }
        if(full==true)
        printf("Case #%d: Draw\n",k);
        else
        printf("Case #%d: Game has not completed\n",k);

      end:;
    }
    return 0;
}
