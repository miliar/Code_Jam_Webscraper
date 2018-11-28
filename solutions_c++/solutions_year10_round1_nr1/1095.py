#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>
#include<string.h>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
    int red=0,blue=0;
    int n,qaz;
    cin>>n>>qaz;
    char b[(n+2)*2][(n+2)*2];
    for(int j=0;j<n+2;j++)
    {
        int x=1;
        for(int k=0;k<=n+1;k++)
        {
            b[j][k]='.';
        }
    }
    for(int j=0;j<n;j++)
    {
        int x=0;
        for(int k=0;k<n;k++)
        {
            char q;
            cin>>q;
            if(q!='.')
            {
                b[j+1][2*(n+2)-x-1]=q;
                x++;   
            }
        }
        for(int k=0;k<x;k++)
        {
            b[j+1][k+1]=b[j+1][2*(n+2)-x+k];
        }
    }
    int q[n+2][n+2][4];
    for(int j=0;j<=n+1;j++)
    {
        for(int k=0;k<=n+1;k++)
        {
            q[j][k][0]=q[j][k][1]=q[j][k][2]=q[j][k][3]=0;
        }
    }
    for(int j=1;j<=n;j++)
    {
        int x=1;
        while(b[j][x]!='.')
        {
            if(b[j][x-1]==b[j][x])
            {
                q[j][x][0]=q[j][x-1][0]+1;
                if(q[j][x][0]==qaz)
                {
                    if(b[j][x]=='R')
                    {
                        red=1;
                    }
                    else
                    {
                        blue=1;
                    }
                }
                
            }
            else
                {
                    q[j][x][0]=1;
                }
            if(b[j-1][x]==b[j][x])
            {
                q[j][x][1]=q[j-1][x][1]+1;
                if(q[j][x][1]==qaz)
                {
                    if(b[j][x]=='R')
                    {
                        red=1;
                    }
                    else
                    {
                        blue=1;
                    }
                }
                
            }
            else
                {
                    q[j][x][1]=1;
                }
            if(b[j-1][x-1]==b[j][x])
            {
                q[j][x][2]=q[j-1][x-1][2]+1;
                if(q[j][x][2]==qaz)
                {
                    if(b[j][x]=='R')
                    {
                        red=1;
                    }
                    else
                    {
                        blue=1;
                    }
                }
            }
            else
            {
                q[j][x][2]=1;
            }
            if(b[j-1][x+1]==b[j][x])
            {
                q[j][x][3]=q[j-1][x+1][3]+1;
                if(q[j][x][3]==qaz)
                {
                    if(b[j][x]=='R')
                    {
                        red=1;
                    }
                    else
                    {
                        blue=1;
                    }
                }
                
            }
            else
                {
                    q[j][x][3]=1;
                }
            x++;
        }
    }
    string an;    
    if(red==1 && blue==1)
    {
        an="Both";
    }    
    else if(red==1)
    {
        an="Red";
    }
    else if(blue==1)
    {
        an="Blue";
    }
    else
    {
        an="Neither";
    }
   /* for(int j=0;j<n+2;j++)
    {for(int k=0;k<=n+1;k++)
    cout<<b[j][k]<<" ";
    cout<<endl;}
    cout<<"\n----------------------\n";
    for(int j=0;j<n+2;j++)
    {for(int k=0;k<=n+1;k++)
    cout<<q[j][k][1]<<" ";
    cout<<endl;}
    cout<<"\n----------------------\n";*/
    cout<<"Case #"<<i<<": "<<an<<endl;
}
  //system("pause");
  return 0;
}
