#include<iostream>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#define max(a,b)(a>b?a:b)
#define min(a,b)(a<b?a:b)
#define inf 100000

using namespace std;

char in1[51][51],in[51][51];
int blue,red;

void col_check(int N,int K);
void r_dia(int N,int K);
void l_dia(int N,int K);
void row_check(int N,int K);

int main()
{
    freopen("A.in","r",stdin);
    freopen("A_out.txt","w",stdout);
    int test,i,j,k,N,K,f,x,b,r,_case=1;
    queue<int>ind;

    scanf("%d",&test);

    while(test--)
    {
        scanf("%d %d",&N,&K);

        for(i=0;i<N;i++){
            scanf("%s",in[i]);
            /*for(j=0;j<N;j++)
                if(in[i][j]=='B'||in[i][j]=='R')
                    continue;
                else in[i][j]='.';
            in[i][j]=0;*/
        }

        for(i=0;i<N;i++)
        {
            for(j=k=N-1;j>=0;j--)
                if(in[i][j]!='.')
                    in[i][k--]=in[i][j];
            for(k;k>=0;k--)
                in[i][k]='.';
        }
        for(i=0;i<N;i++)
            strcpy(in1[i],in[i]);

        /*if(_case==60){
            printf("%d %d\n",N,K);
            for(i=0;i<N;i++)
                printf("%s\n",in1[i]);
        }*/

        blue=red=0;

        row_check(N,K);
        col_check(N,K);
        r_dia(N,K);
        l_dia(N,K);

        printf("Case #%d: ",_case++);

        if(blue&&red)
            printf("Both\n");
        else if(blue)
            printf("Blue\n");
        else if(red)
            printf("Red\n");
        else printf("Neither\n");
    }

    return 0;
}

void row_check(int N,int K)
{
    int i,j,a,b,r;
    for(i=0;i<N;i++)//row check
        {
            b=r=0;
            for(j=0;j<N;j++)
            {
                if(in1[i][j]=='B')
                {
                    if(b) b++;
                    else{ r=0;b++;}
                    if(b==K)
                        blue=1;
                }
                else if(in1[i][j]=='R')
                {
                    if(r) r++;
                    else {r++;b=0;}
                    if(r==K)
                        red=1;
                }
                else
                {
                    b=r=0;
                }
            }
        }
}

void col_check(int N,int K)
{
    int i,j,b,r;

    for(i=0;i<N;i++)//col check
        {
            b=r=0;
            for(j=0;j<N;j++)
            {
                if(in1[j][i]=='B')
                {
                    if(b) b++;
                    else{ r=0;b++;}
                    if(b==K)
                        blue=1;
                }
                else if(in1[j][i]=='R')
                {
                    if(r) r++;
                    else {r++;b=0;}
                    if(r==K)
                        red=1;
                }
                else
                {
                    b=r=0;
                }
            }
        }
}

void r_dia(int N,int K)
{
    int i,j,k,b,r;

    for(j=0;j<N;j++)
    {
        k=j;
        b=r=0;
        for(i=0;i<N;i++,k++)
        {
            if(in1[i][k]=='B')
                {
                    if(b) b++;
                    else{ r=0;b++;}
                    if(b==K)
                        blue=1;
                }
                else if(in1[i][k]=='R')
                {
                    if(r) r++;
                    else {r++;b=0;}
                    if(r==K)
                        red=1;
                }
                else
                {
                    b=r=0;
                }
        }
    }

    for(i=1;i<N;i++)
    {
        k=i;
        b=r=0;
        for(j=0;j<N&&k<N;j++,k++)
        {
            if(in1[k][j]=='B')
                {
                    if(b) b++;
                    else{ r=0;b++;}
                    if(b==K)
                        blue=1;
                }
                else if(in1[k][j]=='R')
                {
                    if(r) r++;
                    else {r++;b=0;}
                    if(r==K)
                        red=1;
                }
                else
                {
                    b=r=0;
                }
        }
    }

}

void l_dia(int N,int K)
{
    int i,j,b,r,k;

    for(j=0;j<N;j++)
    {
        k=j;
        b=r=0;
        for(i=0;i<N&&k>=0;i++,k--)
        {
            if(in1[i][k]=='B')
                {
                    if(b) b++;
                    else{ r=0;b++;}
                    if(b==K)
                        blue=1;
                }
                else if(in1[i][k]=='R')
                {
                    if(r) r++;
                    else {r++;b=0;}
                    if(r==K)
                        red=1;
                }
                else
                {
                    b=r=0;
                }
        }
    }

    for(i=1;i<N;i++)
    {
        k=i;
        b=r=0;
        for(j=N-1;j>=0&&k<N;j--,k++)
        {
            if(in1[k][j]=='B')
                {
                    if(b) b++;
                    else{ r=0;b++;}
                    if(b==K)
                        blue=1;
                }
                else if(in1[k][j]=='R')
                {
                    if(r) r++;
                    else {r++;b=0;}
                    if(r==K)
                        red=1;
                }
                else
                {
                    b=r=0;
                }
        }
    }
}
