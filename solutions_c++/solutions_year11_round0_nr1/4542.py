#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define SIZE(X) ((int)(X.size()))
typedef long long int64;
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
const double pi=acos(-1.0); 
const double eps=1e-11; 
template<class T> inline void getmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void getmax(T &a,T b){if(b>a) a=b;}
using namespace std;
int testCount;
int64 ini;
queue<pair<int, int >> que;
void init(){ 
}
void solve(){
	
}
void output(){
}
int main(){
	#ifdef _LOCAL_Q_
	freopen("d:\\A-large.in","r",stdin); 
        freopen("d:\\output.txt","w",stdout);
	#endif   
       scanf("%d",&testCount);int steps; char color; int pos;
       REP(testcase, testCount){ 
               scanf("%d ",&steps);
			   //init
			   int o = 1 , b = 1;
			   int time = 0;
			   int lasto = 0, lastb = 0;
			   int thiso = 0, thisb = 0; 
			   REP(i, steps)
			   { 
				   scanf("%c %d ",  &color, &pos);  
				   if(color == 'O')
				   {   
					   thiso = 1; 
					   int need = abs(o - pos) ;
					   if(need > lastb)
					   {
						   thiso += (need - lastb);
					   } 
					   lastb = 0;
					   o=pos;
					   lasto += thiso;
					   time += thiso;
				   }
				   else
				   {   
					   thisb = 1;
					   int need = abs(b - pos);
					   if(need > lasto)
					   {
						   thisb += (need - lasto); 
					   } 
					   lasto=0;
					   b=pos;
					   time += thisb;
					   lastb += thisb;
				   }
			   }
			   printf("Case #%d: %d\n", testcase+1, time);
       } 
	return 0;
}