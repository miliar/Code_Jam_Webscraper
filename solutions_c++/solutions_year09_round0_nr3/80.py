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

int n,best[505][22];
string s,c="welcome to code jam";

int solve(int ind,int x)
{//printf("%d %d\n",ind,x);
    if(best[ind][x]!=-1)return best[ind][x];
    if(x==18)return 1;
    int ret=0;
    for(int i=ind+1;i<s.sz;i++)
    {
        if(s[i]==c[x+1])
        {
            ret+=solve(i,x+1);
            ret%=10000;
        }
    }
    return best[ind][x]=ret;
}

FILE*in=fopen("C-large.in","r");
FILE*out=fopen("C-large.out","w");

int main()
{
    fscanf(in,"%d%*c",&n);
    for(int i=0;i<n;i++)
    {
        int ret=0;
        clr(best,-1);
        char x;
        s="";
        fscanf(in,"%c",&x);
        while(x!='\n')
        {
            s+=x;
            fscanf(in,"%c",&x);
        }
        for(int j=0;j<s.sz;j++)
        {
            if(s[j]=='w')
            {
                ret+=solve(j,0);
                ret%=10000;
            }
        }
        fprintf(out,"Case #%d: ",i+1);
        if(ret<1000)fprintf(out,"0");
        if(ret<100)fprintf(out,"0");
        if(ret<10)fprintf(out,"0");
        fprintf(out,"%d\n",ret);
    }
    return 0;
}






























