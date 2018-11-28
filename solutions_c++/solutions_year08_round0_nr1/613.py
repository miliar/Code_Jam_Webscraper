#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
using namespace std;
int main(){
  int N,S,Q,c;
  string n;
  pair<string, int> e[150];
  cin>>N;
  c=1;
  while(N--){
    int t,s,x;
    t=0;
    s=0;
    cin>>S;
    getline(cin,n);
    for(int i=0; i<S; i++){
      getline(cin,n);
      e[i]=make_pair(n,0);  
    }
    cin>>Q;
    getline(cin,n);
    while(Q--){
      getline(cin,n);
      for(int i=0; i<S;i++){
	if(e[i].first==n && e[i].second==0){
	  e[i].second=1;
	  t++;
	  t=t%S;
	  x=i;
	}
      }
      if(t==0){
	s++;
	for(int i=0; i<S; i++){
	  if(i!=x)
	    e[i].second=0;
	}
	t++;
      }
    }
    cout<<"Case #"<<c++<<": "<<s<<endl;
  }
}
