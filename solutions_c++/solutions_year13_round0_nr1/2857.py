#include<iostream>
#include<cstdio>
using namespace std;
char mp[10][10];
bool check(char a,char b)
{
    if(a==b || a=='T') return true;
    return false;
}
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        printf("Case #%d: ",cas++);
        for(int i=0;i<4;i++)scanf("%s",mp[i]);
        int ans = 0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(mp[i][j]=='.') ans = 4;
        for(int i=0;i<4;i++)
        {
            if(check(mp[i][0],'X') && check(mp[i][1],'X')&& check(mp[i][2],'X')&& check(mp[i][3],'X') )
            {
                ans = 1;
                break;
            }
            if(check(mp[i][0],'O') && check(mp[i][1],'O')&& check(mp[i][2],'O')&& check(mp[i][3],'O') )
            {
                ans = 2;
                break;
            }
            if(check(mp[0][i],'X') && check(mp[1][i],'X')&& check(mp[2][i],'X')&& check(mp[3][i],'X') )
            {
                ans = 1;
                break;
            }
            if(check(mp[0][i],'O') && check(mp[1][i],'O')&& check(mp[2][i],'O')&& check(mp[3][i],'O') )
            {
                ans = 2;
                break;
            }
        }
        if(check(mp[0][0],'X') && check(mp[1][1],'X')&& check(mp[2][2],'X')&& check(mp[3][3],'X') )
            ans = 1;
        if(check(mp[0][0],'O') && check(mp[1][1],'O')&& check(mp[2][2],'O')&& check(mp[3][3],'O') )
            ans = 2;
        if(check(mp[0][3],'X') && check(mp[1][2],'X')&& check(mp[2][1],'X')&& check(mp[3][0],'X') )
            ans = 1;
        if(check(mp[0][3],'O') && check(mp[1][2],'O')&& check(mp[2][1],'O')&& check(mp[3][0],'O') )
            ans = 2;
        if(ans==0) puts("Draw");
        else if(ans==1) puts("X won");
        else if(ans==2) puts("O won");
        else puts("Game has not completed");
    }
    return 0;
}
