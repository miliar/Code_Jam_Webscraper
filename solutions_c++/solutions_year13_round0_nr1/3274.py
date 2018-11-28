#include <iostream>
#include <cstdio>
using namespace std;

int T;
char p[10][10];

bool find(char c)
{
    for (int i=0;i<4;i++)
    {
        int cnt=0;
        for (int j=0;j<4;j++)
        {
            if (p[i][j]==c || p[i][j]=='T') cnt++;
        }
        if (cnt==4) return true;
    }

    for (int j=0;j<4;j++)
    {
        int cnt=0;
        for (int i=0;i<4;i++)
        {
            if (p[i][j]==c || p[i][j]=='T') cnt++;
        }
        if (cnt==4) return true;
    }

    int cnt=0;
    for (int i=0;i<4;i++)
    {
        if (p[i][i]==c || p[i][i]=='T') cnt++;
    }
    if (cnt==4) return true;

    cnt=0;
    for (int i=0;i<4;i++)
    {
        if (p[3-i][i]==c || p[3-i][i]=='T') cnt++;
    }
    if (cnt==4) return true;
    return false;

}

int main()
{
    freopen("A-large.in", "r", stdin );
    freopen("A-large.out", "w", stdout );
    cin>>T;
    int cs=0;
    while (T--)
    {
        cs++;
        for (int i=0;i<4;i++)
            scanf("%s",p[i]);
        int awin=find('O');
        int bwin=find('X');
        printf("Case #%d: ", cs);
        if (awin && bwin)
        {
            cout<<"Draw"<<endl;
        }
        else if (!awin && !bwin)
        {
            int sy=false;
            for (int i=0;i<4;i++)
                for (int j=0;j<4;j++)
                {
                    if (p[i][j]=='.') {sy=true; break; }
                }
            if (sy) cout<<"Game has not completed"<<endl;
            else cout<<"Draw"<<endl;
        }
        else if (awin)
        {
            cout<<"O won"<<endl;
        }
        else
        {
            cout<<"X won"<<endl;
        }
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
