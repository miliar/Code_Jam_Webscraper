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
        int n,l,h,ip,flag,ok,op;
        vector<int> vv;
        cin >> n >> l >> h;
        ok=0;
        REP(i,n)
        {
            cin >> ip;
            vv.PB(ip);
        }
        for(int i=l;i<=h;i++)
        {
            flag=1;
            for(int j=0;j<vv.size();j++)
            {
                if(i%vv[j]==0 || vv[j]%i==0)
                {
                    continue;
                }else
                {
                    flag=0;
                    break;
                }
            }
            if(flag)
            {
                op=i;
                ok=1;
                break;
            }
        }
        printf("Case #%d: ",count);
        if(ok)
        {
            cout << op << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
        cases--;
        count++;
    }
    return 0;
}
