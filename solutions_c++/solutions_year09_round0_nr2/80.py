#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include<sstream>
#include<iostream>
#include<queue>
#include<set>
#include<map>

using namespace std;

#define clr(i,n) memset(i,n,sizeof(i))
#define fo(i,a) for(i=0;i<a;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define sz size()

typedef vector<int> vi;
typedef vector<string> vs;

int T;
int h,w,arr[200][200],vis[200][200],t,N,v[200000],dx[5]={-1,0,0,1},dy[5]={0,-1,1,0};
char l[200000],ret[200][200];

FILE*in=fopen("B-large.in","r");
FILE*out=fopen("B-large.out","w");

int main()
{
    fscanf(in,"%d",&T);
    int p=0;
    while(T--)
    {
        clr(vis,0);
        t=0;
        fscanf(in,"%d %d",&h,&w);
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
            {
                fscanf(in,"%d",&arr[i][j]);
                vis[i][j]=i*w+j;
            }
        }
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
            {
                int r=i,c=j;
                while(1)
                {
                    int rr,cc,mini=1<<30;
                    for(int k=0;k<4;k++)
                    {
                        if(r+dx[k]>=0 && r+dx[k]<h && c+dy[k]>=0 && c+dy[k]<w)
                        {
                            if(mini>arr[r+dx[k]][c+dy[k]] && arr[r+dx[k]][c+dy[k]]<arr[r][c])
                            {
                                mini=arr[r+dx[k]][c+dy[k]];
                                rr=r+dx[k];
                                cc=c+dy[k];
                            }
                        }
                    }
                    if(mini==1<<30)break;
                    r=rr;
                    c=cc;
                }
                vis[i][j]=vis[r][c];
            }
        }
        clr(v,0);
        char C='a';
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
            {
                if(!v[vis[i][j]])
                {
                    v[vis[i][j]]=1;
                    l[vis[i][j]]=C;
                    C++;
                }
                ret[i][j]=l[vis[i][j]];
            }
        }
        fprintf(out,"Case #%d:\n",p+1);
        for(int i=0;i<h;i++)
        {
            for(int j=0;j<w;j++)
            {
                fprintf(out,"%c",ret[i][j]);
                if(j!=w-1)fprintf(out," ");
            }
            fprintf(out,"\n");
        }
        p++;
    }

    return 0;
}






























