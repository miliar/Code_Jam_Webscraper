#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef pair<int,int> PI;
typedef vector<pair<int,int> > VPI;
typedef vector<string> VS;


#define ST          first
#define ND          second
#define ALL(x)      (x).begin(), (x).end()
#define FOR(i,s,n)  for(i=s;i<(n);++i)
#define REP(i,s,n)  for(i=s;i<=(n);++i)
#define LOOP(i,x)   for(i=0;i<SZ(x);++i)
#define IT(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define PB          push_back
#define MP          make_pair
#define SZ(x)       (int)(x.size())
#define DISP(x)     cout << #x << ": " << x << endl;

int b[2][105][105],X1,X2,Y1,Y2,c;

void disp(int c)
{
    int i,j;

    FOR(i,1,7)
    {
        FOR(j,1,7)
        {
            printf("%d",b[c][i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

bool iter()
{
    int x,y,i,j;
    bool ret=false;

    FOR(x,1,102) FOR(y,1,102)
    {
        if(b[c][y][x]) ret=true;
        b[1-c][y][x]=b[c][y][x];
        if(!b[c][y-1][x] && !b[c][y][x-1] && b[c][y][x])
            b[1-c][y][x]=0;
        if(b[c][y-1][x] && b[c][y][x-1] && !b[c][y][x])
            b[1-c][y][x]=1;
    }
    c=1-c;
    //DISP(ret);
    //disp(c);

    return ret;
}

int solve()
{
    int ret=0;
    c=0;
    while(iter())
        ++ret;
    return ret;
}

int main()
{
    int i,j,t,kase,n,k,R,x,y,x1,x2,y1,y2;
    //FILE * fin=fopen("sample.txt","r");
    FILE * fin=fopen("C-small-attempt0.in","r");
    //FILE * fin=fopen("A-large.in","r");
    FILE * fout=fopen("out.txt","w");

    fscanf(fin,"%d",&t);
    for(kase=1;kase<=t;++kase)
    {
        fscanf(fin,"%d",&R);
        FOR(x,0,105) FOR(y,0,105) b[0][x][y]=b[1][x][y]=0;
        FOR(i,0,R)
        {
            fscanf(fin,"%d %d %d %d",&x1,&y1,&x2,&y2);
            FOR(x,x1,x2+1)
                FOR(y,y1,y2+1)
                    b[0][y][x]=1;
        }
        //disp(0);

        fprintf(fout,"Case #%d: %d\n",kase,solve());
        cout << "*";
    }

	return 0;
}
