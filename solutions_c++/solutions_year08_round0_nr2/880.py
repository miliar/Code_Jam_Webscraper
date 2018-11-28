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

int nab[101],nae[101];
int nbb[101],nbe[101];
int a[24*60],b[24*60];

int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
	   int T,NA,NB;
	   cin>>T>>NA>>NB;
	   zer(a); zer(b);
	   char c;
	   int h,m;
	   for(int i=0; i<NA; i++){
	      cin>>h>>c>>m;
		  nab[i]=h*60+m;
		  cin>>h>>c>>m;
		  nae[i]=h*60+m;
	   }
	   for(int i=0; i<NB; i++){
	      cin>>h>>c>>m;
		  nbb[i]=h*60+m;
		  cin>>h>>c>>m;
		  nbe[i]=h*60+m;
	   }
	   for(int i=0; i<NA-1; i++)
	     for(int j=0; j<NA-1-i; j++)
		   if(nab[j+1]<nab[j]) {swap(nab[j],nab[j+1]); swap(nae[j],nae[j+1]);}
	   for(int i=0; i<NB-1; i++)
	     for(int j=0; j<NB-1-i; j++)
		   if(nbb[j+1]<nbb[j]) {swap(nbb[j],nbb[j+1]); swap(nbe[j],nbe[j+1]);}
	   int reta=0, retb=0;
	   for(int t=0; t<24*60; t++){
	     for(int i=0; i<NA; i++)
		   if(nab[i]==t){
 		      if(a[t]>0){ for(int j=t; j<24*60; j++) a[j]--;}
			  else reta++;
			  for(int j=nae[i]+T; j<24*60; j++) b[j]++;
		   }
	     for(int i=0; i<NB; i++)
		   if(nbb[i]==t){
 		      if(b[t]>0){ for(int j=t; j<24*60; j++) b[j]--;}
			  else retb++;
			  for(int j=nbe[i]+T; j<24*60; j++) a[j]++;
		   }
	   }
	   cout<<"Case #"<<l<<": "<<reta<<" "<<retb<<endl;
	}
}
