#include<cstdio>
#include<cstring>
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int tt;
    cin>>tt;
    for(int t=1;t<=tt;t++)
    {
        int r,c;
        cin>>r>>c;
        char reg[60][60];
        int ok[60][60];
        memset(ok,1,sizeof(ok));
        for(int i=1;i<=r;i++)
        {
            string s;
            cin>>s;
            for(int j=1;j<=c;j++)
            {
                if(s[j-1]=='.')
                ok[i][j]=1,reg[i][j]='.';
                else
                ok[i][j]=0,reg[i][j]=s[j-1];
            }
        }
        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                if(ok[i][j]==1) continue;
                if(ok[i][j]==0&&ok[i][j+1]==0&&ok[i+1][j]==0&&ok[i+1][j+1]==0)
                {
                    reg[i][j]='/';
                    reg[i][j+1]='\\';
                    reg[i+1][j]='\\';
                    reg[i+1][j+1]='/';
                    ok[i][j]=1;
                    ok[i][j+1]=1;
                    ok[i+1][j]=1;
                    ok[i+1][j+1]=1;
                }

            }
        }
        bool flag=1;
        for(int i=1;i<=r;i++)
            for(int j=1;j<=c;j++)
                flag&=ok[i][j];
            cout<<"Case #"<<t<<":\n";
        if(flag==1)
        {
            for(int i=1;i<=r;i++)
            {
                for(int j=1;j<=c;j++)
                {
                    cout<<reg[i][j];
                }
                cout<<"\n";
            }
        }
        else
        cout<<"Impossible\n";
    }
    return 0;
}
