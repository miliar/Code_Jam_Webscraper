#include<iostream>
using namespace std;

char s[1005][1005];
int m[105][105];
int main()
{
int t;
cin>>t;

for(int i=1;i<=t;i++)
{
    int x,y;
    cin>>x>>y;
    int g=0;
    memset(m,0,sizeof(m));
    for(int i=1;i<=x;i++)
    {
    for(int j=1;j<=y;j++){
        cin>>s[i][j];
        if(s[i][j]=='#')
     {
      m[i][j]=1;  g++;
    }
        }}
    if(g%4!=0&&g>0)
    {
        cout<<"Case #"<<i<<":"<<endl;
        cout<<"Impossible"<<endl;
        continue;
    }
    else if(g==0)
    {
        cout<<"Case #"<<i<<":"<<endl;
         for(int i=1;i<=x;i++)
    {
        for(int j=1;j<=y;j++)
    {cout<<s[i][j];}cout<<endl;
    }
        continue;
    }
    bool f=0;
    for(int i=1;i<=x;i++)
    {
        for(int j=1;j<=y;j++)
        {
            if(m[i][j]==1)
            {
                m[i][j]=2;
                if(m[i+1][j]==1&&m[i][j+1]==1&&m[i+1][j+1]==1)
                {
                m[i+1][j]=2;
                m[i][j+1]=2;
                m[i+1][j+1]=2;
                s[i][j]='/';
                s[i][j+1]='\\';
                s[i+1][j+1]='/';
                s[i+1][j]='\\';
                }
                else{
                f=1;
                break;
                }
            }

        }
        if(f==1)break;
    }
     cout<<"Case #"<<i<<":"<<endl;
     if(f==1)
     {
         cout<<"Impossible"<<endl;
     }
     else{
         for(int i=1;i<=x;i++)
    {
        for(int j=1;j<=y;j++)
    {cout<<s[i][j];}cout<<endl;
    }}
}
return 0;
}
