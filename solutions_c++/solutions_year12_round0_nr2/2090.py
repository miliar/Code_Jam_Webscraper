#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<complex>
#include<sstream>
#include<map>
#include<set>
#define DEBUG(x) cout<<"line"<<__LINE__<<":"<<#x" == "<<x<<endl
#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()
#define INF 1000000
using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<int,int> P;

int test = 0;
int n,p,s;
int ans = 0;
//////////////////////////////////////////////////////////////
int main(){
    int T;
    cin>>T;
    for(int i = 0 ; i< T; i++){
        cin>>n>>s>>p;
        ans = 0;
        int t[n];
            for(int j = 0;j<n;j++){
                cin>>t[j];
                if(s>=0){
                if(t[j]%3==0){
                    if((t[j]/3>=p&&t[j]!=0)||(t[j]/3>=p&&t[j]==0&&p==0)){
                        ans++;
                    }
                    else if((s>0&&((t[j]/3)+1)>=p)&&t[j]!=0){
                        s--;
                        ans++;
                    }
                }
                else if(t[j]%3==1){
                    if((t[j]+2)/3>=p){
                        ans++;
                    }
                    
                }
                else if(t[j]%3==2){
                    if((t[j]+1)/3>=p){
                        ans++;
                    }
                    else if(s>0&&((t[j]+4)/3)>=p){
                        ans++;
                        s--;
                    }
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
    return 0;
  
}

