#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

char str[10][10];

int check()
{
    for(int i=0;i<4;i++)
    {
        int num1=0,num2=0,num3=0,num4=0;
        for(int j=0;j<4;j++)
        {
            if(str[i][j]=='X' || str[i][j]=='T')num1++;
            if(str[i][j]=='O' || str[i][j]=='T')num2++;
            if(str[j][i]=='X' || str[j][i]=='T')num3++;
            if(str[j][i]=='O' || str[j][i]=='T')num4++;
        }
        if(num1==4 || num3==4)return 1;
        if(num2==4 || num4==4)return 2;
    }
    int num1=0,num2=0,num3=0,num4=0;
    for(int i=0;i<4;i++)
    {
      if(str[i][i]=='X' || str[i][i]=='T')num1++;
      if(str[i][i]=='O' || str[i][i]=='T')num2++;
      if(str[i][3-i]=='X' || str[i][3-i]=='T')num3++;
      if(str[i][3-i]=='O' || str[i][3-i]=='T')num4++;
    }
    if(num1==4 || num3==4)return 1;
    if(num2==4 || num4==4)return 2;
    for(int i=0;i<4;i++)
      for(int j=0;j<4;j++)
        if(str[i][j]=='.')return 3;
    return 0;
}

int main()
{
    freopen("x.in","r",stdin);
    freopen("x.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int K=1;K<=T;K++)
    {
        for(int i=0;i<4;i++)
          scanf(" %s",str[i]);
        printf("Case #%d: ",K);
        switch(check())
        {
            case 0:puts("Draw");break;
            case 1:puts("X won");break;
            case 2:puts("O won");break;
            case 3:puts("Game has not completed");break;
        }
    }
    return 0;
}
