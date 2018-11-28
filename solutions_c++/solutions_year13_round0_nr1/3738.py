#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>
#define MOD 1000000007
using namespace std;
int ar[9][9];
int mymap[6];
int main()
{
    char ch;
    int t,n;
    int ctr=0;
    scanf("%d",&t);
    while(t--)
    {
        /*for(int i=0;i<6;i++)
        {
            for(int j=0;j<6;j++)
            {
                ar[i][j]=-1;
            }
        }*/
        getchar();
        ctr++;
        int spl=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%c",&ch);
                if(ch=='O')
                ar[i][j]=1;
                else if(ch=='X')
                ar[i][j]=2;
                else if(ch=='T')
                ar[i][j]=3;
                else
                ar[i][j]=0;

                if(ar[i][j]==0)
                spl++;
            }
            getchar();
        }
        mymap[0]=0;
        mymap[1]=0;
        mymap[2]=0;
        mymap[3]=0;
        int ans=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                mymap[ar[i][j]]++;
            }
            if((mymap[1]==3 && mymap[3]==1)||(mymap[2]==3 && mymap[3]==1)||(mymap[1]==4)||(mymap[2]==4))
            {
                ans=1;
                break;
            }
            mymap[0]=0;
            mymap[1]=0;
            mymap[2]=0;
            mymap[3]=0;
        }
        for(int j=1;j<=4 && ans!=1;j++)
        {
            for(int i=1;i<=4;i++)
            {
                mymap[ar[i][j]]++;
            }
            if((mymap[1]==3 && mymap[3]==1)||(mymap[2]==3 && mymap[3]==1)||(mymap[1]==4)||(mymap[2]==4))
            {
                ans=1;
                break;
            }
            mymap[0]=0;
            mymap[1]=0;
            mymap[2]=0;
            mymap[3]=0;
        }
        for(int i=1;i<=1 && ans!=1;i++)
        {
            mymap[ar[1][1]]++;
            mymap[ar[2][2]]++;
            mymap[ar[3][3]]++;
            mymap[ar[4][4]]++;

            if((mymap[1]==3 && mymap[3]==1)||(mymap[2]==3 && mymap[3]==1)||(mymap[1]==4)||(mymap[2]==4))
            {
                ans=1;
                break;
            }
            mymap[0]=0;
            mymap[1]=0;
            mymap[2]=0;
            mymap[3]=0;
        }
        for(int i=1;i<=1 && ans!=1;i++)
        {
            mymap[ar[4][1]]++;
            mymap[ar[3][2]]++;
            mymap[ar[2][3]]++;
            mymap[ar[1][4]]++;


            if((mymap[1]==3 && mymap[3]==1)||(mymap[2]==3 && mymap[3]==1)||(mymap[1]==4)||(mymap[2]==4))
            {
                ans=1;
                break;
            }
            mymap[0]=0;
            mymap[1]=0;
            mymap[2]=0;
            mymap[3]=0;
        }
        printf("Case #%d: ",ctr);
        if(ans==1)
        {
            if((mymap[1]==3 && mymap[3]==1)||(mymap[1]==4))
            {
                printf("O won\n");
            }
            else if((mymap[2]==3 && mymap[3]==1)||(mymap[2]==4))
            {
                printf("X won\n");
            }
        }
        else
        {
            if(spl>0)
            {
                printf("Game has not completed\n");
            }
            else
            {
                printf("Draw\n");
            }
        }

    }
    return 0;
}
