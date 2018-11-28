#include <algorithm>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <stack>
#include <utility>
#include <queue>

using namespace std;

#define CLR(_x) memset((_x),0,sizeof(_x))
#define all(_x) _x.begin(),_x.end()
#define pb push_back
#define mp make_pair
#define px first
#define py second

typedef long long ll;
typedef pair <int,int> point;

int func(int x, int diff){
	
	int ret=0;
	for(int a=0; a<=10; a++)
	  for(int b=0; b<=10; b++)
	    for(int c=0; c<=10; c++)
	      if(a+b+c==x && abs(a-b)<=diff && abs(a-c)<=diff && abs(b-c)<=diff)
	        ret=max(ret,max(a,max(b,c)));
	return ret;
}

int main(){
	
 	freopen("blarge.in","r",stdin);	
	freopen("blarge.out","w",stdout);
	
	int T,cases=1;
	
	cin>>T;
	int a[501],b[501];
	while(T--){
	  int n,s,p;
	  cin>>n>>s>>p;
	  for(int i=0; i<n; i++) cin>>a[i],b[i]=func(a[i],2),a[i]=func(a[i],1);
	  
	  //for(int i=0; i<n; i++) cout<<b[i]<<" "<<a[i]<<endl;
	  
	  int ret=0;
	  bool vis[501]={0};
	  while(1){
	    bool devam=0;
	    for(int i=0; i<n; i++) if(b[i]>=p && a[i]<p && s>0 && !vis[i]){
		  ret++;
		  s--;
		  vis[i]=1;
		  devam=1;
		}
		if(!devam) break;
	  }
	  
	  for(int i=0; i<n; i++){
	    if(!vis[i] && b[i]>=p && s>0){
		  ret++;
		  vis[i]=1;
		  s--;
		}
		if(!vis[i] && a[i]>=p){
		  ret++;
		}
	  }
	  
	  cout<<"Case #"<<cases++<<": "<<ret<<endl;
	}
	
	return 0;
}
