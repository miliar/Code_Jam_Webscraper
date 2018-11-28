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

string P;

int f(int ps){
    int n=P.length();
    P[ps]='0';
    //D(P);
    int pos=ps+1;
    int ct=0;
    while( pos<n && P[pos]!='0' ){
        ct++;
        pos++;
    }
    int pos3=ps-1;
    while( pos3>-1 && P[pos3]!='0' ){
        ct++;
        pos3--;
    }
    //cout<<"pos=  "<<ct<<endl;    
    return ct;
};

int main(){
    int nc;
    int p,q,t;
    cin>>nc;
    F(0,nc,caso){
        VI Q;
        
        cin>>p>>q;
        F(0,q,i){
            cin>>t; Q.pb(t-1);
        }
        
        int nl=Q.size();
        int mn=1000000000;
        sort(all(Q));
        do{
            string p1(p,'1');
            P=p1;
            int x=0;
            F(0,nl,i){
                x+=f(Q[i]);
                
            }
            mn=min(x,mn);
        
        }while(next_permutation(all(Q)));
        cout<<"Case #"<<caso+1<<": "<<mn<<endl;
    }
}
