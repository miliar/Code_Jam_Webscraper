#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
using namespace std;
char grid[7][7];
int r[]={0,1,2,3};
int c[]={3,2,1,0};
bool check_X()
{
    for(int i=0; i<4; i++)
    {
        int x=0,t=0;
        for(int j=0; j<4; j++)
        {
            if(grid[i][j]=='X')
                x++;
            if(grid[i][j]=='T')
                t++;

        }
        if(x==4||(x==3&&t==1))
            return true;
    }
    for(int j=0; j<4; j++)
    {
        int x=0,t=0;
        for(int i=0; i<4; i++)
        {
            if(grid[i][j]=='X')
                x++;
            if(grid[i][j]=='T')
                t++;

        }
        if(x==4||(x==3&&t==1))
            return true;
    }

    int x=0,t=0;

    for(int i=0; i<4; i++)
    {
        if(grid[i][i]=='X')
            x++;
        if(grid[i][i]=='T')
            t++;
    }
    if(x==4||(x==3&&t==1))
        return true;

    x=0,t=0;


for(int k=0;k<4;k++)
    {
        int i, j;
        i=r[k];
        j=c[k];
        if(grid[i][j]=='X')
            x++;
        if(grid[i][j]=='T')
            t++;
    }
    if(x==4||(x==3&&t==1))
        return true;

    return false;


}
bool check_o()
{
    for(int i=0; i<4; i++)
    {
        int y=0,t=0;
        for(int j=0; j<4; j++)
        {
            if(grid[i][j]=='O')
                y++;
            if(grid[i][j]=='T')
                t++;

        }
        if(y==4||(y==3&&t==1))
            return true;
    }
    for(int j=0; j<4; j++)
    {
        int y=0,t=0;
        for(int i=0; i<4; i++)
        {
            if(grid[i][j]=='O')
                y++;
            if(grid[i][j]=='T')
                t++;

        }
        if(y==4||(y==3&&t==1))
            return true;


    }
    int y=0,t=0;
    for(int i=0; i<4; i++)
    {
        if(grid[i][i]=='O')
            y++;
        if(grid[i][i]=='T')
            t++;
    }
    if(y==4||(y==3&&t==1))
        return true;
    y=0,t=0;
    for(int k=0; k<4; k++)
    {
        int i,j;
        i=r[k];
        j=c[k];
        if(grid[i][j]=='O')
            y++;
        if(grid[i][j]=='T')
            t++;
           // cout<<grid[i][j]<<"  ";
    }
   // cout<<y<<"   "<<t<<endl;
    if(y==4||(y==3&&t==1))
        return true;


    return false;

}
bool check_complete()
{
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            if(grid[i][j]=='.')
                return true;

    return false;
}
int main()
{
    FILE *f;
   f=fopen("outputA.txt","w");
    int t,kase=1;
    scanf("%d\n",&t);
    while(t--)
    {
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
                cin>>grid[i][j];
        }
       // getchar();


       // for(int k=0;k<4;k++)
       //     cout<<grid[r[k]][c[k]]<<" ";
       // cout<<"Case #"<<kase++<<": ";

        if(check_X())
        {
             fprintf(f,"Case #%d: ",kase++);
            fprintf(f,"X won\n");

        }
        else if(check_o())
        {
             fprintf(f,"Case #%d: ",kase++);
            fprintf(f,"O won\n");

        }
        else if(check_complete())
        {
             fprintf(f,"Case #%d: ",kase++);
            fprintf(f,"Game has not completed\n");
        }
        else
        {
             fprintf(f,"Case #%d: ",kase++);
             fprintf(f,"Draw\n");
        }






    }
}
