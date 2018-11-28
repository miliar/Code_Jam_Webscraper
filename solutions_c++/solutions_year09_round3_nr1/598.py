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

int main(){
    int nc;
    cin>>nc;
    string s;
    F(0,nc,caso){
        cin>>s;
        set <char> st;
        FE(it,s) st.insert(*it);
        
        int n=s.length();
        int nv=st.size();
        string res(n,' ');
        F(0,n,i){
            if( s[i]==s[0] ) res[i]='1';
        }
        //cout<<"res1="<<res<<endl;
        //D(res);
        F(0,nv,v){
            if(v==1) continue;
            int pos=-1;
            F(0,n,i){
                if(res[i]==' '){
                    pos=i;
                    break;
                }
            }
            if(pos!=-1){
            F(0,n,i){
                if( s[i]==s[pos] ) res[i]=v+'0';
            }
            }
            //D(res);
        }
        //D(res);
        long long res1=0;
        long long p=1;
        if(nv==1) nv=2;
        R(0,n,i){
            res1+=(res[i]-'0')*p;
            p*=nv;
        }
        cout<<"Case #"<<caso+1<<": "<<res1<<endl;
    }
}
