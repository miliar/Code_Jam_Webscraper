#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <memory.h>

#define oo 1000000005
#define eps 1e-11

#define REP(i,n) for(int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a), _b = (b); i < _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i > _b; i--)
#define RESET(c,x) memset (c, x, sizeof (c))

#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long ll;
using namespace std;

int ntest;
string s[10005];
string l[105];
bool f[10005][26];
int c,mx;
vector<int> vt;
int r[10005];
bool solve(int t, string str, int o){   
    if(vt.size()==1)   return true;         
    int temp = str[o] -'a';
    bool flag=false;
    
    REP( i,vt.size() )        
        if( f[ vt[i] ][temp] ){ flag= true; break; }    
    
    if(!flag) return false;    
    if(!f[t][temp]){        
        c++;
        vector<int> tmp;
        REP(i,vt.size() )
            if( !f[ vt[i] ][temp] ) tmp.PB(vt[i] );
        vt=tmp;      
        if(vt.size()==1){          
            return true;
        }        
    }
    else{                
        vector<int> tmp;               
        REP(i,vt.size() ){            
            if( f[ vt[i] ][temp] ) {
                bool check = true;
                REP(j,s[t].length()){
                    if( s[t][j]-'a'==temp && s[vt[i]][j]-'a'!=temp) check =false;
                    if( s[t][j]-'a'!=temp && s[vt[i]][j]-'a'==temp) check =false;
                }
                if(check) tmp.PB(vt[i] ); 
            }
        }
        vt=tmp;                
        if(vt.size()==1){       
            return true;
        }
    }    
    return false;
}
int n,m;
int main () {
    freopen("B-small-attempt3.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&ntest);
    REP(t,ntest){
        printf("Case #%d: ",t+1);        
        scanf("%d %d\n",&n,&m);
        REP(i,n) getline(cin,s[i]);
        REP(i,m) getline(cin,l[i]);
        
        memset(f,false,sizeof f);
        REP(i,n)
            REP(j,s[i].length()) f[i][s[i][j]-'a']=true;                  
            
        REP(t,m){
            mx=0;
            REP(i,n){                
                vt.clear();c=0;                
                REP(j,n)
                    if(s[j].length()==s[i].length()) vt.PB(j);
                REP(j,26){                  
                    if ( solve(i,l[t],j) ) break;                    
                }
                r[i]=c;
                mx=max(mx,c);                                      
            }            
            REP(i,n){                
                if(r[i]==mx){if(t) cout << " "; cout<< s[i]; break;}                
            }
        }                    
        cout << endl;
    }
    return 0;
}
