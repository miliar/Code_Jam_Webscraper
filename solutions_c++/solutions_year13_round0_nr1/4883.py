#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char map[10][10];


int solve()
{
    int num1,num2;
    for(int i=1;i<=4;i++)
    {
        num1=num2=0;
        for(int j=1;j<=4;j++)
        {
            if(map[i][j]=='X')  num1++;
            else if(map[i][j]=='O')  num2++;
            else if(map[i][j]=='T')  num1++,num2++;
        }
        if(num1==4)  return 1;
        if(num2==4)  return 2;
    }

    for(int j=1;j<=4;j++)
    {
        num1=num2=0;
        for(int i=1;i<=4;i++)
        {
            if(map[i][j]=='X')  num1++;
            else if(map[i][j]=='O')  num2++;
            else if(map[i][j]=='T')  num1++,num2++;
        }
        if(num1==4)  return 1;
        if(num2==4)  return 2;
    }


        num1=num2=0;
        for(int i=1;i<=4;i++)
        {
            if(map[i][i]=='X')  num1++;
            else if(map[i][i]=='O')  num2++;
            else if(map[i][i]=='T')  num1++,num2++;
        }
        if(num1==4)  return 1;
        if(num2==4)  return 2;


        num1=num2=0;
        for(int i=1;i<=4;i++)
        {
            if(map[i][5-i]=='X')  num1++;
            else if(map[i][5-i]=='O')  num2++;
            else if(map[i][5-i]=='T')  num1++,num2++;
        }
        if(num1==4)  return 1;
        if(num2==4)  return 2;

        for(int i=1;i<=4;i++)
           for(int j=1;j<=4;j++)
              if(map[i][j]=='.')  return -1;

        return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cas,cas1=1;
    cin>>cas;
    while(cas--)
    {
        memset(map,0,sizeof(map));
        for(int i=1;i<=4;i++)  scanf("%s",map[i]+1);

        int ans=solve();

        printf("Case #%d: ",cas1++);
        if(ans==1)  printf("X won\n");
        else if(ans==2)  printf("O won\n");
        else if(ans==0)  printf("Draw\n");
        else if(ans==-1)  printf("Game has not completed\n");
    }
    return 0;
}
