#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <cctype>
#include <assert.h>
#include <list>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace __gnu_cxx;
using namespace std;

#define MP(a,b) make_pair(a,b)
#define i64 long long
#define pb push_back
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define Rev(i,a,b) for(typeof(a) i=(a);i>=(b);i--)
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++)
#define CLR(a,x) memset(a,x,sizeof(a))
#define ALL(x) x.begin(),x.end()

/**********************************************************************************/
int t;
map<string,int> MA;
int mem[1111];
int tim;
int fin(string s){
 if (MA.count(s)) return MA[s];
 //cout << s <<  ' ' << MA.size() << endl;
 return MA[s]=tim++;;
}
vector<int> M[1011];
bool par[1111];
int doit(int x){
 int &ret=mem[x];
 if (ret>=0) return ret;
 ret=0;
 vector<int> V;
 For(i,0,M[x].size()){
   V.pb(doit(M[x][i]));
  }
  sort(ALL(V));
  reverse(ALL(V));
  
  For(i,0,V.size()){
	//cout << V[i] +i<< ' ';
    ret=max(ret,V[i]+i);
}
  ret=max(ret,(int)V.size()+1);
  //cout <<":" <<  x << ' '<< ret << endl;
  return ret; 
}
int n,k;
char buf[1000];
int main(){
   freopen("A.in","r",stdin);
   scanf("%d",&t);
   for(int cas=1;cas<=t;cas++){
   tim=0;
    MA.clear();
	scanf("%d",&n);
	CLR(par,0);
	For(i,0,n) M[i].clear();
	For(i,0,n){
	 scanf("%s",&buf);
	 string s=buf;
	 int cur=fin(s);
	 
	 scanf("%d",&k);
	 //cout << k <<endl;
	 For(j,0,k){
	  scanf("%s",buf);
	  string g=buf;
	// cout << g << endl;
	  if (g[0]>='a' && g[0]<='z') continue;
	  M[cur].pb(fin(g));
	  
	  par[fin(g)]=1;
	  //cout << cur << ' '<< fin(g) << ' '  << M[cur].size() << endl;
	 }
	}
	
		
	CLR(mem,-1);
	For(i,0,n)
	  if (!par[i]){
		printf("Case #%d: %d\n",cas,doit(i));
	  }
    
   }
return 0;
} 
