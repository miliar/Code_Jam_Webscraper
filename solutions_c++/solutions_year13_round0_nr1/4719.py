#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <deque>
#include <cmath>
#define mod 1000000007LL
using namespace std;

char a[10][10];


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int d[8][2]={-1,-1,-1,0,-1,1,0,-1,0,1,1,-1,1,0,1,1};
    int i,j,k,p,x,y;
    int re,cases=1;
    cin>>re;
    while(re--)
    {
        for(i=0;i<4;i++)
            scanf("%s",a[i]);
        char ans='.';
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[i][j]=='X'||a[i][j]=='O')
                {
                for(k=0;k<8;k++)
                {
                    for(p=0;p<4;p++)
                    {
                        x=i+d[k][0]*p;
                        y=j+d[k][1]*p;
                        if(x<0||x==4||y<0||y==4)
                            break;
                        if(a[x][y]==a[i][j]||a[x][y]=='T')
                            continue;
                        break;
                    }
                    if(p==4)//win
                        ans=a[i][j];
                }
                }
            }
        }
        
        cout<<"Case #"<<cases++<<": ";
        if(ans!='.')
        {
            cout<<ans<<" won"<<endl;
        }
        else
        {
            for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            if(a[i][j]=='.')
                ans='!';
            if(ans=='!')
                cout<<"Game has not completed"<<endl;
            else cout<<"Draw"<<endl;
        }
        
    }
    return 0;
}
