#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
#include<math.h>
#include<stack>
using namespace std;
char map[10][10];
int solve()
{
    int i,j,k,m,n;
    int b=0;
    int sum;
    for(i=0;i<4;i++)
    {
         sum=0;
        for(j=0;j<4;j++)
            if(map[i][j]=='X'||map[i][j]=='T')
            sum++;
        if(sum==4)
            return 2;
    }
     for(j=0;j<4;j++)
    {
         sum=0;
        for(i=0;i<4;i++)
            if(map[i][j]=='X'||map[i][j]=='T')
            sum++;
        if(sum==4)
            return 2;
    }
    sum=0;
    for(i=0;i<4;i++)
        if(map[i][i]=='X'||map[i][i]=='T')
        sum++;
    if(sum==4)
        return 2;
        sum=0;
        for(i=3;i>=0;i--)
            if(map[3-i][i]=='X'||map[3-i][i]=='T')
            sum++;
        if(sum==4)
            return 2;
    //X win

    sum=0;
     for(i=0;i<4;i++)
    {
         sum=0;
        for(j=0;j<4;j++)
            if(map[i][j]=='O'||map[i][j]=='T')
            sum++;
        if(sum==4)
            return 3;
    }
     for(j=0;j<4;j++)
    {
         sum=0;
        for(i=0;i<4;i++)
            if(map[i][j]=='O'||map[i][j]=='T')
            sum++;
        if(sum==4)
            return 3;
    }
    sum=0;
    for(i=0;i<4;i++)
        if(map[i][i]=='O'||map[i][i]=='T')
        sum++;
    if(sum==4)
        return 3;
        sum=0;
        for(i=3;i>=0;i--)
            if(map[3-i][i]=='O'||map[3-i][i]=='T')
            sum++;
        if(sum==4)
            return 3;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if(map[i][j]=='.')
        return 0;
    return 1;
}
int main()
{
    FILE *fp1,*fp2;
    fp1=fopen("A-large.in","r");
    fp2=fopen("A-large1.out","w");
    int i,j,k,m,n;
    int ca;
    fscanf(fp1,"%d",&ca);
    for(int t=1;t<=ca;t++)
    {
        for(i=0;i<4;i++)
            fscanf(fp1,"%s",map[i]);
        int tem=solve();
        fprintf(fp2,"Case #%d: ",t);
        if(tem==0)
            fprintf(fp2,"Game has not completed\n");
        else if(tem==1)
            fprintf(fp2,"Draw\n");
        else if(tem==2)
            fprintf(fp2,"X won\n");
        else
            fprintf(fp2,"O won\n");
    }
    fclose(fp1);
    fclose(fp2);
    return 0;
}
