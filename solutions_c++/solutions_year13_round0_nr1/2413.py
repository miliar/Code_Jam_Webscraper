#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
bool equal(char c1,char c2)
{
    if(c1==c2) return true;
    else if(c1=='.' || c2=='.') return false;
    else if(c1=='T' || c2=='T') return true;
    return false;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ci=1;ci<=cas;ci++)
    {
        char data[5][5];
        gets(data[0]);
        for(int i=0;i<4;i++)
        {
            gets(data[i]);
        }
        //for(int i=0;i<4;i++) cout << data[i] << endl;
        bool draw=true;
        int ans=0;
        for(int i=0;i<4;i++)
        {
            bool e=true;
            char c=data[i][0];
            if(c=='T') c=data[i][1];
            for(int j=0;j<4;j++)
            {
                if(data[i][j]=='.') draw=false;
                e=e&&equal(c,data[i][j]);
            }
            if(data[i][0]!='.' && e)
            {
                //cout << i << ' ' << c<<  endl;
                if(c=='X') ans=1;
                else ans=2;
                break;
            }
            e=true;
            c=data[0][i];
            if(c=='T') c=data[1][i];
            for(int j=0;j<4;j++)
            {
                e=e&&equal(c,data[j][i]);
            }
            if(data[0][i]!='.' && e)
            {
                //cout << i << ' ' << c<<  endl;
                if(c=='X') ans=1;
                else ans=2;
                break;
            }
        }
        //cout << ans << ' ' << draw << endl;
        if(ans==0 && !draw)
        {
            bool e=true;
            char c=data[0][0];
            if(c=='T') c=data[1][1];
            for(int i=0;i<4;i++)
            {
                e=e&&equal(data[i][i],c);
            }
            if(data[0][0]!='.' && e)
            {
                if(c=='X') ans=1;
                else ans=2;
            }
        }

        if(ans==0 && !draw)
        {
            bool e=true;
            char c=data[0][3];
            if(c=='T') c=data[1][2];
            for(int i=0;i<4;i++)
            {
                e=e&&equal(data[i][3-i],c);
            }
            if(data[0][3]!='.' && e)
            {
                if(c=='X') ans=1;
                else ans=2;
            }
        }
        printf("Case #%d: ",ci);
        if(ans==0 && draw)
        {
            printf("Draw\n");
        }
        else if(ans==0 && !draw)
        {
            printf("Game has not completed\n");
        }
        else if(ans==1)
        {
            printf("X won\n");
        }
        else
        {
            printf("O won\n");
        }
    }
}
