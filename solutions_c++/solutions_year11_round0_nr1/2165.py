
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <numeric>
#include <limits>
#include <iterator>
using namespace std;


const int INF=(1<<30)-1;
const int DIRX[]={-1, 0, 0, 1,-1,-1, 1, 1}, DIRY[]={ 0,-1, 1, 0,-1, 1,-1, 1};
const double ERR=1e-9, PI=(2*acos(0.0));


template<class T> inline T MIN(T a,T b) {return ((a<b)?(a):(b));}
template<class T> inline T MAX(T a,T b) {return ((b<a)?(a):(b));}
template<class T> inline T ABS(T a) {return ((a<(T)0)?(-a):(a));}
template<class T> inline void checkMIN(T& a,T b) {if(b<a) a=b;}
template<class T> inline void checkMAX(T& a,T b) {if(a<b) a=b;}
template<class T> T SQR(T x) {return (x*x);}
template<class T> T GCD(T a,T b) {if(!b) return a; else return GCD(b,a%b);}
template<class T> T FastPow(T Base,T Power)
{T Result=(T)1; while(Power>0) {if(Power&(T)1)Result*=Base; Power>>=1; Base*=Base;} return Result;}
inline int CompareDouble(double x,double y,double err=ERR) { double d=x-y; if(d>err) return 1; if(d<-err) return -1; return 0;}


#define rep(x,n)	for(x=0;x<(int)(n);x++)
#define Fori(x,a,b)	for(x=(a);x<=(b);x++)
#define Ford(x,a,b)	for(x=(a);x>=(b);x--)
#define Mem(X,byte)	memset((X),(byte),sizeof(X))
#define All(X)		(X).begin(),(X).end()
#define Size(X)		((int)(X).size())
#define Each(X,itr)	for( __typeof((X).begin()) itr=(X).begin(); itr!=(X).end(); itr++)
#define Contains(X,item)	((X).find(item) != (X).end())
#define Contains_n(X,item)	(find(ALL(X),(item)) != (X).end())
#define PB	push_back
#define MP	make_pair
#define fs	first
#define sc	second

typedef unsigned long long	ULL;
typedef long long		LL;
typedef stringstream	SS;
typedef vector<string>	VS;
typedef vector<LL>		VL;
typedef vector<int>		VI;
typedef pair<int,int>	Pii;

struct Robot
{
	int position, extra_time;
	
	Robot() { position=1; extra_time=0;}
	
	int process(int new_position)
	{
		int time = ABS( position - new_position ), ret;
		
		if( time <= extra_time ) ret = 0;
		else ret = time - extra_time;
		
		extra_time = 0;
		position = new_position;
		
		return ret;
	}
} ;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	
	int _kase,kase=0;
	int i,j,k,n,p,t,total;
	char color;
	
	scanf("%d",&_kase);
	
	while( kase++ < _kase )
	{
		vector<Robot> r(2);
		
		total = 0;
		
		scanf(" %d",&n);
		rep(k,n)
		{
			scanf(" %c %d",&color,&p);
			
			i = color%2;
			t = r[i].process(p) + 1;
			
			r[1-i].extra_time += t;
			total += t;
		}
		
		printf("Case #%d: %d\n",kase,total);
	}
	
	return 0;
}
