#include<iostream>
using namespace std;
int map[105][105]; 
int main()
{
    int casen; 
    int h,w,r; 
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d%d%d",&h,&w,&r);
        int x,y;
        memset(map,0,sizeof(map));
        map[1][1]=1; 
        for (int i=1;i<=r;i++)
        {
            scanf("%d%d",&x,&y);
            map[x][y]=-1;
        }
        for (int i=1;i<=h;i++)
          for (int j=1;j<=w;j++)
            if (map[i][j]!=-1)
            {
                              if (i-1>0&&j-2>0)map[i][j]+=map[i-1][j-2];
                              if (i-2>0&&j-1>0)map[i][j]+=map[i-2][j-1];
                              map[i][j]=map[i][j]%10007; 
            }
            else map[i][j]=0;
        printf("Case #%d: %d\n",casei,map[h][w]);
    }
    return 0;
}
 
