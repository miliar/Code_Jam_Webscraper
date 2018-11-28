#include <iostream>
#include <math.h>
#include <list>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <memory.h>
#include <map>
#include <stack>
#include <queue>
#include <set>
#include <stdio.h>
#include <assert.h>

using namespace std;
#define SET(a,n) memset(a,n,sizeof(a));
#define FOR(a,b,c) for(int a=b;a<c;++a)
#define GN(a) scanf("%d",&a)

typedef long long int LL;
typedef vector<int> VI;

using namespace std;

int graph[102][102];
int n;
int win[102],played[102];
double owp[102],oowp[102];

int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);
    int t;
    char c;
    cin>>t;

    FOR(test,1,t+1)
    {
        cin>>n;
        SET(graph,-1);
        SET(win,0);
        SET(played,0);
        FOR(i,0,n)FOR(j,0,n)
        {
            cin>>c;
            if(c=='0')graph[i][j]=0;
            else if(c=='1')graph[i][j]=1;
        }
        FOR(i,0,n)FOR(j,0,n)
        {
            if(graph[i][j]==1)win[i]++;
            if(graph[i][j]!=-1)played[i]++;
        }
        FOR(i,0,n)
        {
            owp[i]=0.0;
            FOR(j,0,n)
            {
                if(graph[i][j]!=-1)
                {
                    int num = win[j];
                    if(graph[i][j]==0)num--;
                    owp[i]+=(double)num/(played[j]-1);
                }
            }
            owp[i]=owp[i]/played[i];
        }
        FOR(i,0,n)
        {
            oowp[i]=0.0;
            FOR(j,0,n)
            {
                if(graph[i][j]!=-1)
                {
                    oowp[i]+=owp[j];
                }
            }
            oowp[i]=oowp[i]/played[i];
        }

        double r[102];

        FOR(i,0,n)
        {
            r[i]=0.25*win[i]/played[i];
            r[i]+=0.50*owp[i] + 0.25*oowp[i];
        }

        cout<<"Case #"<<test<<":\n";

        FOR(i,0,n)printf("%.12f\n",r[i]);
    }

    return 0;
}

