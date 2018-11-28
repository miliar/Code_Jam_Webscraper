#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string>
#include <stdio.h>
using namespace std;

int N,M,D;
const int MN=555;

int vals[MN][MN];
int sumX[MN][MN];
int sumY[MN][MN];
int sumW[MN][MN];

void test()
{
    cin>>N>>M>>D;
    int i,j,k;
    char c;
    for(i=0;i<N;i++)
        for(j=0;j<M;j++)
        {
            cin>>c;
            vals[i][j]=c-'0';
            //cout<<vals[i][j]<<endl;
        }
    int cursumX=0;
    int cursumY=0;
    int cursumW=0;
    for(i=0;i<N;i++)
    {
        cursumX=0;
        cursumY=0;
        cursumW=0;
        for(j=0;j<M;j++)
        {
            cursumX+=vals[i][j]*i;
            cursumY+=vals[i][j]*j;
            cursumW+=vals[i][j];

            sumX[i+1][j+1]=sumX[i][j+1]+cursumX;
            sumY[i+1][j+1]=sumY[i][j+1]+cursumY;
            sumW[i+1][j+1]=sumW[i][j+1]+cursumW;
        }
    }

    int bk=-1;
    int sx,sy,sw,cx,cy,kx,ky;;
    for(i=0;i<N;i++)
        for(j=0;j<M;j++)
            for(k=3;i+k-1<N&&j+k-1<M;k++)
            {
                sx=sumX[i][j]+sumX[i+k][j+k]-sumX[i][j+k]-sumX[i+k][j];
                sy=sumY[i][j]+sumY[i+k][j+k]-sumY[i][j+k]-sumY[i+k][j];
                sw=sumW[i][j]+sumW[i+k][j+k]-sumW[i][j+k]-sumW[i+k][j];

                kx=i+k-1; ky=j+k-1;
                sw-=vals[i][j]+vals[kx][ky]+vals[kx][j]+vals[i][ky];
                sx-=vals[i][j]*i+vals[kx][ky]*kx+vals[kx][j]*kx+vals[i][ky]*i;
                sy-=vals[i][j]*j+vals[kx][ky]*ky+vals[kx][j]*j+vals[i][ky]*ky;

                cx=2*i+k-1;
                cy=2*j+k-1;
                cx*=sw;
                cy*=sw;
                if(cx==2*sx&&cy==2*sy)
                {//cout<<i<<" "<<j<<" "<<k<<endl;
                    if(k>bk) bk=k;
                }
            }
    if(bk==-1)  cout<<"IMPOSSIBLE";
    else cout<<bk;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int i,T;
    cin>>T;
    for(i=0;i<T;i++)
    {
      cout<<"Case #"<<i+1<<": ";
      test();
      cout<<endl;
    }
    return 0;
}
