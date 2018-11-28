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
vector<string> have;
vector<string> want;int best;
void solve(){
        for(int i=0;i<want.size();i++){ 
                int mi=count(want[i].begin(),want[i].end(),'/'); 
                if(want[i]=="/")continue;
                for(int t=0;t<have.size();t++){ 
                        if(have[t]==want[i]){//相同
                                mi=0;break;
                        }  
                        int pos=0;
                        while(pos<have[t].size() &&pos<want[i].size()&&have[t][pos]==want[i][pos]){
                                pos++;
                        }
                        if(pos==want[i].size()){//want 用完
                                if(pos==have[t].size()||have[t][pos]=='/'){
                                        mi=0;break;
                                }else
                                       getmin(mi,1);
                        }else{//还有want
                                int cnt;
                                if(pos==have[t].size()) {
                                         if(want[i][pos]=='/') {cnt=1;pos++;}
                                         else cnt=1;
                                }else{
                                        if(want[i][pos]=='/'){cnt=2;pos++;}
                                        else cnt=1;
                                }
                        while(pos<want[i].size()){
                                if(want[i][pos]=='/')cnt++;
                                pos++;
                        }
                        getmin(mi,cnt);
                        }
                }
                best+=mi;if(mi!=0)have.push_back(want[i]);
        }
} 
int main(){
	#ifdef _LOCAL_Q_
	freopen("d:\\input.txt","r",stdin);
          freopen("d:\\out.txt","w",stdout);
	#endif  
        cin>>testcase;
        for(int i=1;i<=testcase;i++){
                cin>>n>>m;
                have.clear();want.clear();string tmp;best=0;
                REP(k,n){ 
                        cin>>tmp;have.push_back(tmp);
                }
                REP(d,m){
                        cin>>tmp;want.push_back(tmp);
                }
                solve(); 
                 cout<<"Case #"<<i<<": "<<best<<endl;    
        }
	
	return 0;
}