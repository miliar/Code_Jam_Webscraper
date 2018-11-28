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

int L,D,N;
vector<string > arr;
string d[5000];

FILE*in=fopen("A-large.in","r");
FILE*out=fopen("A-large.out","w");

int main()
{
    fscanf(in,"%d %d %d",&L,&D,&N);
    for(int i=0;i<D;i++)
    {
        char x[5555];
        fscanf(in,"%s",x);
        d[i]=x;
    }
    for(int i=0;i<N;i++)
    {
        int ret=0;
        arr.clear();
        char x[5555];
        fscanf(in,"%s",x);
        int n=strlen(x),c=0;
        string h;
        for(int j=0;j<n;j++)
        {
            if(x[j]=='(')c++;
            if(x[j]==')')c--;
            if(isalpha(x[j]))
            {
                if(c==0)
                {
                    h="";
                    h+=x[j];
                    arr.pb(h);
                    h="";
                }
                else h+=x[j];
            }
            else
            {
                if(h.sz)
                {
                    arr.pb(h);
                }
                h="";
            }
        }
        for(int j=0;j<D;j++)
        {
            int k;
            for( k=0;k<d[j].sz;k++)
            {
                if(arr[k].find(d[j][k])==-1)break;
            }
            if(k==d[j].sz)ret++;
        }
        fprintf(out,"Case #%d: %d\n",i+1,ret);
    }
    return 0;
}





/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(aa)bc
*/























