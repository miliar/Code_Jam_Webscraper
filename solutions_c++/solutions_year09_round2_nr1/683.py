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

vector<string> v;

double f(string t){
    VI a,c;
    int n=t.length();
    int x=0;
    int ok2=0;
    F(0,n,i){
        if(t[i]=='('){
            x++;
            if(x<=2) a.pb(i);                
        }
        if(t[i]==')'){
            x--;
            if(x<2) c.pb(i);
            ok2=1;
        }
    }
    string t2=t; t2[a[0]]=' ';
    
    double p; string ft;
    
    if (a.size()==1){
        t2[c[0]]=' ';
        ss in(t2);
        in>>p;
        return p;
    }
    ss in(t2);
    in>>p; in>>ft;
    
    int nf=v.size();
    bool ok=0;
    F(0,nf,i) if(v[i]==ft) ok=1;
    if(ok){
        return p*f(t.substr(a[1],c[0]-a[1]+1));
    }
    return p*f( t.substr(a[2],c[1]-a[2]+1) );
    
};


int main(){
    int nc,nl,na;
    string s;
    getline(cin,s);
    sscanf(s.c_str(),"%d",&nc);
    for(int caso=0;caso<nc;caso++){
        getline(cin,s);
        sscanf(s.c_str(),"%d",&nl);
        string t;
        for(int i=0;i<nl;i++){
            getline(cin,s);
            t+=s;
        }
        getline(cin,s);
        sscanf(s.c_str(),"%d",&na);
        cout<<"Case #"<<caso+1<<":"<<endl;
        for(int j=0;j<na;j++){
            getline(cin,s);
            stringstream in(s);
            int nf;
            in>>s;in>>nf;
            v.clear();
            for(int k=0;k<nf;k++){
                in>>s;
                v.push_back(s);
            }
            //cout<<v.size()<<endl;
            //cout<<t<<endl;
            printf("%.7lf",f(t));
            cout<<endl;
        }
    }
}
