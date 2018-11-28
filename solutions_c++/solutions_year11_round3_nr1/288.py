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
char g[100][100];

int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);

    int t;
    cin>>t;
    char c;
    FOR(test,1,t+1)
    {
        int R,C;
        cin>>R>>C;
        FOR(i,0,R)FOR(j,0,C)cin>>g[i][j];
        bool valid = 1;
        FOR(i,0,R)
        {
            FOR(j,0,C)
            {
                if(g[i][j]=='#')
                {
                    if(!(i+1<R && j+1<C))
                    {
                        valid = 0;
                        break;
                    }
                    if(!(g[i][j+1]=='#' && g[i+1][j]=='#' && g[i+1][j+1]=='#'))
                    {
                        valid = 0;
                        break;
                    }
                    g[i][j]='/';
                    g[i+1][j]='\\';
                    g[i][j+1]='\\';
                    g[i+1][j+1]='/';
                }
                if(!valid)break;
            }
            if(!valid)break;
        }
        cout<<"Case #"<<test<<":\n";
        if(!valid)
        {
            cout<<"Impossible"<<endl;
        }
        else
        {
            FOR(i,0,R)
            {
                FOR(j,0,C)
                {
                    cout<<g[i][j];
                }
                cout<<endl;
            }
        }
    }
    return 0;
}

