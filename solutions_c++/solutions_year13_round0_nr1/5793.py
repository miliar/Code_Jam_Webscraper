#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int T;
char a[5][5];
int gx[4]={1,0,1,1};
int gy[4]={0,1,1,-1};
int ok1(int x,int y)
{
    return (x>=0&&x<4&&y>=0&&y<4);
}
int ok(int x,int y,char f)
{
    for(int i=0;i<4;i++)
    {
        int cnt=0,r=x,c=y;
        for(int j=0;j<3;j++)
        {
            int xx=r+gx[i],yy=c+gy[i];
            if(ok1(xx,yy)&&(a[xx][yy]==f||a[xx][yy]=='T')) cnt++;
            r=xx;c=yy;
        }
        if(cnt==3) return 1;
    }
    return 0;
}
int main()
{
    freopen("test.txt","r",stdin);
    freopen("test_out.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int ans=-1,flag=-1;
        for(int i=0;i<4;i++)
            cin>>a[i];

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a[i][j]=='.') flag=0;
                else if(a[i][j]=='O'&&ok(i,j,'O'))
                {
                    ans=0;break;
                }
                else if(a[i][j]=='X'&&ok(i,j,'X'))
                {
                    ans=1;break;
                }
                else if(a[i][j]=='T')
                {
                    if(ok(i,j,'O')) ans=0;
                    if(ok(i,j,'T')) ans=1;
                    if(ans!=-1) break;
                }
            }
            if(ans!=-1) break;
        }
        printf("Case #%d: ",t);
        if(ans==0) cout<<"O won"<<endl;
        else if(ans==1) cout<<"X won"<<endl;
        else if(flag==-1) cout<<"Draw"<<endl;
        else cout<<"Game has not completed"<<endl;
    }
    return 0;
}
