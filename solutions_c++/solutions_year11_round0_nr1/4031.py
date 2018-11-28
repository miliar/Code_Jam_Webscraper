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

#ifndef FASTIO
char *ipos, *opos, InpFile[20000000], OutFile[20000000], DIP[20];
inline int input(int flag=0) {

   while(*ipos <= 32) ++ipos;
   if ( flag  ) return (*ipos++ - '0'); /* For getting Boolean Characters */
   int x=0, neg = 0;char c;
   while( true ) {
      c=*ipos++; if(c == '-') neg = 1;
      else {
	 if (c<=32) return neg?-x:x;
	 x=(x<<1)+(x<<3)+c-'0';
      }
   }
}
inline void output(int x,int flag) {
   int y,dig=0;
   while (x||!dig) { y=x/10;DIP[dig++]=x-((y << 3) + (y << 1))+'0';x=y;}
   while (dig--) *opos++=DIP[dig];
   *opos++= flag ? '\n' : ' ';

}
inline void InitFASTIO() {
   ipos = InpFile; opos = OutFile;
   fread_unlocked(InpFile,20000000,1,stdin);
}
inline void FlushFASTIO() {
   fwrite_unlocked(OutFile,opos-OutFile,1,stdout);
}
#endif

int main()
{
    int cases,number,value,pos1,pos2,posnext1,posnext2;
    long long int total,time;
    int count = 0;
    char OB;
    S(cases);
    while (count<cases)
    {
        total = 0;
        pos1 = 1;
        pos2  =1;
        posnext2 = 1;
        posnext1 = 1;
        S(number);
        bool series[number];
        int val[number];
        REP (i,number)
        {
            scanf (" %c %d",&OB,&value);
             if(OB == 'O')
               series[i] = false;
            else
                {series[i] = true;}
            val[i] = value;
        }
        REP (i,number)
        {
            if (series[i] == false)
                {posnext1 = val[i];
                break;}
        }
        REP (i,number)
        {
            if (series[i] == true)
               {
                posnext2 = val[i];
                break;
               }
        }
        REP (i,number)
        {

            if (series[i] == false)
               {
                   time = val[i]-pos1;
                    abs(time);
                   total  = time + total + 1;
                   pos1 = val[i];
                   int a = (posnext2-pos2);
                   abs(a);
                   if ((time+1) > a)
                            pos2 = posnext2;
                    else if ((posnext2-pos2) < 0)
                        pos2 = pos2 - time-1;
                    else
                        pos2 = pos2 + time + 1;
                   FOR (j,i+1,number)
                   {
                       if (series[j] == false)
                       {
                           posnext1 = val[j];
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
                   int a = posnext1-pos1;
                   abs(a);
                   if ((time+1) > a)
                            pos1 = posnext1;
                    else if ((posnext1-pos1) < 0)
                        pos1 = pos1 - time-1;
                    else
                        pos1 = pos1 + time + 1;
                   FOR (j,i+1,number)
                   {
                       if (series[j] == true)
                       {
                           posnext2 = val[j];
                           break;
                       }

                   }

               }
            //printf("%d %d %d %d %lld %lld\n",pos1,pos2,posnext1,posnext2,time+1,total);

        }

        cout<<"Case #"<<count+1<<": "<<total<<"\n";
        count++;
    }

return 0;
}
