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
    int cases;
    cin >> cases;
    int count=1;
    while (cases > 0)
    {
        int total,mov,p1,p2,pos,curr,ex;
        int dist[2]={1};
        int time[2]={0};
        int prev[2]={0,0};
        char bot;
        dist[0]=1;
        dist[1]=1;
        time[0]=0;
        time[1]=0;
        cin >> total;
        ex=0;
        REP(i,total)
        {
            cin >> bot >> mov;
            pos=(bot=='O') ? 0 : 1;
            curr=dist[pos];
            if(mov > curr)
                ex=(mov-curr)+1;
            else
                ex=(curr-mov)+1;
            dist[pos]=mov;
            time[pos]+=max(ex,prev[pos]+1);
            ex=max(ex,prev[pos]+1);
            if(pos==0)
            {
                prev[1]+=ex-prev[0];
                prev[0]=0;
            }
            else
            {
                prev[0]+=ex-prev[1];
                prev[1]=0;
            }
//                cout << ex <<" "<<mov<<" "<<curr<<" "<<time[0]<<","<<time[1]<<"--"<<prev[0]<<","<<prev[1]<<"--"<<endl;
        }
        printf("Case #%d: %d\n",count,max(time[0],time[1]));
        count++;
//        cout << max(time[0],time[1])<<endl;
        cases--;
    }
    return 0;
}
