#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <cstdio>
using namespace std;
char map[55][55];
int r,c;
int main()
{
    int t;
    freopen("A-large (2).in","r",stdin);
    freopen("out2.txt","w",stdout);
    cin>>t;
    int cas=1;
    while(t--)
    {
        cout<<"Case #"<<cas++<<":"<<endl;
        int cnt = 0;
        cin>>r>>c;
        for(int i =0;i<r;i++)
        for(int j =0;j<c;j++)
        {
            cin>>map[i][j];
            if(map[i][j]=='#')cnt++;
        }
        if(cnt%4!=0)
        {
            cout<<"Impossible"<<endl;
            continue;
        }
        bool flag = true;
        int round = cnt/4;
        while(round--)
        {
            bool find = false;
            for(int i =0;i<r-1;i++)
            {
                for(int j =0;j<c-1;j++)
                {
                    if(map[i][j]=='#')
                    {

                        find = true;
                        if(map[i+1][j]=='#'&&map[i][j+1]=='#'&&map[i+1][j+1]=='#')
                        {
                            map[i][j]=map[i+1][j+1]='/';
                            map[i+1][j]=map[i][j+1]='\\';
                            break;
                        }
                        else
                        {

                            flag = false;
                            break;
                        }
                    }
                }
                if(find)
                    break;
            }
            if(!flag)
                 break;
        }
        if(!flag)
        {
            cout<<"Impossible"<<endl;
        }
        else
        {
            for(int i =0;i<r;i++)
            {
                for(int j =0;j<c;j++)
                {
                    cout<<map[i][j];
                }
                cout<<endl;
            }
        }
    }
    return 0;
}
