#include <vector>
#include <list>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <deque>
#include <fstream>
#include <stack>
#include <bitset>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}
#define FI first
#define SE second
#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i)
#define REV(i,a,b) for(int i= (int )a ; i >= (int)b ; --i)
#define REP(i,n) FOR(i,0,n)
#define DEP(i,n) REV(i,n,0)
#define PB push_back
#define PP pop()
#define EM empty()
#define INF 1000000000
#define MAX(x,y) (x)>(y)?(x):(y)
#define PF push_front
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define V(x) vector< x >
#define Debug false
#define PRINT(x)        cout << #x << " " << x << endl
#define LET(x,a) 	    __typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define PRESENT(c,x) 	((c).find(x) != (c).end())
#define SZ(x) 		x.size()
#define CPRESENT(c,x) 	(find(c.begin(),c.end(),x) != (c).end())
#define D(N) 		int N
#define S(N)		scanf("%d",&N)
#define FASTIO          1
#define abs(x) x=((x)<0)?(-1)*(x):(x)

typedef pair<int,int>   PI;
typedef pair<int,PI>    TRI;
typedef V( int )        VI;
typedef V( PI )        VII;
typedef V( string )     VS;
typedef long long       LL;
typedef long double     LD;

/* FastIO, generally required these days ;) */


int main()
{
    int cases,number,value,pos1,pos2,pnext1,pnext2;
    long long int total,time;
    int count = 0;
    char OB;
    S(cases);
    while (count<cases)
    {
        total = 0;
        pos1 = 1;
        pos2  =1;
        pnext2 = 1;
        pnext1 = 1;
        S(number);
        bool s[number];
        int val[number];
        REP (i,number)
        {
            scanf (" %c %d",&OB,&value);
             if(OB == 'O')
               s[i] = false;
            else
                {s[i] = true;}
            val[i] = value;
        }
        REP (i,number)
        {
            if (s[i] == false)
                {pnext1 = val[i];
                break;}
        }
        REP (i,number)
        {
            if (s[i] == true)
               {
                pnext2 = val[i];
                break;
               }
        }
        REP (i,number)
        {

            if (s[i] == false)
               {
                   time = val[i]-pos1;
                    abs(time);
                   total  = time + total + 1;
                   pos1 = val[i];
                   int a = (pnext2-pos2);
                   abs(a);
                   if ((time+1) > a)
                            pos2 = pnext2;
                    else if ((pnext2-pos2) < 0)
                        pos2 = pos2 - time-1;
                    else
                        pos2 = pos2 + time + 1;
                   FOR (j,i+1,number)
                   {
                       if (s[j] == false)
                       {
                           pnext1 = val[j];
                           break;
                       }

                   }

               }
            else
               {
                   time = val[i]-pos2;
                   abs(time);
                   total  = time + total + 1;
                   pos2 = val[i];
                   int a = pnext1-pos1;
                   abs(a);
                   if ((time+1) > a)
                            pos1 = pnext1;
                    else if ((pnext1-pos1) < 0)
                        pos1 = pos1 - time-1;
                    else
                        pos1 = pos1 + time + 1;
                   FOR (j,i+1,number)
                   {
                       if (s[j] == true)
                       {
                           pnext2 = val[j];
                           break;
                       }

                   }

               }
            //printf("%d %d %d %d %lld %lld\n",pos1,pos2,pnext1,pnext2,time+1,total);

        }

        cout<<"Case #"<<count+1<<": "<<total<<"\n";
        count++;
    }

return 0;
}
