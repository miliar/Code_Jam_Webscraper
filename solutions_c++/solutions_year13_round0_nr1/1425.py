#include <iostream>
#include <cstdio>

using namespace std;

char ch[5][5];

bool judge(char cha)
{
    int i,j;
    for(i=1;i<=4;i++)
    {
        if(ch[i][1]!=cha&&ch[i][1]!='T') continue;
        if(ch[i][2]!=cha&&ch[i][2]!='T') continue;
        if(ch[i][3]!=cha&&ch[i][3]!='T') continue;
        if(ch[i][4]!=cha&&ch[i][4]!='T') continue;
        return true;
    }
    for(j=1;j<=4;j++)
    {
        if(ch[1][j]!=cha&&ch[1][j]!='T') continue;
        if(ch[2][j]!=cha&&ch[2][j]!='T') continue;
        if(ch[3][j]!=cha&&ch[3][j]!='T') continue;
        if(ch[4][j]!=cha&&ch[4][j]!='T') continue;
        return true;
    }
    if((ch[1][1]==cha||ch[1][1]=='T')&&(ch[2][2]==cha||ch[2][2]=='T')&&(ch[3][3]==cha||ch[3][3]=='T')&&(ch[4][4]==cha||ch[4][4]=='T')) return true;
    if((ch[1][4]==cha||ch[1][4]=='T')&&(ch[2][3]==cha||ch[2][3]=='T')&&(ch[3][2]==cha||ch[3][2]=='T')&&(ch[4][1]==cha||ch[4][1]=='T')) return true;
    return false;
}
int main()
{
    int T,cas=0;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    while(T--)
    {
        cas++;
        bool X=false,O=false,flag=true;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>ch[i][j];
                if(ch[i][j]=='.') flag=false;
                //cout<<ch[i][j];
            }
            //cout<<endl;
        }
        if(judge('X')) X=true;
        if(judge('O')) O=true;
        if(X&&!O) cout<<"Case #"<<cas<<": X won"<<endl;
        if(!X&&O) cout<<"Case #"<<cas<<": O won"<<endl;
        if(!X&&!O&&flag) cout<<"Case #"<<cas<<": Draw"<<endl;
        if(!flag&&!X&&!O) cout<<"Case #"<<cas<<": Game has not completed"<<endl;

    }
    return 0;
}
