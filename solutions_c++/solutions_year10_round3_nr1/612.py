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
int m,n,x,y,z,ret,testcase; 
int start[2000];int end[2000]; 
void solve(){
        ret=0;
        for(int i=0;i<n;i++)
                for(int j=0;j<i;j++){ 
                                if(start[i]>start[j] &&end[i]<end[j])
                                        ret++;
                                else if(start[i]<start[j] &&end[i]>end[j])
                                        ret++;
                }
	
} 
int main(){
	#ifdef _LOCAL_Q_
	freopen("d:\\input.txt","r",stdin);
        freopen("d:\\output.txt","w",stdout);
	#endif  
        cin>>testcase;
        for(int i=1;i<=testcase;i++){
                cin>>n;
                REP(k,n){
                        cin>>start[k]>>end[k];
                }
                solve(); 
                 cout<<"Case #"<<i<<": "<<ret<<endl;    
        }
	
	return 0;
}