#include <iostream>
using namespace std;
#define M 102
int box[M][M];
int nb[M][M];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int c;
    cin>>c;
    for(int ca=1;ca<=c;++ca)
    {
        int rst=1;
        int r;
        int x1,x2,y1,y2;
        memset(box, 0, sizeof(int)*M*M);
        memset(nb,0,sizeof(int)*M*M);
        cin>>r;
        for(int i=0;i<r;++i)
        {
            cin>>x1>>y1>>x2>>y2;
            for(int x=x1;x<=x2;++x)
            {
                for(int y=y1;y<=y2;++y)
                {
                    box[y][x]=1;
                }
            }
        }
        int over=0;
        while(1)
        {
            /*
            for(int i=0;i<7;++i)
            {
                for(int j=0;j<7;++j)
                    cout << box[i][j];
                cout<<endl;
            }
            cout << endl;
            */
            over=1;
            nb[0][0]=0;
            for(int j=1;j<M;++j)
            {
                if(box[0][j-1])
                {
                    nb[0][j]=box[0][j];
                    over=0;
                }
                else nb[0][j]=0;
            }
            for(int j=1;j<M;++j)
            {
                if(box[j-1][0])
                {
                    nb[j][0]=box[j][0];
                    over=0;
                }
                else nb[j][0]=0;
            }
            for(int i=1;i<M;++i)
            {
                for(int j=1;j<M;++j)
                {
                    if(box[i-1][j]==1 && box[i][j-1]==1)
                    {
                        nb[i][j]=1;
                        over=0;
                    }
                    else if(box[i-1][j]==0&&box[i][j-1]==0)
                    {
                        nb[i][j]=0;
                    }
                    else if(box[i][j])
                    {
                        over=0;
                        nb[i][j]=1;
                    }
                    else nb[i][j]=0;
                }
            }
            
            if(over)break;
            memcpy(box, nb, sizeof(int)*M*M);
            ++rst;
        }
        cout << "Case #"<<ca<<": " <<rst<<endl;
    }
    return 0;
}
