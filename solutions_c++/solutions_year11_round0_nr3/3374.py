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
#include <ctime> 
  
using namespace std; 
  
typedef vector<int> VI; 
typedef vector<string> VS; 
typedef long long LL; 
typedef pair<int,int> PII; 
typedef pair<string,string> PSS; 
 
#define pb push_back 
#define all(a) a.begin(), a.end() 
 
#define ss stringstream 
 
#define F(a,b,i) for(int i=a; i<b; ++i)   
#define FE(it,s) for (__typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)  
#define R(a,b,i) for(int i=b-1; i>=a; --i) 
  
/*  debug  */ 
#define D(x) cout << #x << " = "<< x <<endl; 
#define PV(label,x) cout<<label<<"=[ "; FE(it,x) cout<<*it<<" "; cout<<"]"<<endl; 
#define PM(label,x) cout<<label<<endl; FE(it,x){cout<<label<<"["<<it->first<<"]="<<it->second<<endl;} 

int main()
{
    int nc,n;
    cin>>nc;
    int v[15];
    F(0,nc,t){
        cin>>n;
        F(0,n,i){
            cin>>v[i];
        }
        int res=0;
        F(1,pow(2,n)-1,s){
            int s1,s2;
            s1=s2=0;
            int a1=0;
            F(0,n,bit){
                if( (s&1 << bit) ){
                    s1^=v[bit];
                    //cout<<1;
                    a1+=v[bit];
                }
                else{
                    s2^=v[bit];
                    //cout<<0;
                }
            }
            //cout<<endl;
            if(s1==s2){
                res=max(res,a1);
            }
        }
        if(res==0) cout<<"Case #"<<t+1<<": NO"<<endl;
        else cout<<"Case #"<<t+1<<": "<<res<<endl;
    }
    return 0;
}
