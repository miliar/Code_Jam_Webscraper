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
#include <queue>
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
#define FR(i,a,b) for(long longi=(a);i<(b);++i)//[a,b)
#define FOR(i,n) FR(i,0,n)//[0,n)
#define FORALL(i,v) FOR(i,(int)v.size())//[0,v.size()) 
#define FORSZ(i,a,v) FR(i,a,SZ(v))//[a,v.size())
#define FRE(i,a,b) for(long longi=(a);i<=(b);++i)//[a,b]
#define FORE(i,n) FRE(i,1,n)//[1,n]
#define FOREACH(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i)
//反向遍历  
#define RF(i,a,b) for(long longi=(a)-1;i>=(b);--i)//[b,a)
#define ROF(i,n) RF(i,n,0)//[0,n)
#define RFE(i,a,b) for(long longi=(a);i>=(b);--i)//[b,a]
#define ROFE(i,n) RFE(i,1,0)//[1,n]
#define ROFALL(i,v) ROF(i,(int)v.size())//[0,v.size()) 
#define ROFSZ(i,a,v) RF(i,SZ(v),a)//[a,v.size())
#define ROFEACH(i,v) for(typeof(v.rend())i=v.rbegin();i!=v.rend();++i)
const double Pi=acos(-1.0);
const double eps=1e-11;
typedef pair<int,int> pi;

long long T,cs,R,k,N;
long long recystart;
long long  G[1500],bit[1500];
int main() 
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
    cin>>T;
    cs=0;
    while(++cs<=T){
        cin>>R>>k>>N;
        for(long long i=0;i<N;i++)
            cin>>G[i];
        queue<int> q,qb;            
        for(long long i=0;i<N;i++)
            q.push(i);
        CL(bit,0);
        long long tot;
        vector<int> rstart,rnum;
        while(1){
            tot=0;
            long long start=q.front();
            if(bit[start]){
                for(long long i=0;i<rstart.size();i++){
                    if(rstart[i]==start){
                        recystart=i;
                        break;
                    }
                }
                break;
            }
            while(!q.empty()&&tot+G[q.front()]<=k){
                tot+=G[q.front()];
                qb.push(q.front());
                q.pop();
            }
            while(!qb.empty()){
                q.push(qb.front());
                qb.pop();
            }
            bit[start]=tot;
            rstart.push_back(start);
            rnum.push_back(tot);
            
        }
        long long res=0;
        if(R<=rstart.size()){
            for(long long i=0;i<R;i++)
                res+=rnum[i];
        }
        else{
             for(long long i=0;i<rnum.size();i++)
                res+=rnum[i];
            long long recysize=0,recytot=0;
            for(long long i=recystart;i<rnum.size();i++){
                recytot+=rnum[i];
                recysize++;
            }
            R-=rstart.size();
            res+=R/recysize*recytot;
            R%=recysize;
            for(long long i=0;i<R;i++)
                res+=rnum[recystart+i];
        }
        cout<<"Case #"<<cs<<": "<<res<<endl;
    }
	return 0;	
}
