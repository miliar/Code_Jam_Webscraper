#include<math.h>
#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
char map[11][11];
int state;
bool row(int r)
{
    char top=map[r][0];
    int cnt=0;
    for(int i=0; i<4; i++)
    {
        if(map[r][i]=='.')return 0;
        cnt+=(map[r][i]==top||map[r][i]=='T');
    }
    return cnt==4;
}
bool col(int c)
{
    char top=map[0][c];
    int cnt=0;
    for(int i=0; i<4; i++)
    {
        if(map[i][c]=='.')return 0;
        cnt+=(map[i][c]==top||'T'==map[i][c]);
    }
    return cnt==4;
}

void bfs()
{
    int i,j,k;
    for(i=0; i<4; i++)
    {
        if(row(i))
        {
            if('X'==map[i][0])state=0;
            else if('O'==map[i][0])state=1;
            return ;
        }
        else if(col(i))
        {
            if('X'==map[0][i])state=0;
            else state=1;
            return ;
        }
    }
    char top=map[0][0];
    k=0;
    for(i=0; i<4; i++)
    {
        if(map[i][i]=='.')break;
        k+=(map[i][i]==top||map[i][i]=='T');
    }
    if(k==4)
    {
        if('X'==top)state=0;
        else state=1;
        return ;
    }
    top=map[0][3];
    k=0;
    for(i=0; i<4; i++)
    {
        if(map[i][3-i]=='.')break;
        k+=(map[i][3-i]==top||map[i][3-i]=='T');
    }
    if(k==4)
    {
        if('X'==top)state=0;
        else state=1;
        return ;
    }
    //cout<<"ºÕºÕ"<<endl;
    int cnt=0;
    for(i=0; i<4; i++)
    {
        for(j=0; j<4; j++)
        {
            cnt+=(map[i][j]!='.');
        }
    }
    if(cnt==16)
    {
        state=2;
    }
    else
    {
        state=3;
    }
}
int main()
{
    int t;
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int z=1; z<=t; z++)
    {
        int i,j;
        for(i=0; i<4; i++)scanf("%s",&map[i]);
        printf("Case #%d: ",z);
        state=-1;
        bfs();
        if(state==0)printf("X won");
        else if(state==1)printf("O won");
        else if(state==2)printf("Draw");
        else printf("Game has not completed");
        cout<<endl;
    }
}
