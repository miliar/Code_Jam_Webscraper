#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <queue>
#include <deque>
#include <set>

using namespace std;

#define mem(i,n) memset(i,n,sizeof(i))
#define fo(i,n) for(i=0;i<(n);i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define sz size()
#define cs c_str()

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

FILE *in=fopen("A-large.in","r");
FILE *out=fopen("Saving The Universe.out","w");

int N,S,Q,best[1001][104];
char SS[101][101],QQ[1001][101];

int solve(int ind,int s)
{
    if(ind==Q)return 0;
    if(best[ind][s]!=-1)return best[ind][s];
    int ret=1<<30,i;
    if(s==101 || (string)QQ[ind]==(string)SS[s])
    {
        int c=1;
        if(s==101)c--;
        fo(i,S)
        {
            if((string)SS[i]!=(string)QQ[ind])
                ret=min(ret,solve(ind+1,i)+c);
        }
    }
    else ret=min(ret,solve(ind+1,s));
    //printf("%d\n",ret);
    return best[ind][s]=ret;
}

int main()
{
    int p=0,i,j;
    fscanf(in,"%d\n",&N);
    while(p!=N)
    {
        fscanf(in,"%d\n",&S);
        fo(i,S)
        {
            char x;
            j=0;
            fscanf(in,"%c",&x);
            while(x!='\n')
            {
                SS[i][j]=x;
                j++;
                fscanf(in,"%c",&x);
            }
            SS[i][j]='\0';
        }
        fscanf(in,"%d\n",&Q);
        fo(i,Q)
        {
            char x;
            j=0;
            fscanf(in,"%c",&x);
            while(x!='\n')
            {
                QQ[i][j]=x;
                j++;
                fscanf(in,"%c",&x);
            }
            QQ[i][j]='\0';
        }
        mem(best,-1);
        int ret=solve(0,101);
        fprintf(out,"Case #%d: %d\n",p+1,ret);
        //fo(i,S)printf("%s\n",SS[i]);
        //printf("\n");
        //fo(i,Q)printf("%s\n",QQ[i]);
        //printf("\n");
        //printf("\n");
        p++;
    }
    //getchar();
    return 0;
}






























