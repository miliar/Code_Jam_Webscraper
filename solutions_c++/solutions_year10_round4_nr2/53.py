#include<iostream>
#include<vector>
#include<cstring>
#include<stdio.h>
#include<string>
#include<cassert>
#include<algorithm>
using namespace std;

#define forn(i,n) for (int i=0;i<(n);i++)
#define init(a,v) memset(a,v,sizeof(a))
#define gi(t) scanf("%d",&(t))
#define sz 1050

// 1 - based
int p;
int miss[sz];
int cost[2*sz];
int tree[2*sz][12]; // Best code for tree rooted at [i] so that exactly [j] matches have been missed above

int INF = 1000000000; 

int main ()
{
    int nTest; gi(nTest);
    forn(test, nTest)
    {
        gi(p);
        forn(i, (1<<p)) { gi(miss[i]); }
        for (int level = p-1; level >= 0; level--)
            for (int i = (1<<level); i < (1<<(level+1)); i++)
                gi(cost[i]);
            
        forn(i,2*sz) forn(j,12) tree[i][j] = INF;
        forn(i, (1<<p)) forn(j,miss[i]+1)
            tree[(1<<p)+i][j] = 0;

        for (int level = p-1; level >= 0; level--)
            forn(i, (1<<level))
                forn(j,p+1)
                    tree[i + (1<<level)][j] = min(INF, min(tree[((i + (1<<level))<<1)][j+1] + tree[((i + (1<<level))<<1) + 1][j+1], cost[i + (1<<level)] + tree[((i + (1<<level))<<1)][j] + tree[((i + (1<<level))<<1) + 1][j]));
        cout << "Case #" << test+1 << ": " << tree[1][0] << endl;
    }
    return 0;
}
