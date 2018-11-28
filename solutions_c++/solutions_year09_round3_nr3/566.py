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
  
int P,Q;
  vector<int> H;
  
  bool PP[10000];
  
  

  
  int eval(){
    memset(PP,1,sizeof PP);
    PP[0]=0;
    PP[P+1]=0;
    int res=0;
    FORN(i,Q){
      	PP[H[i]]=0;
        int h=H[i];
    	while (PP[++h])res++;
        h=H[i];
        while (PP[--h])res++;	
    }
  
    return res;
  }
  
  
int main(int a__,char **rr){

    int T;
    cin>>T;
    
    FORN(_case,T){
	cin>>P>>Q;
         H.clear();
        FORN(i,Q){
          int tmp;
            cin>>tmp;
            H.PB(tmp);
        }
        int minn=1<<30;
        do{
        	minn=min(minn,eval());
        }while(next_permutation(ALL(H)));
        
        printf("Case #%d: %d\n",_case+1,minn);
        
    }

}

