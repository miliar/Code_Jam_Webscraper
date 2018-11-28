#include<iostream>
#include<cstdio>

using namespace std;

char arr[4][5];

int check(char ch)
{
    int count=0,i,j;
    for(i=0;i<4;i++)
    {
        count=0;
        for(j=0;j<4;j++)
        {
            if(arr[i][j]==ch || arr[i][j]=='T')
            count++;
            else
            break;
        }
        if(count==4)
        return(1);
    }
    for(i=0;i<4;i++)
    {
        count=0;
        for(j=0;j<4;j++)
        {
            if(arr[j][i]==ch || arr[j][i]=='T')
            count++;
            else
            break;
        }
        if(count==4)
        return(1);
    }

    count=0;
    for(i=0,j=0;i<4 && j<4;i++,j++)
    {
        if(arr[i][j]==ch || arr[i][j]=='T')
        count++;
        else
        break;
    }
    if(count==4)
    return(1);

    count=0;
    for(i=3,j=0;i>=0 && j<4;i--,j++)
    {
        if(arr[i][j]==ch || arr[i][j]=='T')
        count++;
        else
        break;
    }
    if(count==4)
    return(1);

    return(0);
}

int main()
{
    FILE *fin=fopen("A-large.in","r");
    FILE *fout=fopen("output.txt","w");
    int t,i,x,j,complete;
    fscanf(fin,"%d",&t);
    for(x=1;x<=t;x++)
    {
        for(i=0;i<4;i++)
        fscanf(fin,"%s",arr[i]);

        complete=1;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        if(arr[i][j]=='.')
        complete=0;

        if(check('X'))
        fprintf(fout,"Case #%d: X won\n",x);
        else if(check('O'))
        fprintf(fout,"Case #%d: O won\n",x);
        else if(complete==0)
        fprintf(fout,"Case #%d: Game has not completed\n",x);
        else
        fprintf(fout,"Case #%d: Draw\n",x);
    }
    return(0);
}
