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
int m,n,x,y,z,ret,k;
vector<string> vec; 
bool mp[55][55]; 
bool use[55][55][9];
int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
bool B[2];
char A[]={'R','B'}; 
inline bool valid(int r,int c){
        if(r>=0&&c>=0&&r<n&&c<n&&vec[r][c]!='.')
                return true;
        return false;
}
void solve(){
        memset(mp,false,sizeof(mp)); 
      B[0]=B[1]=false;
        REP(i,n){//rotate
                int pos=n-1 ;
                string tmp="";
                while(pos>=0){
                        if(vec[i][pos ]!='.')tmp+=vec[i][pos];
                        pos--;
                }
                REP(k,tmp.size())vec[i][n-1-k]=tmp[k];
                for(int s=n-1-tmp.size();s>=0;s--)vec[i][s]='.';
        }   
        vector<string> v2,v3,v4;
        v2=vec;
        REP(i,n) 
                REP(k,n)
                        v2[i][k]=vec[k][i]; 
        REP(i,n){
                if(B[0]&&B[1])return;
                if(vec[i].find(string(k,'R'))!=-1||v2[i].find(string(k,'R'))!=-1)
                        B[0]=true;
                if(vec[i].find(string(k,'B'))!=-1||v2[i].find(string(k,'B'))!=-1)
                        B[1]=true;
        }

          if(B[0]&&B[1])return;
          REP(i,n){ if(B[0]&&B[1])return;
                int r=i,c=n-1;string tmp="";
                while(valid(r,c)){tmp+=vec[r][c];r-=1;c-=1;}
                if(tmp.find(string(k,'B'))!=-1)B[1]=true;
               if(tmp.find(string(k,'R'))!=-1)B[0]=true;
                if(B[0]&&B[1])return;
                tmp=""; r=i,c=n-1;
                while(valid(r,c)){tmp+=vec[r][c];r+=1;c-=1;}
                 if(tmp.find(string(k,'B'))!=-1)B[1]=true;
               if(tmp.find(string(k,'R'))!=-1)B[0]=true;
                if(B[0]&&B[1])return;
                tmp="";
                r=n-1,c=i;
                while(valid(r,c)){tmp+=vec[r][c];r-=1;c+=1;}
                 if(tmp.find(string(k,'B'))!=-1)B[1]=true;
               if(tmp.find(string(k,'R'))!=-1)B[0]=true;
                if(B[0]&&B[1])return;tmp="";
                r=n-1,c=i;
                while(valid(r,c)){tmp+=vec[r][c];r-=1;c-=1;}
                 if(tmp.find(string(k,'B'))!=-1)B[1]=true;
               if(tmp.find(string(k,'R'))!=-1)B[0]=true;
                if(B[0]&&B[1])return;
          }
}
void output(){
}
int main(){
	#ifdef _LOCAL_Q_
	freopen("d:\\input.txt","r",stdin);
        freopen("d:\\out.txt","w",stdout);
	#endif  
        int t;cin>>t;
        for(int testcase=1;testcase<=t;testcase++){
        cin>>n>>k;
        vec.clear();vec.resize(n);
        REP(i,n)cin>>vec[i];
	solve();  
          if(B[0]&&B[1]){
                cout<<"Case #"<<testcase<<": Both"<<endl;
          }else if(B[0]){
                cout<<"Case #"<<testcase<<": Red"<<endl;
          }else if(B[1]){
          cout<<"Case #"<<testcase<<": Blue"<<endl;
          }else{
                cout<<"Case #"<<testcase<<": Neither"<<endl;
          }
        }
	return 0;
}