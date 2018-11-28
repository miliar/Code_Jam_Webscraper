#include <iostream>

using namespace std;
int map[225][225];
int tmap[225][225];
int lef,up,down,rig;
int ans;
bool inbound(int x,int y)
{
    return x>=up&&x<=down&&y>=lef&&y<=rig;
}
void solve()
{
    ans=0;
    bool flag=1;
    while(flag)
    {
        int i,j;
//        for(i=1;i<=6;i++)
//        {
//            for(j=1;j<=6;j++)
//                cout<<map[i][j];
//            cout<<endl;
//        }
//        cout<<endl;
        ans++;
        flag=0;
        for(i=up;i<=down;i++)
            for(j=lef;j<=rig;j++)
            {
//                if((inbound(i-1,j)&&map[i-1][j])||(inbound(i,j-1)&&map[i][j-1]))
//                    tmap[i][j]=1;
//                else
//                    tmap[i][j]=0;
                    if(map[i][j])
                    {
                        if((inbound(i-1,j)&&map[i-1][j])||(inbound(i,j-1)&&map[i][j-1]))
                    tmap[i][j]=1;
                else
                    tmap[i][j]=0;
                    }
                    else
                    {
                        if((inbound(i-1,j)&&map[i-1][j])&&(inbound(i,j-1)&&map[i][j-1]))
                    tmap[i][j]=1;
                else
                    tmap[i][j]=0;
                    }
            }
        for(i=up;i<=down;i++)
            for(j=lef;j<=rig;j++)
            {
                if(tmap[i][j])
                {
                    map[i][j]=1;
                    flag=1;
                }
                else
                    map[i][j]=0;
            }
    }
}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("ttout.txt","w",stdout);
    int r;
    int t;
    int x1,x2,y1,y2;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        down=rig=0;
        lef=up=101;
        int i,j;
        memset(map,0,sizeof(map));
        scanf("%d",&r);
        while(r--)
        {
            scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
            down=max(down,y2);
            rig=max(rig,x2);
            lef=min(lef,x1);
            up=min(y1,up);
            for(i=y1;i<=y2;i++)
                for(j=x1;j<=x2;j++)
                {
                    map[i][j]=1;
                }
        }
        solve();
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
