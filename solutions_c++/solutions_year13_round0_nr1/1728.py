#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int n;
    char a[4][4];
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.txt","w",stdout);
    //while(cin>>n)
    //{
    cin>>n;
        for(int c=1;c<=n;c++)
        {
            int x,o,sum=0;
            bool flag=false;
            for(int i=0;i<4;i++)
            {
                if(!flag)
                {
                    x=0;
                    o=0;
                }
                for(int j=0;j<4;j++)
                {
                    cin>>a[i][j];
                    if(!flag)
                    {
                        if(a[i][j]=='X'||a[i][j]=='T')
                        {
                            x++;
                        }
                        if(a[i][j]=='O'||a[i][j]=='T')
                        {
                            o++;
                        }
                        if(a[i][j]=='.')
                        {
                            sum++;
                        }
                    }
                }
                if(x==4||o==4)
                {
                    flag=true;
                }
            }
            if(x==4)
            {
                cout<<"Case #"<<c<<": "<<"X won"<<endl;
                continue;
            }
            else if(o==4)
            {
                cout<<"Case #"<<c<<": "<<"O won"<<endl;
                continue;
            }
            for(int j=0;j<4;j++)
            {
                x=0;
                o=0;
                for(int i=0;i<4;i++)
                {
                    if(a[i][j]=='X'||a[i][j]=='T')
                    {
                        x++;
                    }
                    if(a[i][j]=='O'||a[i][j]=='T')
                    {
                        o++;
                    }
                }
                if(x==4||o==4)
                {
                    break;
                }
            }
            if(x==4)
            {
                cout<<"Case #"<<c<<": "<<"X won"<<endl;
                continue;
            }
            else if(o==4)
            {
                cout<<"Case #"<<c<<": "<<"O won"<<endl;
                continue;
            }
            x=0;
            o=0;
            for(int i=0;i<4;i++)
            {
                if(a[i][i]=='X'||a[i][i]=='T')
                {
                    x++;
                }
                if(a[i][i]=='O'||a[i][i]=='T')
                {
                    o++;
                }
            }
            if(x==4)
            {
                cout<<"Case #"<<c<<": "<<"X won"<<endl;
                continue;
            }
            else if(o==4)
            {
                cout<<"Case #"<<c<<": "<<"O won"<<endl;
                continue;
            }
            x=0;
            o=0;
            for(int i=0;i<4;i++)
            {
                if(a[i][3-i]=='X'||a[i][3-i]=='T')
                {
                    x++;
                }
                if(a[i][3-i]=='O'||a[i][3-i]=='T')
                {
                    o++;
                }
            }
            if(x==4)
            {
                cout<<"Case #"<<c<<": "<<"X won"<<endl;
                continue;
            }
            else if(o==4)
            {
                cout<<"Case #"<<c<<": "<<"O won"<<endl;
                continue;
            }
            if(sum==0)
            {
                cout<<"Case #"<<c<<": "<<"Draw"<<endl;
                continue;
            }
            cout<<"Case #"<<c<<": "<<"Game has not completed"<<endl;
        }
    //}
    return 0;
}
