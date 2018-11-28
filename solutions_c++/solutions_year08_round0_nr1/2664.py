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

int dp[1001][1001];
VS vq;
int n;

int memo(int a, int b){
    if( b-a < 2 ) return 0;
    int &t=dp[a][b];
    if( t != -1 ) return t;
    set<string>  c;
    F(a,b,i) c.insert(vq[i]);
    int val;
    if( c.size()< n ) val=0;
    else val=1000000000;
    
    t=val;
    F(a+1,b,i){
        t=min(t, memo(a,i)+memo(i,b) + 1 );
    }
    return t;
}

int main(){
    int nc,q;
    string s;
    
    
    getline(cin,s);
    sscanf(s.c_str(),"%d",&nc);
    //D(nc);
    F(0,nc,z){
        
        VS v;

        getline(cin,s);
        sscanf(s.c_str(),"%d",&n);
        //D(n);
        
        F(0,n,i){
            getline(cin,s);
            v.push_back(s);
        }

        cin>>q;
        getline(cin,s);
        sscanf(s.c_str(),"%d",&q);
        //D(q);
        vq.clear();
        
        F(0,q,i){
            getline(cin,s);
            vq.pb(s);
        }
        
//        PV("nq",nq);
        memset(dp,-1,sizeof(dp));
        
        int mn=memo(0,q);
        cout<<"Case #"<<z+1<<": ";
        cout<<mn;
        cout<<endl;
    }
}



