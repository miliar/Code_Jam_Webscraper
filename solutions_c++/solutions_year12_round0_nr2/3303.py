#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#define MAX(X,Y) ((X)>(Y)?(X):(Y))
#define MIN(X,Y) ((X)<(Y)?(X):(Y))
#define ABS(X)  ((X)>0?(X):(-(X)))
#define SWAP(TYPE,X,Y) {TYPE T=X; X=Y; Y=T;}
int nCase;
using namespace std;
//#define SMALL
#define LARGE
int n, s, p, sc[105];
int chk(int val1, int val2)
{
    for(int i1=p; i1<=10; i1++)
        for(int i2=0; i2<=10; i2++)
        {
            int x = val1-i1-i2;
            int y = val2-i1-i2;
            if(x>=0 && x<=10 && y>=0 && y<=10)
                return 1;
        }
    return 0;
}
int main()
{
    #ifdef SMALL
    	freopen("B-small-attempt0.in","rt",stdin);
        freopen("B-small.out","wt",stdout);
    #endif
    #ifdef LARGE
    	freopen("B-large.in","rt",stdin);
        freopen("B-large.out","wt",stdout);
    #endif
    
    scanf("%d",&nCase);
    for(int iCase=1; iCase<=nCase; iCase++)
    {
        int ct=0;
        printf("Case #%d: ",iCase);
        scanf("%d%d%d",&n,&s,&p);
        for(int i=1; i<=n; i++)
            scanf("%d",&sc[i]);
        for(int i=1; i<=n; i++)
        {
//            printf("\n%d %d",sc[i],3*p);
            if(sc[i]<p)
                continue;
            if(sc[i]>=3*p)
                ct++;
            else if(3*p-sc[i]<=2  &&  3*p-sc[i]>=0)
                ct++;
            else if(s>0  &&  3*p-sc[i]<=4  &&  3*p-sc[i]>=0)
            {
                s--;
                ct++;
            }
        }
        printf("%d\n",ct);
    }
    scanf(" ");
    return 0;
}
