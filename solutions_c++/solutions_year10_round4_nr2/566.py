
/* Author :: Yash */
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

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i) 
#define REV(i,a,b) for(int i= (int )a ; i >= (int)b ; --i)
#define REP(i,n) FOR(i,0,n)
#define DEP(i,n) REV(i,n,0)
#define PB push_back
#define PP pop()
#define EM empty()
#define INF 1000000000
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

typedef pair<int,int>   PI;
typedef pair<int,PI>    TRI;
typedef V( int )        VI;
typedef V( PI  )        VII;
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

/* Main Code Starts from here */

int P;
int M[2000];

bool check(int x,int y) {
   FOR(i,x,y+1) if(!M[i]) return true;
   return false;
}
void dec(int x,int y) {
   FOR(i,x,y+1) M[i]--;
}
void inc(int x,int y) {
   FOR(i,x,y+1) M[i]++;
}
map<PI,int> Value;
int memo[2000][2000];
int solve(int x,int y) {

   if(x >= y)  return 0; int diff = (y-x)/2;
   if(check(x,y)) {
      int ans = Value[PI(x,y)] + solve(x,x+diff) + solve(x+diff+1,y);
      memo[x][y] = ans; 
   }
   else {
      int tmp  = Value[PI(x,y)] + solve(x,x+diff) + solve(x+diff+1,y); dec(x,y);
      int tmp1 = solve(x,x+diff) + solve(x+diff+1,y); inc(x,y);
      return (memo[x][y] = min(tmp,tmp1));  
   }
   
}
int main() {

   	int kases; scanf("%d",&kases);
	REP(l1,kases) {

	   	Value.clear();memset(memo, -1, sizeof memo);
		scanf("%d",&P);
		REP(i,(1 << P)) {
		   scanf("%d",&M[i]);
		   assert(M[i] >= 0 && M[i] <= P);
		}
		int t = P - 1, y = 1;
		REP(i,P) {
		   int start = 0;
		   REP(j,(1 << t)) {
		        int x; cin >> x;
			Value[PI(start,start+y)] = x;
			start += y + 1;
		   }
		   y = y*2 + 1;
		   --t;
		}
		int ans = solve(0,(1 << P)-1);
		printf("Case #%d: %d\n",l1+1,ans);
	}
	return 0;
}
