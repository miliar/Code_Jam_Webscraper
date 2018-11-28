#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>

using namespace std;

struct sink
{
    int i,j;
    char name;
};

vector<sink> sinks;
char name='a';

char find_sink_name(int i,int j)
{
    for(int n=0;n<sinks.size();n++)
    {
        if(sinks[n].i==i&&sinks[n].j==j)
            return sinks[n].name;
    }

    sink temp;
    temp.i=i;
    temp.j=j;
    temp.name=name;
    name++;

    sinks.push_back(temp);
    return temp.name;

}

sink calc(int i, int j, int ip[110][110])
{
    sink d;

    if(ip[i-1][j]<ip[i][j] && ip[i-1][j]<=ip[i][j-1] && ip[i-1][j]<=ip[i][j+1] && ip[i-1][j]<=ip[i+1][j] )
    {
        d.i=-1;
        d.j=0;
    }


    else if( ip[i][j-1]<ip[i][j] && ip[i][j-1]<=ip[i][j+1] && ip[i][j-1]<=ip[i+1][j] )
    {
        d.i=0;
        d.j=-1;
    }

    else if(ip[i][j+1]<ip[i][j] && ip[i][j+1]<=ip[i+1][j])
    {
        d.i=0;
        d.j=1;
    }

    else if(ip[i+1][j]<ip[i][j])
    {
        d.i=1;
        d.j=0;
    }
    else
    {
        d.i=0;
        d.j=0;
    }

    return d;
}



int main()
{

int n,ca=1;

cin>>n;

while(n-->0)
{
    sinks.clear();
    name='a';
    int m,n;
    int ip[110][110];
    char ans[110][110];
    sink dir[110][110];
    cin>>m>>n;

    for(int i=0;i<m+2;i++)
        for(int j=0;j<n+2;j++)
            ip[i][j]=10001;


    for(int i=1;i<=m;i++)
        for(int j=1;j<=n;j++)
            cin>>ip[i][j];

    for(int i=1;i<=m;i++)
        for(int j=1;j<=n;j++)
            dir[i-1][j-1]=calc(i,j,ip);


    for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
        {
            int x=i,y=j;

            while(!(dir[x][y].i==0 && dir[x][y].j==0))
            {
                x+=dir[x][y].i;
                y+=dir[x][y].j;

            }

            ans[i][j]=find_sink_name(x,y);

        }


    cout<<"Case #"<<ca++<<":\n";
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
            cout<<ans[i][j]<<' ';

        cout<<'\n';
    }

}


}

