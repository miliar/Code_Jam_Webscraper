#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>
#include<math.h>
using namespace std;
char mymap[10][10];
struct node
{
    int x;
    int o;
    int t;
}col[10],row[10];
int main()
{
    int n;
    int i,j,casee;
    int res;
    bool hasDot;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    while(scanf("%d",&n)!=EOF)
    {
        for(casee=1;casee<=n;casee++)
        {
            getchar();
            res=-1;
            hasDot=false;
            for(i=0;i<4;i++)
            {
                scanf("%s",&mymap[i]);
                for(j=0;j<4;j++)
                    if(mymap[i][j]=='.')
                        hasDot=true;
            }
            memset(row,0,sizeof(row));
            memset(col,0,sizeof(col));
            
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(mymap[i][j]=='X')
                    {
                        row[i].x++;
                        col[j].x++;
                    }
                    else if(mymap[i][j]=='O')
                    {
                        row[i].o++;
                        col[j].o++;
                    }
                    else if(mymap[i][j]=='T')row[i].t++,col[j].t++;
                }
            }
            for(i=0;i<4;i++)
            {
                if((row[i].o+row[i].t==4)||col[i].o+col[i].t==4)
                {
                    res=1;
                    break;
                }
                if((row[i].x+row[i].t==4)||col[i].x+col[i].t==4)
                {
                    res=2;
                    break;
                }
            }
            int oo,tt,xx;
            oo=tt=xx=0;
            for(i=0;i<4;i++)
            {
                if(mymap[i][i]=='O') oo++;
                else if(mymap[i][i]=='X') xx++;
                else if(mymap[i][i]=='T')tt++;
                if(oo+tt==4)
                {
                    res=1;
                    break;
                }if(xx+tt==4)
                {
                    res=2;
                    break;
                }
            }
            oo=xx=tt=0;
            for(i=0;i<4;i++)
            {
                if(mymap[i][3-i]=='O') oo++;
                else if(mymap[i][3-i]=='X') xx++;
                else if(mymap[i][3-i]=='T')tt++;
                if(oo+tt==4)
                {
                    res=1;
                    break;
                }if(xx+tt==4)
                {
                    res=2;
                    break;
                }
            }
            if(res==1)
            {
                printf("Case #%d: O won\n",casee);
                continue;
            }else if(res==2)
            {
                printf("Case #%d: X won\n",casee);
                continue;
            }else if(!hasDot) printf("Case #%d: Draw\n",casee);
            else printf("Case #%d: Game has not completed\n",casee);
        } 
    }
    return 0;
}