#include<cstdio>
#include<cstring>
#include<string.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define MAX 512
int M,N;
int flag[MAX+1];
void update(int idx,char A[],char c)
{
    string temp;
    switch(c)
    {
        case '0':temp="0000";
            break;
        case '1':temp="0001";
            break;
        case '2':temp="0010";
            break;
        case '3':temp="0011";
            break;
        case '4':temp="0100";
            break;
        case '5':temp="0101";
            break;
        case '6':temp="0110";
            break;
        case '7':temp="0111";
            break;
        case '8':temp="1000";
            break;
        case '9':temp="1001";
            break;
        case 'A':temp="1010";
            break;
        case 'B':temp="1011";
            break;
        case 'C':temp="1100";
            break;
        case 'D':temp="1101";
            break;
        case 'E':temp="1110";
            break;
        case 'F':temp="1111";
            break;
    }
    //copy temp
    for(int j=0;j<4;j++)
    A[idx+j]=temp[j];
}

char grid[MAX][MAX];
inline bool validate(int r1,int r2,int c1,int c2)
{
    for(int i=r1;i<r2;i++)
    {
        for(int j=c1;j<c2;j++)
        {
            if(grid[i][j]=='X')
            return false;
        }
    }
    return true;
}
void check(int r1,int c1,int len)
{
    register int i,j;
    bool f=true;
    //validate
    if(!validate(r1,r1+len,c1,c1+len))
    return;
    for(i=r1;i<r1+len;i++)
    {
        for(j=c1;j<c1+len;j++)
        {
            if(j==c1 && i!=r1)
            {
                //check wit top
                if(grid[i][j]==grid[i-1][j])
                {
                    f=false;
                    goto stop;
                }
            }
            if(j>c1)
            {
                if(grid[i][j]==grid[i][j-1])
                {
                    f=false;
                    goto stop;
                }
            }
        }
    }
    stop:
    if(f)
    {
        //mark all of them used
        for(i=r1;i<r1+len;i++)
            for(j=c1;j<c1+len;j++)
                grid[i][j]='X';
        flag[len]++;
    }
}
void solve()
{
    int row;
    int minL=min(M,N);
    for(row=minL;row>=1;row--)
    {
        //we want boards of row*row
        register int i,j;
        for(i=0;i<M;i++)
        {
            for(j=0;j<N;j++)
            {
                //i,j is start
                if(i+row<=M && j+row<=N)
                    check(i,j,row);
                else
                break;
            }
        }
    }
}


int main()
{
    FILE *in,*out;
    in=fopen("in.txt","r");
    out=fopen("out.txt","w");
    int cases;
    int T;
    fscanf(in,"%d",&T);
    register int i,j;
    for(cases=1;cases<=T;cases++)
    {
        fscanf(in,"%d %d",&M,&N);
        char s[130];
        memset(flag,0,sizeof(flag));
        for(i=0;i<M;i++)
        {
            fscanf(in,"%s",s);
            //read s
            int cntr=0;
            for(j=0;j<N/4;cntr+=4,j++)
                update(cntr,grid[i],s[j]);
            grid[i][N]='\0';
        }
        //now search for boards
        solve();
        int cnt=0;
        //search diff board sizes
        for(i=1;i<MAX+1;i++)
        if(flag[i]>0)
        cnt++;
        /*for(i=0;i<M;i++)
        printf("%s\n",grid[i]);*/
        fprintf(out,"Case #%d: %d\n",cases,cnt);
        for(i=min(M,N);i>=1;i--)
        if(flag[i]>0)
        fprintf(out,"%d %d\n",i,flag[i]);
    }
    return 0;
}
