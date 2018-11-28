#include <vector>
#include <list>
#include <map>
#include <set>
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
typedef vector<int> vi;
typedef vector<string> vs;
typedef stringstream sst;
#define fri(a,i) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fr(i,n) for(int i=0; i<(int)(n); i++)
#define zer(a) memset((a),0,sizeof(a));
#define all(a) (a).begin(), (a).end()
#define pb push_back

int a[10001][2];
int M;
int b[10001],c[10001];
int d[10001];

int f(int k, int v){
   if(a[k][v]!=-1) return -1;
   int& ret=a[k][v];
   if(k>(M-1)/2)
      if(d[k]==v) return ret=0;
	  else return ret=INT_MAX;
   if(d[k]==v) return ret=0;
   if(v==1){
   	int left=f(2*k,1);
   	int right=f(2*k+1,1);
   	int and_ret=(left!=INT_MAX&&right!=INT_MAX)?left+right:INT_MAX;
   	int or_ret=min(left,right);
    if(!c[k]){
	  if(b[k]) return ret=and_ret;
	  else return ret=or_ret;
    }else{
    	 if(b[k]) return min(and_ret, or_ret==INT_MAX?INT_MAX:1+or_ret);
 		 else return ret=min(or_ret,and_ret==INT_MAX?INT_MAX:1+and_ret);
    }
   }else{
   	int left=f(2*k,0);
   	int right=f(2*k+1,0);
   	int or_ret=(left!=INT_MAX&&right!=INT_MAX)?left+right:INT_MAX;
   	int and_ret=min(left,right);
    if(!c[k]){
	  if(b[k]) return ret=and_ret;
	  else return ret=or_ret;
    }else{
    	 if(b[k]) return min(and_ret, or_ret==INT_MAX?INT_MAX:1+or_ret);
 		 else return ret=min(or_ret,and_ret==INT_MAX?INT_MAX:1+and_ret);
    }
   }
}

int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
		int V;
		cin>>M>>V;
		for(int k=1; k<=M; k++)
		  for(int v=0; v<2; v++)
		    a[k][v]=-1;
		for(int i=1; i<=(M-1)/2; i++)
		  cin>>b[i]>>c[i];
		for(int i=(M-1)/2+1; i<=M; i++)
		  cin>>d[i];
		for(int i=(M-1)/2; i>=1; i--)
		  if(b[i]) d[i]=d[2*i]&&d[2*i+1];
		  else d[i]=d[2*i]||d[2*i+1];
		int ret=f(1,V);  
		//for(int i=1; i<=M; i++)
		//  for(int v=0; v<2; v++)
		//    cout<<i<<" "<<v<<" "<<a[i][v]<<endl;
		sst ss;
		ss<<ret;
	    cout<<"Case #"<<l<<": "<<(ret==INT_MAX?"IMPOSSIBLE":ss.str())<<endl;
	}
}
