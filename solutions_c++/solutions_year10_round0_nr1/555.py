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
int m,n,x,y,z,ret; 
int main(){
	#ifdef _LOCAL_Q_
		freopen("A-large.in","r",stdin); 
		 freopen("A-large.txt","w",stdout);
	#else
		freopen("A-large.in","r",stdin); 
		freopen("A-large.out","w",stdout);
	#endif   
       scanf("%d",&x);int k;
       REP(testcase,x){ 
               scanf("%d%d",&n,&k); 
               int64 x=k+1;bool good=true;
               while(x&&n){
                       if(x%2!=0){
                                good=false;break;
                       }
                       x/=2;
                       n--;
               }
               if(n)good=false;
               if( good)
                       printf("Case #%d: ON\n",testcase+1);
               else
                       printf("Case #%d: OFF\n",testcase+1); 
 
       } 
	return 0;
}