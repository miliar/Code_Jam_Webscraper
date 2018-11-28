#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include <fstream>
using namespace std;
const int mod = 1e9+7;
#define LL long long
#define mem(a,b) memset(a,b,sizeof(a))
char s[5][5];
int main()
{
    int i,j,t;
    freopen("A-small-attempt4.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
        int sum=0;
        for(i=0;i<4;i++)
        {
           scanf("%s",s[i]);
           for(j=0;j<4;j++)
             if(s[i][j]=='.')sum=1;
        }
        int flag1=0,flag2=0;
        for(i=0;i<4;i++)
        {
            if(s[i][0]=='X'&&s[i][1]=='X'&&s[i][2]=='X'&&s[i][3]=='X')flag1=1;
            if(s[i][0]=='T'&&s[i][1]=='X'&&s[i][2]=='X'&&s[i][3]=='X')flag1=1;
            if(s[i][0]=='X'&&s[i][1]=='T'&&s[i][2]=='X'&&s[i][3]=='X')flag1=1;
            if(s[i][0]=='X'&&s[i][1]=='X'&&s[i][2]=='T'&&s[i][3]=='X')flag1=1;
            if(s[i][0]=='X'&&s[i][1]=='X'&&s[i][2]=='X'&&s[i][3]=='T')flag1=1;

            if(s[i][0]=='O'&&s[i][1]=='O'&&s[i][2]=='O'&&s[i][3]=='O')flag2=1;
            if(s[i][0]=='T'&&s[i][1]=='O'&&s[i][2]=='O'&&s[i][3]=='O')flag2=1;
            if(s[i][0]=='O'&&s[i][1]=='T'&&s[i][2]=='O'&&s[i][3]=='O')flag2=1;
            if(s[i][0]=='O'&&s[i][1]=='O'&&s[i][2]=='T'&&s[i][3]=='O')flag2=1;
            if(s[i][0]=='O'&&s[i][1]=='O'&&s[i][2]=='O'&&s[i][3]=='T')flag2=1;

            if(s[0][i]=='X'&&s[1][i]=='X'&&s[2][i]=='X'&&s[3][i]=='X')flag1=1;
            if(s[0][i]=='T'&&s[1][i]=='X'&&s[2][i]=='X'&&s[3][i]=='X')flag1=1;
            if(s[0][i]=='X'&&s[1][i]=='T'&&s[2][i]=='X'&&s[3][i]=='X')flag1=1;
            if(s[0][i]=='X'&&s[1][i]=='X'&&s[2][i]=='T'&&s[3][i]=='X')flag1=1;
            if(s[0][i]=='X'&&s[1][i]=='X'&&s[2][i]=='X'&&s[3][i]=='T')flag1=1;

            if(s[0][i]=='O'&&s[1][i]=='O'&&s[2][i]=='O'&&s[3][i]=='O')flag2=1;
            if(s[0][i]=='T'&&s[1][i]=='O'&&s[2][i]=='O'&&s[3][i]=='O')flag2=1;
            if(s[0][i]=='O'&&s[1][i]=='T'&&s[2][i]=='O'&&s[3][i]=='O')flag2=1;
            if(s[0][i]=='O'&&s[1][i]=='O'&&s[2][i]=='T'&&s[3][i]=='O')flag2=1;
            if(s[0][i]=='O'&&s[1][i]=='O'&&s[2][i]=='O'&&s[3][i]=='T')flag2=1;
        }
        if(s[0][0]=='X'&&s[1][1]=='X'&&s[2][2]=='X'&&s[3][3]=='X')flag1=1;
        if(s[0][0]=='T'&&s[1][1]=='X'&&s[2][2]=='X'&&s[3][3]=='X')flag1=1;
        if(s[0][0]=='X'&&s[1][1]=='T'&&s[2][2]=='X'&&s[3][3]=='X')flag1=1;
        if(s[0][0]=='X'&&s[1][1]=='X'&&s[2][2]=='T'&&s[3][3]=='X')flag1=1;
        if(s[0][0]=='X'&&s[1][1]=='X'&&s[2][2]=='X'&&s[3][3]=='T')flag1=1;

        if(s[0][0]=='O'&&s[1][1]=='O'&&s[2][2]=='O'&&s[3][3]=='O')flag1=1;
        if(s[0][0]=='T'&&s[1][1]=='O'&&s[2][2]=='O'&&s[3][3]=='O')flag1=1;
        if(s[0][0]=='O'&&s[1][1]=='T'&&s[2][2]=='O'&&s[3][3]=='O')flag1=1;
        if(s[0][0]=='O'&&s[1][1]=='O'&&s[2][2]=='T'&&s[3][3]=='O')flag1=1;
        if(s[0][0]=='O'&&s[1][1]=='O'&&s[2][2]=='O'&&s[3][3]=='T')flag1=1;

        if(s[0][3]=='O'&&s[1][2]=='O'&&s[2][1]=='O'&&s[3][0]=='O')flag2=1;
        if(s[0][3]=='T'&&s[1][2]=='O'&&s[2][1]=='O'&&s[3][0]=='O')flag2=1;
        if(s[0][3]=='O'&&s[1][2]=='T'&&s[2][1]=='O'&&s[3][0]=='O')flag2=1;
        if(s[0][3]=='O'&&s[1][2]=='O'&&s[2][1]=='T'&&s[3][0]=='O')flag2=1;
        if(s[0][3]=='O'&&s[1][2]=='O'&&s[2][1]=='O'&&s[3][0]=='T')flag2=1;

        if(s[0][3]=='X'&&s[1][2]=='X'&&s[2][1]=='X'&&s[3][0]=='X')flag2=1;
        if(s[0][3]=='T'&&s[1][2]=='X'&&s[2][1]=='X'&&s[3][0]=='X')flag2=1;
        if(s[0][3]=='X'&&s[1][2]=='T'&&s[2][1]=='X'&&s[3][0]=='X')flag2=1;
        if(s[0][3]=='X'&&s[1][2]=='X'&&s[2][1]=='T'&&s[3][0]=='X')flag2=1;
        if(s[0][3]=='X'&&s[1][2]=='X'&&s[2][1]=='X'&&s[3][0]=='T')flag2=1;
        printf("Case #%d: ",++cas);
        //cout<<flag1<<" "<<flag2<<endl;
        if((flag2&&flag1)||(flag2==0&&flag1==0&&sum==0))puts("Draw");
        else if(flag1)puts("X won");
        else if(flag2)puts("O won");
        else puts("Game has not completed");
    }

}
