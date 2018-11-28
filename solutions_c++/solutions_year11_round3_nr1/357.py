#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<=(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	

int main()
{
    int cases,count;
    cin >> cases;
    count=1;
    while(cases>0)
    {
        vector< vector<char> > b;
        int c1,c2;
        int r,c;
        char ip;
        cin >> r >> c;
        REP(i,r)
        {
            vector<char> a;
            REP(j,c)
            {
                cin >> ip;        
                a.PB(ip);
            }
            b.PB(a);
        }
        c1=0;
        c2=0;
        int flag=1;
        REP(i,r)
        {
            REP(j,c)
            {
                if(b[i][j]=='#')
                {
                    if(i == r-1 || j==c-1)
                    {
                        flag=0;
                        break;
                    }
                    if(b[i+1][j]=='#' && b[i][j+1]=='#' && b[i+1][j+1]=='#')
                    {
                             b[i][j]='/';
                             b[i+1][j]='\\';
                             b[i][j+1]='\\';
                             b[i+1][j+1]='/';
                    }
                    else
                    {
                        flag=0;
                        break;
                    }
                }
            }
        }
        printf("Case #%d:\n",count);
        if(flag)
        {
            REP(i,r)
            {
                REP(j,c)
                {
                    cout << b[i][j];
                }
                cout << endl;
            }
        }
        else
            cout << "Impossible" << endl;

        cases--;
        count++;
    }
    return 0;
}
