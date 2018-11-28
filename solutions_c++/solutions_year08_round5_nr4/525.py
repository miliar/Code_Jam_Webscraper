#include <iostream>
using namespace std;
int N,R,W,H;
const int dx[2]={1,2};
const int dy[2]={2,1};
bool map[200][200];
int res[200][200];
int main()
{
    int Ni,i,r,c;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    cin>>N;
    for (Ni=1;Ni<=N;Ni++)
    {
        cin>>H>>W>>R;
        memset(map,true,sizeof(map));
        memset(res,0,sizeof(res));
        for (i=0;i<R;i++)
        {
            cin>>r>>c;
            map[r][c]=false;
        }
        res[1][1]=1;
        for (r=1;r<=H;r++)
            for (c=1;c<=W;c++) if (res[r][c]!=0)
                for (i=0;i<2;i++)
                    if (dx[i]+r<=H && dy[i]+c<=W && map[r+dx[i]][c+dy[i]])
                        res[r+dx[i]][c+dy[i]]=(res[r][c]+res[r+dx[i]][c+dy[i]])%10007;
        cout<<"Case #"<<Ni<<": "<<res[H][W]<<endl;
    }
    return 0;
}
