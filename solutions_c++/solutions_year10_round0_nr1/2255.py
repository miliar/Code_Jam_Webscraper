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

int main()
{
    int i,j,t,kase,n,k;
    int tot,once;
    //FILE * fin=fopen("sample.txt","r");
    //FILE * fin=fopen("A-small-attempt1.in","r");
    FILE * fin=fopen("A-large.in","r");
    FILE * fout=fopen("out.txt","w");

    fscanf(fin,"%d",&t);
    for(kase=1;kase<=t;++kase)
    {
        fscanf(fin,"%d %d",&n,&k);
        tot=(1 << n);
        once=tot-1;
        //DISP(tot);
        //DISP(n);DISP(k);
        fprintf(fout,"Case #%d: ",kase);
        if(k%tot==once)
            fprintf(fout,"ON\n");
        else
            fprintf(fout,"OFF\n");
    }

	return 0;
}
