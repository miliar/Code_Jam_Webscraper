#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int t,iii;
int n,i,j,k;
int x1,x2,y11,y2;
int cell[105][105][2];
int prev;
int now;
int chk;

int main()
{
    scanf("%d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%d",&n);
        prev=0;
        now=1;
        for(i=1;i<=100;i++)
        {
            for(j=1;j<=100;j++)
            {
                cell[i][j][prev]=0;
            }
        }
        for(i=1;i<=n;i++)
        {
            scanf("%d %d %d %d",&x1,&y11,&x2,&y2);
            for(j=x1;j<=x2;j++)
            {
                for(k=y11;k<=y2;k++)
                {
                    cell[j][k][prev]=1;
                }
            }
        }
        for(i=1;i<=100;i++)
        {
            for(j=1;j<=100;j++)
            {
                cell[i][j][now]=0;
            }
        }
        /*
        for(i=1;i<=10;i++)
        {
            for(j=1;j<=10;j++)
            printf("%d ",cell[i][j][prev]);
            printf("\n");
        }
        */
        for(k=1;;k++)
        {
            chk=1;
            for(i=1;i<=100;i++)
            {
                for(j=1;j<=100;j++)
                {
                    cell[i][j][now]=0;
                    if((cell[i][j][prev]==1&&((cell[i][j-1][prev]==1||cell[i-1][j][prev]==1)))||(cell[i][j-1][prev]==1&&cell[i-1][j][prev]==1))
                    {
                        //printf("%d %d\n",i,j);
                        cell[i][j][now]=1;
                        chk=0;
                    }
                }
            }
            /*
            for(i=1;i<=10;i++)
        {
            for(j=1;j<=10;j++)
            //printf("%d ",cell[i][j][now]);
            printf("\n");
        }
        */
            if(chk==1)
            break;
            now=1-now;
            prev=1-prev;
        }
        printf("Case #%d: %d\n",iii,k);
    }
	return 0;
}
