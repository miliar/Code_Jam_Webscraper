/* Jai Gupta */
#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <deque>
#include <bitset>
#include <cmath>
#include <functional>
#include <set>

using namespace std;

#define INT_MAX 2147483647
#define INT_MIN -2147483648
#define MAX(a,b)   (((a)>(b))?(a):(b))
#define MIN(a,b)   (((a)<(b))?(a):(b))
#define CMAX(a,b)  if((a)<(b)) a=b
#define CMIN(a,b)  if((a)>(b)) a=b
#define FOR(i,a,b)   for(i=a; i<b; i++)
#define REVI(i,a,b)  for(int i= a ; i >= b ; --i)
#define LET(x,a)     __typeof(a) x(a)
#define IFOR(i,a,b)  for(LET(i,a);i!=(b);++i)
#define DFOR(i,a,b)  for(LET(i,a);i<(b);++i)
#define EACH(it,v)   IFOR(it,v.begin(),v.end())
#define SWAP(a,b,t)  t=a,a=b,b=t
#define REP(i,n)     for(int i=0; i<n; i++)
#define gint(t)      scanf("%d", &t);
#define pint(t)      printf("%d\n", t);
#define pb           push_back

#ifdef JAI_ARENA
#define debug(args...) {dbg,args; cerr<<endl;}
#define dline cerr<<endl
#else
#define debug(args...) {};
#endif

typedef long long int   ll;
typedef unsigned long long int ull;
typedef unsigned int    uint;
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector<vi>      vii;
typedef vector<pii>     vpii;

struct debugger
{
    template<typename T> debugger& operator , (const T& v)
	{
	    cerr<<v<<" ";
	    return *this;
	}
} dbg;


#define BUF 4096
char ibuf[BUF];
int ipt = BUF;
 
int readUInt() {
    while (ipt < BUF && ibuf[ipt] < '0') ipt++;
    if (ipt == BUF) {
	fread(ibuf, 1, BUF, stdin);
	ipt = 0;
	while (ipt < BUF && ibuf[ipt] < '0') ipt++;
    }
    int n = 0; char neg = 0;
    if(ipt !=0 && ibuf[ipt-1] == '-') neg = 1;
    while (ipt < BUF && ibuf[ipt] >= '0') n = (n*10)+(ibuf[ipt++]-'0');
    if (ipt == BUF) {
	fread(ibuf, 1, BUF, stdin);
	ipt = 0;
	while (ipt < BUF && ibuf[ipt] >= '0') n = (n*10)+(ibuf[ipt++]-'0');
    }
    return neg?-n:n;
}


/* memset(start*, byteVal, numBytes);
 *  memcpy(dst*, src*, numBytes);
 */
typedef struct node
{
    int prob;
    int time;
    int id;
} node;
bool operator<(const node &a, const node &b)
{
    int d = a.prob - b.prob;
    if(d<0) return false;
    if(d>0) return true;
    d = a.time - b.time;
    if(d<0) return false;
    if(d>0) return  true;
    return a.id < b.id;
}
node a[1005];
int main()
{
    int n, t; gint(t);
    REP(ti, t)
    {
	gint(n);
	REP(ni,n)
	{
	    gint(a[ni].time);
	    a[ni].id = ni;
	}
	REP(ni, n)
	{
	    gint(a[ni].prob);
	}
	sort(a, a+n);
	printf("Case #%d:", ti+1);
	REP(ni, n)
	{
	    printf(" %d", a[ni].id);
	}
	printf("\n");
    }
    return 0;
}
