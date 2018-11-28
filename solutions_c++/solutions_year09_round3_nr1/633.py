#include <cstdio>
#include <cmath>
#include <map>
#include <algorithm>
#include <iostream>
#include <queue> 
#include <ctime> 
#include <sstream> 
#include <vector> 
#define FOR(i,j,n) for (int  i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define sz(a) (int)a.size()
#define foreach(i, c) for( __typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define PB push_back

using namespace std;
  string s;
  
  map<char,int>M;
  
  long long pww(long long a,long long ex){
  	long long res=1;
        FORN(i,ex)
              res*=a;
        return res;
  }
  
  long long conv(string v,int base){
    long long res=0;
    
   	 FORN(i,sz(v))
         	res+=(M[v[i]])*pww(base,sz(v)-i-1);
                
  return res;
  } 
  

int main(int a__,char **rr){

    int T;
    cin>>T;
    
    FORN(_case,T){
	cin>>s;
        M.clear();
        M[s[0]]=1;
       
        
        int nex=0;
        
	FOR(i,1,sz(s)){
        	if (M.count(s[i])) continue;
                M[s[i]]=nex;
                if (nex==0)
                      nex=2;
                else nex++;
        }
        
        int mx=0;
        FORN(i,sz(s))
            mx=max(mx,M[s[i]]);
           
        
        
        printf("Case #%d: ",_case+1);
        
        cout<<conv(s,mx+1)<<endl;
    }

}

