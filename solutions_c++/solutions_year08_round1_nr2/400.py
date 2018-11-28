#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
#include <set>
#include <sstream>
#include <cstdlib>
#include <stack>
#define FOR(i,j,n) for (int i=j;i<n;++i)
#define FORI(i,j,n) for (int i=j;i<=n;++i)
#define FORN(i,n) FOR(i,0,n)
#define SZ size()
#define PB(a) push_back(a)
#define foreach(i, c) for( __typeof( (c).rbegin() ) i = (c).rbegin(); i != (c).rend(); ++i )
#define CPRESENT(container, element) (find(ALL(container),element) != container.end())
#define MIN(a,b) (a < b ? a : b)
#define MAX(a,b) (a > b ? a : b)
#define ALL(x) x.begin(), x.end()
#define INF 1<<30

using namespace std;

int T;
int num,cl,k,a,b;


int SAT[1010][1100];


bool ok(int k){
   vector<int> test(num,0);
   int pos=0;
   while (k){
      if (k&1){
	 test[pos]=1;
      }
      k>>=1;
      pos++;
   }
   FORN(i,cl){
      bool satis=0;
      FORN(j,num)
	    if (SAT[i][j]){
	        if (SAT[i][j]==2 && test[j]==1)satis=1;
		else if (SAT[i][j]==1 && test[j]==0)satis=1;
	    }
      if (!satis)return false;
   }
return true;
}

int count(int s){
int res=0;
while (s){
   if (s&1)res++;
   s>>=1;
}
return res;
}

void pr(int s){
FORN(i,num)
   if (s&(1<<i))cout<<" 1";
   else cout<<" 0";
}

int main(){
   cin>>T;
   FORN(c,T){
      memset(SAT,0,sizeof(SAT));
      cin>>num>>cl;
      FORN(i,cl){
	   cin>>k;
	   FORN(j,k){
	     cin>>a>>b;
	     SAT[i][a-1]=(b+1);
	   }
      }
      vector<int> Asig(num,0);
      FORN(i,num)Asig[i]=i;

       cout<<"Case #"<<c+1<<":";
      bool found=0;
      int Mmin=1000000;
      int res=0;
      FORN(i,1<<num){
	 if (ok(i)){
	 found=1;
	 if ((count(i))<Mmin){
	    Mmin=count(i);
	    res=i;
	 }
	 }
      }
      
      
      if (found)pr(res);
      else  cout<<" IMPOSSIBLE";
		    
	 cout<<endl;


   }
//   
    return 0;
}
