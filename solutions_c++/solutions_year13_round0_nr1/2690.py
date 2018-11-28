#include<iostream>
#include<stdio.h>
using namespace std;
char map[4][4];
int search()
{
    bool win=1;
    int l;
    for(int i=0; i<4; i++)
    {
        l=(map[i][0]=='T'?1:0);
        //cout<<l;
        win=1;
        for(int j=1; j<4; j++)
            if(map[i][j]=='.')
            {
                win=0;
                break;
            }
            else if(map[i][j]!=map[i][l]&&map[i][j]!='T')
                win=0;
        if(win)
            return (map[i][l]=='X'?1:-1);
    }
    for(int j=0; j<4; j++)
    {
        win=1;
        l=(map[0][j]=='T'?1:0);
        for(int i=1; i<4; i++)
            if(map[i][j]=='.')
            {
                win=0;
                break;
            }
            else if(map[i][j]!=map[l][j]&&map[i][j]!='T')win=0;
        if(win)
            return (map[l][j]=='X'?1:-1);
    }
    l=(map[0][0]=='T'?1:0);
    win=1;
    for(int i=0; i<4; i++)
    {
        if(map[i][i]=='.')
        {
            win=0;
            break;
        }
        else if(map[i][i]!=map[l][l]&&map[i][i]!='T')win=0;
    }
    if(win)
        return (map[l][l]=='X'?1:-1);
    l=(map[0][3]=='T'?1:0);
    win=1;
    for(int i=0; i<4; i++)
    {
        if(map[i][3-i]=='.')
        {
            win=0;
            break;
        }
        else if(map[i][3-i]!=map[l][3-l]&&map[i][3-i]!='T')win=0;
       // cout<<win<<endl;
    }
    if(win)
        return (map[l][3-l]=='X'?1:-1);
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.txt","w",stdout);
    int t;
    cin>>t;
    for(int cnt=1; cnt<=t; cnt++)
    {
        int isfull=1;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                cin>>map[i][j];
                if(map[i][j]=='.')isfull=0;
            }
        // for(int i=0; i<4; i++)            for(int j=0; j<4; j++)cout<<map[i][j];
        cout<<"Case #"<<cnt<<": ";
        int ans=search();
        if(ans==1)
            cout<<"X won"<<endl;
        else if(ans==0&&isfull==1)
            cout<<"Draw"<<endl;
        else if(ans==0&&isfull==0)
            cout<<"Game has not completed"<<endl;
        else
            cout<<"O won"<<endl;

    }
}
