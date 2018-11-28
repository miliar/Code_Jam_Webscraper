#include<stdio.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#define pi 2*acos(0)
#define inf INT_MAX
#define eps 0.00000001
using namespace std;

main()
{
    int i,j,n,p,flag,flag1;
    char arr[110][110],ch;
    FILE *read,*write;
    read=fopen("codejamin.txt","r");
    write=fopen("codejamout.txt","w");
    fscanf(read," %d",&n);
    for(p=1;p<=n;p++)
    {
        fscanf(read," %s",&arr[0]);
        fscanf(read," %s",&arr[1]);
        fscanf(read," %s",&arr[2]);
        fscanf(read," %s",&arr[3]);
        flag1=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(arr[i][j]=='.')
                {flag1=1;
                break;}
            }
        }
        flag=0;
        if(arr[0][0]=='X'||arr[0][0]=='T')
        {
            if((arr[1][1]=='X'||arr[1][1]=='T')&&(arr[2][2]=='X'||arr[2][2]=='T')&&(arr[3][3]=='X'||arr[3][3]=='T'))
            flag=1;
        }
        if(arr[0][0]=='O'||arr[0][0]=='T')
        {
            if((arr[1][1]=='O'||arr[1][1]=='T')&&(arr[2][2]=='O'||arr[2][2]=='T')&&(arr[3][3]=='O'||arr[3][3]=='T'))
            flag=2;
        }
        if(arr[0][3]=='X'||arr[0][3]=='T')
        {
            if((arr[1][2]=='X'||arr[1][2]=='T')&&(arr[2][1]=='X'||arr[2][1]=='T')&&(arr[3][0]=='X'||arr[3][0]=='T'))
            flag=1;
        }
        if(arr[0][3]=='O'||arr[0][3]=='T')
        {
            if((arr[1][2]=='O'||arr[1][2]=='T')&&(arr[2][1]=='O'||arr[2][1]=='T')&&(arr[3][0]=='O'||arr[3][0]=='T'))
            flag=2;
        }
        for(i=0;i<4&&flag==0;i++)
        {
            if(arr[i][0]=='X'||arr[i][0]=='T')
            {
            if((arr[i][1]=='X'||arr[i][1]=='T')&&(arr[i][2]=='X'||arr[i][2]=='T')&&(arr[i][3]=='X'||arr[i][3]=='T'))
            flag=1;
            }
            if(arr[i][0]=='O'||arr[i][0]=='T')
            {
             if((arr[i][1]=='O'||arr[i][1]=='T')&&(arr[i][2]=='O'||arr[i][2]=='T')&&(arr[i][3]=='O'||arr[i][3]=='T'))
            flag=2;
            }
        }
        for(i=0;i<4&&flag==0;i++)
        {
            if(arr[0][i]=='X'||arr[0][i]=='T')
            {
            if((arr[1][i]=='X'||arr[1][i]=='T')&&(arr[2][i]=='X'||arr[2][i]=='T')&&(arr[3][i]=='X'||arr[3][i]=='T'))
            flag=1;
            }
            if(arr[0][i]=='O'||arr[0][i]=='T')
            {
             if((arr[1][i]=='O'||arr[1][i]=='T')&&(arr[2][i]=='O'||arr[2][i]=='T')&&(arr[3][i]=='O'||arr[3][i]=='T'))
            flag=2;
            }
        }
        if(flag==1)
        fprintf(write,"Case #%d: X won\n",p);
        else if(flag==2)
        fprintf(write,"Case #%d: O won\n",p);
        else if(flag1==0)
        fprintf(write,"Case #%d: Draw\n",p);
        else
        fprintf(write,"Case #%d: Game has not completed\n",p);
        fscanf(read,"%c%c",&ch,&ch);
    }
    fclose(read);
    fclose(write);
    return 0;
}
