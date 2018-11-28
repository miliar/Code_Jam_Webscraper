//Template by Burbero
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <iomanip>
#include <limits>
#include <valarray>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <blitz/tinyvec.h>
#include <blitz/tinyvec-et.h>

using namespace std;
using namespace blitz;

typedef TinyVector<double,2> vec2;
typedef TinyVector<double,3> vec3;
typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ull;

const double infinity = numeric_limits<double>::infinity();

#define FOR(i,a,b) for(int i=a;i < b;++i)
#define REP(i,c) for(typeof(c.begin()) i = c.begin();i != c.end();++i)
#define BIT(i) (1LL << i)

int move(int a,int b,vi & in)
{
    if (a == b) return 0;
    int tmp = in[a];
    if (a < b)
        FOR (i,a,b) in[i]=in[i+1];
    else
        for (int i=a;i > b;--i) in[i]=in[i-1];
    in[b]=tmp;
    return abs(a-b);
}

void print(vi & in)
{
    FOR(i,0,in.size()) cerr << in[i] << " ";
    cerr << endl;
}

int solve(vi & in,int d = 0)
{
   // print(in);
  //  cout << d << endl;
    int N = in.size();
    bool isdiag=true;
    FOR(i,0,N) if (in[i] > i) isdiag=false;
    if(isdiag)return 0;
    if (d >= N-1) return INT_MAX-100000;
    vi candidates;
    FOR(i,d,N)
        if (in[i] <= d) candidates.push_back(i);
    int res = INT_MAX;
    REP(iter,candidates)
    {
        vi tmp = in;
        int m = move(*iter,d,tmp);
        int s = solve(tmp,d+1);
        if (m+s < res) res = m+s;
    }
    return res;
}


int main(int argc,char * argv[])
{
    int N;
    cin >> N;
    for (int i=1;i <=N;++i)
    {
        //Parse
        int S;
        cin >> S;
        cin.ignore(1);
        vi r;
        char buf[512];
        FOR(i,0,S)
        {
            cin.getline(buf,512);
            int j=0;
            FOR(k,0,S)
                if (buf[k] == '1') j=k;
            r.push_back(j);
        }
        //Solve
        cout << "Case #" << i << ": " << solve(r) << endl; //Solution here
    }
    return 0;
}

