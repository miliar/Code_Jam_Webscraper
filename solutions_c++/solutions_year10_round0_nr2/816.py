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
#define DISP(x)     cout << #x << ": " << x << endl;

#define MAX 5

int num[MAX],N;

int gcd(int a,int b)
{
    if(b==0) return a;
    else return gcd(b,a%b);
}

int solve()
{
    int T=-1;
    int i,j;

    sort(num,num+N,greater<int>());
    FOR(i,0,N)
    {
        FOR(j,i+1,N)
        {
            if(T==-1)
            {
                T=num[i]-num[j];
            } else
            {
                T=gcd(T,num[i]-num[j]);
            }
        }
    }
    //DISP(T);

    return (T-(num[0]%T))%T;
}

int main()
{
    int i,j,t,kase;
    //FILE * fin=fopen("sample.txt","r");
    FILE * fin=fopen("B-small-attempt0.in","r");
    //FILE * fin=fopen("B-large.in","r");
    FILE * fout=fopen("out.txt","w");

    fscanf(fin,"%d",&t);
    for(kase=1;kase<=t;++kase)
    {
        fscanf(fin,"%d",&N);
        FOR(i,0,N) fscanf(fin,"%d",&num[i]);
        fprintf(fout,"Case #%d: ",kase);
        fprintf(fout,"%d\n",solve());
    }

	return 0;
}
