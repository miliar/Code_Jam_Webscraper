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
    int nc;
    cin>>nc;
    F(0,nc,t){
        int nm,no,n;
        char d[30][30]={};
        char op[30][30]={};
        /*memset(d,0,sizeof(d));
        memset(op,0,sizeof(op));*/
        string s;
        
        cin>>nm;
        F(0,nm,i){
            cin>>s;
            d[s[0]-'A'][s[1]-'A']=s[2];
            d[s[1]-'A'][s[0]-'A']=s[2];
        }
        cin>>no;
        F(0,no,i){
            cin>>s;
            op[s[0]-'A'][s[1]-'A']=1;
            op[s[1]-'A'][s[0]-'A']=1;
        }
        cin>>n;
        cin>>s;
        vector< char > v;
        
        F(0,n,i){
            char c=s[i];
            int sz=v.size();
            if( sz==0 ){
                v.pb(c);
                continue;
            }
            int ok=0;
            if(   d[ v[sz-1]-'A' ][ c-'A' ] != 0  ){
                char tt=v[sz-1];
                v.pop_back();
                v.pb( char( d[tt-'A'][ c-'A' ]) );
            }
            else{
                F(0,sz,j){
                    if( op[v[j]-'A'][c-'A'] ){
                        v.clear();
                        ok=1;
                    }
                }
                if(!ok) v.pb(c);
            }
            
        }
        cout<<"Case #"<<t+1<<": [";
        F(0,v.size(),i){
            if(i!= v.size()-1){
                cout<<v[i]<<", ";
            }
            else{
                cout<<v[i]<<"]"<<endl;
            }
        }
        if(v.size()==0) cout<<"]"<<endl;
        
    }
}
