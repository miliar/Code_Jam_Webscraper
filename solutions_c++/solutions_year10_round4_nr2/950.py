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

int M[2048],Pr[2048],use[2048],um[2048],P;

int solve()
{
    int tot=((1<<P)-1),ret=0,cur,i,j,tx,sum=0,k;

    FOR(i,0,tot) um[i]=use[i]=0;
    FOR(i,0,P) M[i]=M[i];

    FOR(i,0,(1<<P))
    {
        cur=i/2;
        tx=i/2;
        sum=0;
        k=0;
        //DISP(i);
        //DISP(M[i]);
        for(j=P-1;j>=0 && k<P;--j,++k)
        {
            //cout << (k>=M[i]);
            //DISP(cur);
            if(k>=M[i]) use[cur]=1;
            sum+=(1<<j);
            tx/=2;
            cur=sum+tx;
        }

    }

    FOR(i,0,tot)
        if(use[i])
            ret+=Pr[i];
    //FOR(i,0,tot) printf("%d",use[i]);
    //printf("\n");
    return ret;

}


int main()
{
    int i,j,t,kase,n,k;
    int tot,cur;
    int ret;
    //FILE * fin=fopen("sample.txt","r");
    FILE * fin=fopen("B-small-attempt0.in","r");
    //FILE * fin=fopen("A-large.in","r");
    //FILE *fin=stdin;
    FILE * fout=fopen("out.txt","w");

    fscanf(fin,"%d",&t);
    for(kase=1;kase<=t;++kase)
    {
        fscanf(fin,"%d",&P);
        tot=(1<<P);
        FOR(i,0,tot)
            fscanf(fin,"%d",&M[i]);

        //cout << "*";
        cur=0;
        for(i=(1<<P)-2;i>=0;--i)
        {
            fscanf(fin,"%d",&Pr[i]);
        }

        //DISP(P);
        cout << "*";
        ret=solve();

        fprintf(fout,"Case #%d: %d\n",kase,ret);

    }

	return 0;
}
