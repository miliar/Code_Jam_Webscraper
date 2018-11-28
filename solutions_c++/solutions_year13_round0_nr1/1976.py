#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

char cm[5][5];

void solve()
{
    int OO1,XX1,TT1,OO2,XX2,TT2,DD=0;
    for(int i=0;i<4;i++)
    {
        OO1=0;XX1=0;TT1=0;
        OO2=0;XX2=0;TT2=0;
        for(int j=0;j<4;j++)
        {
            if('O'==cm[i][j])OO1++;
            else if('X'==cm[i][j])XX1++;
            else if('T'==cm[i][j])TT1++;
            if('O'==cm[j][i])OO2++;
            else if('X'==cm[j][i])XX2++;
            else if('T'==cm[j][i])TT2++;
            if('.'==cm[i][j])DD++;
        }
        if(4==OO1+TT1 || 4==OO2+TT2)
        {
            printf("O won\n");
            return;
        }
        else if(4==XX1+TT1 || 4==XX2+TT2)
        {
            printf("X won\n");
            return;
        }
    }
    OO1=0;XX1=0;TT1=0;
    OO2=0;XX2=0;TT2=0;
    for(int i=0;i<4;i++)
    {
        if('O'==cm[i][i])OO1++;
        else if('X'==cm[i][i])XX1++;
        else if('T'==cm[i][i])TT1++;
        if('O'==cm[3-i][i])OO2++;
        else if('X'==cm[3-i][i])XX2++;
        else if('T'==cm[3-i][i])TT2++;
    }
    if(4==OO1+TT1 || 4==OO2+TT2)
    {
        printf("O won\n");
        return;
    }
    else if(4==XX1+TT1 || 4==XX2+TT2)
    {
        printf("X won\n");
        return;
    }
    if(0==DD)
    {
        printf("Draw\n");
    }
    else 
    {
        printf("Game has not completed\n");
    }
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A.out.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>cm[0]>>cm[1]>>cm[2]>>cm[3];
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
