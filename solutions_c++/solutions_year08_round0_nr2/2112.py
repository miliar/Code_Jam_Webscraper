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
    int n;
    string sta,stb;
    int ta,tb;
    int g,na,nb;
    
    cin>>n;
    F(0,n,z){
        cin>>g;
        cin>>na>>nb;
        vector< pair< pair<int,int> , int >  > v;
        F(0,na,i){
            cin>>sta>>stb;
            ta=((sta[0]-'0')*10 + sta[1]-'0')*60 +  (sta[3]-'0')*10 + sta[4]-'0';
            tb=((stb[0]-'0')*10 + stb[1]-'0')*60 +  (stb[3]-'0')*10 + stb[4]-'0';
            v.pb( make_pair(make_pair(tb,ta),0) );
        }
        F(0,nb,i){
            cin>>sta>>stb;
            ta=((sta[0]-'0')*10 + sta[1]-'0')*60 +  (sta[3]-'0')*10 + sta[4]-'0';
            tb=((stb[0]-'0')*10 + stb[1]-'0')*60 +  (stb[3]-'0')*10 + stb[4]-'0';
            v.pb( make_pair(make_pair(tb,ta),1) );
        }
        sort(all(v));
        int st=1;
        int t=0;
        int t1,k;
        int ra=0,rb=0;
        while(v.size()!=0){
            if(st){
                t=(v[0].first).first;//llegada
                k=v[0].second;//tipo
                st=0;
                v.erase(v.begin()+0);
                if(k) rb++;
                else ra++;
            }
            else{
                //siguiente a el primero
                t+=g;
                int sz=v.size();
                int ok=0;
                F(0,sz,i){
                    if( v[i].second != k && t<= (v[i].first).second ){
                        ok=1;
                        t=(v[i].first).first;
                        k=v[i].second;
                        v.erase(v.begin()+i);
                        break;
                    }
                }
                if(!ok) st=1;
            }
        }
        cout<<"Case #"<<z+1<<": "<<ra<<" "<<rb<<endl;
    }
}
