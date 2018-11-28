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
#define LOOP(i,x)   for(i=0;i<SZ(x);++i)
#define IT(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define PB          push_back
#define MP          make_pair
#define SZ(x)       (int)(x.size())
#define DISP(x)     cerr << #x << ": " << x << endl;

#define MAX 1005

int K,N,R;
int g[MAX],reach[MAX],cost[MAX];

ull solve()
{
    ull ret=0;
    int i,j,k,r=R,cnt=0,cur=0,ci;
    int rep,rcost;
    FOR(i,0,N) reach[i]=-1;
    ci=0;
    while(r)
    {
        if(reach[ci]!=-1)
        {
            rep=cnt-reach[ci];
            rcost=ret-cost[ci];
            ret+=(r/rep)*rcost;
            r%=rep;
            FOR(i,0,N) reach[i]=-1;
            continue;
        }
        reach[ci]=cnt;
        cost[ci]=ret;
        if(g[ci]>K) return ret;
        cur=g[ci];
        for(i=(ci+1)%N;i!=ci;i=(i+1)%N)
        {
            if(cur+g[i]<=K)
            {
                cur+=g[i];
            } else
            {
                ci=i;
                break;
            }
        }
        ret+=cur;
        ++cnt;
        --r;
    }

    return ret;
}

int main()
{
    int i,j,t,kase;
    //FILE * fin=fopen("sample.txt","r");
    FILE * fin=fopen("C-small-attempt0.in","r");
    //FILE * fin=fopen("A-large.in","r");
    FILE * fout=fopen("out.txt","w");

    fscanf(fin,"%d",&t);
    for(kase=1;kase<=t;++kase)
    {
        fscanf(fin,"%d %d %d",&R,&K,&N);
        FOR(i,0,N) fscanf(fin,"%d",&g[i]);
        fprintf(fout,"Case #%d: ",kase);
        fprintf(fout,"%llu\n",solve());
    }

	return 0;
}
