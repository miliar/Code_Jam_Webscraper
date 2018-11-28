#include<iostream>
#include<cstdio>
using namespace std;
char arr[4][4];
bool won(int c)
{
    int o,x;
    for(int i=0;i<4;i++)
    {
        o=1;x=1;
        for(int j=0;j<4;j++)
        {
            if(arr[i][j]!='O'&&arr[i][j]!='T')o=0;
            if(arr[i][j]!='X'&&arr[i][j]!='T')x=0;
        }
        if(o==1){printf("Case #%d: O won\n",c);return 1;}
        if(x==1){printf("Case #%d: X won\n",c);return 1;}
    }
    for(int j=0;j<4;j++)
    {
        o=1;x=1;
        for(int i=0;i<4;i++)
        {
            if(arr[i][j]!='O'&&arr[i][j]!='T')o=0;
            if(arr[i][j]!='X'&&arr[i][j]!='T')x=0;
        }
        if(o==1){printf("Case #%d: O won\n",c);return 1;}
        if(x==1){printf("Case #%d: X won\n",c);return 1;}
    }
    o=1;x=1;
    for(int i=0;i<4;i++)
    {
        if(arr[i][i]!='O'&&arr[i][i]!='T')o=0;
        if(arr[i][i]!='X'&&arr[i][i]!='T')x=0;
    }
    if(o==1){printf("Case #%d: O won\n",c);return 1;}
    if(x==1){printf("Case #%d: X won\n",c);return 1;}
    o=1;x=1;
    for(int i=0;i<4;i++)
    {
        if(arr[i][3-i]!='O'&&arr[i][3-i]!='T')o=0;
        if(arr[i][3-i]!='X'&&arr[i][3-i]!='T')x=0;
    }
    if(o==1){printf("Case #%d: O won\n",c);return 1;}
    if(x==1){printf("Case #%d: X won\n",c);return 1;}
    return 0;
}
bool empty()
{
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(arr[i][j]=='.')return 1;
        }
    }
    return 0;
}
int main()
{
    int t,c=0;
    cin>>t;
    while(t--)
    {
        
        for(int i=0;i<4;i++)
        {
            scanf("%s",arr[i]);
        }
        c++;
        if(!won(c))
        {
            if(empty())printf("Case #%d: Game has not completed\n",c);
            else printf("Case #%d: Draw\n",c);
        }
    }
}
        
