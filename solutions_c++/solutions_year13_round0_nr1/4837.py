/* 	Language C++
	Copyright Liang Yongqing all
*/

#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>

using namespace std;
#define fi first
#define se second
#define ll long long
#define INF 2000000000
#define eps 1e-12
#define maxn 4

const int route[4][2]={{0,1},{1,0},{1,1},{-1,1}};
char a[4][4];

int main()
{
	freopen("temp.in","r",stdin);
	freopen("temp.out","w",stdout);

    int Test,test;
    int i,j,k,l,flag,x,y,pd;

    cin>>Test; test=0;
    while (Test--)
    {
        printf("Case #%d: ",++test);

        for (i=0;i<4;i++) cin>>a[i];
        flag=0;
        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                if (a[i][j]=='.') flag=1;
            }
            if (flag) break;
        }
        for (i=0;i<4;i++)
        {
            for (j=0;j<4;j++)
            {
                if (a[i][j]=='.') continue;

                for (k=0;k<4;k++)
                {
                    if (a[i][j]=='T') pd=0;
                    if (a[i][j]=='O') pd=2;
                    if (a[i][j]=='X') pd=3;
                    for (l=1;l<4;l++)
                    {
                        x=i+route[k][0]*l; y=j+route[k][1]*l;
                        if (!(x>=0 && x<=3 && y>=0 && y<=3)) break;
                        if (a[x][y]=='T') continue;
                        if (a[x][y]=='.') break;
                        if (pd==0)
                        {
                            if (a[x][y]=='O') pd=2;
                            if (a[x][y]=='X') pd=3;
                        }else
                        {
                            if (pd==2 && a[x][y]=='O') continue;
                            if (pd==3 && a[x][y]=='X') continue;
                            break;
                        }
                    }
                    if (l==4 && pd>=2)
                    {
                        flag=pd;
                        break;
                    }
                }
                if (flag>1) break;
            }
            if (flag>1) break;
        }
        if (flag==0) printf("Draw");
        if (flag==1) printf("Game has not completed");
        if (flag==2) printf("O won");
        if (flag==3) printf("X won");
        printf("\n");
    }
	return 0;
}
