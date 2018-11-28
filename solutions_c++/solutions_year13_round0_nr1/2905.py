#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int a[5][5];
int dir[8][2]={1,0,-1,0,0,1,0,-1,-1,-1,1,1,1,-1,-1,1};

int expand(int p ,int q, int l)
{
    int ans1=0;
    int x = p + dir[l][0],y=q+dir[l][1];
    while ((x>=0)&&(x<4)&&(y>=0)&&(y<4)&&((a[x][y]==a[p][q])||(a[x][y]==3)))
    {
          ans1++;
          x = x+dir[l][0],y=y+dir[l][1];
    }
    return ans1;
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;char ch;
    int k;
    scanf("%d ",&t);
    int t1 = 1;
    int i,j;
    while (t--)
    {
        int empty = 0;
        bool f=false;
        for (i = 0;i<4;++i)
        {
            for (j=0;j<4;++j)
            {
                scanf("%c",&ch);
                if (ch == 'X')
                {
                       a[i][j]=1;
                }
                else if (ch == 'O')
                {
                       a[i][j]=2;
                }
                else if (ch == 'T')
                {
                       a[i][j]=3;
                }
                else
                {
                    a[i][j]=0, empty ++;
                }
            }
            scanf(" ");
        }
        for (i = 0;i<4;++i)
        {
            for (j=0;j<4;++j)
            {
                if ((a[i][j]==3)||(a[i][j]==0)) continue;
                for (k=0;k<8;k+=2)
                {
                    int ans =  1+expand(i,j,k)+expand(i,j,k+1);
                    if (ans>=4)
                    {
                        if (a[i][j]==1)
                            printf("Case #%d: X won\n",t1);
                            else printf("Case #%d: O won\n",t1);
                            f=true;
                            break;
                    }
                }
                if (f) break;
            }
            if (f) break;
        }
        if (!f)
        {
           if (empty) printf("Case #%d: Game has not completed\n",t1);
           else printf("Case #%d: Draw\n",t1);
        }
        t1++;
    }
    return 0;
}
