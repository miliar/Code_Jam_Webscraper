#include <vector>
#include <list>
#include <set>
#include <deque>
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
#include <ctime>
#include <cstring>
using namespace std;
#define dump(x) cerr <<  __LINE__ << " : "<< #x << "  =  " << (x) <<endl;
#define CL(a,x) memset(a,x,sizeof(a))
#define Pb push_back
#define Mp(A,B) make_pair(A,B)
#define SZ(v) ((int)(v).size())
#define LEN(X) ((int)X.length())
//遍历 
#define BEND(v) v.begin(),v.end()
#define FR(i,a,b) for(int i=(a);i<(b);++i)//[a,b)
#define FOR(i,n) FR(i,0,n)//[0,n)
#define FORALL(i,v) FOR(i,(int)v.size())//[0,v.size()) 
#define FORSZ(i,a,v) FR(i,a,SZ(v))//[a,v.size())
#define FRE(i,a,b) for(int i=(a);i<=(b);++i)//[a,b]
#define FORE(i,n) FRE(i,1,n)//[1,n]
#define FOREACH(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i)
//反向遍历  
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)//[b,a)
#define ROF(i,n) RF(i,n,0)//[0,n)
#define RFE(i,a,b) for(int i=(a);i>=(b);--i)//[b,a]
#define ROFE(i,n) RFE(i,1,0)//[1,n]
#define ROFALL(i,v) ROF(i,(int)v.size())//[0,v.size()) 
#define ROFSZ(i,a,v) RF(i,SZ(v),a)//[a,v.size())
#define ROFEACH(i,v) for(typeof(v.rend())i=v.rbegin();i!=v.rend();++i)
const double Pi=acos(-1.0);
const double eps=1e-11;
typedef pair<int,int> pi;
template <class T> void out(T A[],int n){for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template <class T> void out (vector<T> A,int n=-1){if(n==-1) n=A.size();for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
int main() 
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int onoff[20];
	int electric[20];
    int T,N,K,cs;
    cin>>T;
    cs=0;
    while(++cs<=T){
        cin>>N>>K;
        bool ok=true;
        for(int i=0;i<N;i++){
            if(K%2!=1){
                ok=false;
                break;
            }
            K/=2;
        }
        if(ok){
            printf("Case #%d: ON\n",cs);
        }
        else{
            printf("Case #%d: OFF\n",cs);
        }
    }
	return 0;	
}
