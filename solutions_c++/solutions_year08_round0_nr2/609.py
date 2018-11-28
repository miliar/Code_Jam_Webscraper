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
  int sa[105];
  int ea[105];
  int sb[105];
  int eb[105];
  int N,NA,NB,T,c,a,b,ma,mb;
  char t;
  cin>>N;
  c=1;
  while(N--){
    cin>>T>>NA>>NB;
    for(int i=0; i<NA; i++){
      cin>>a>>t>>b;
      sa[i]=a*60+b;
      cin>>a>>t>>b;
      ea[i]=a*60+b;
    }
    for(int i=0; i<NB; i++){
      cin>>a>>t>>b;
      sb[i]=a*60+b;
      cin>>a>>t>>b;
      eb[i]=a*60+b;
    }
    ma=NA;
    mb=NB;
    if(NA&&NB){
      sort(sa,sa+NA);
      sort(sb,sb+NB);
      sort(ea,ea+NA);
      sort(eb,eb+NB);
      int j=0;
      for(int i=0; i<NA; i++){
	if(j<NB&&sa[i]-eb[j]>=T){
	  ma--;
	  j++;
	}
      }
      j=0;
      for(int i=0; i<NB; i++){
	if(j<NA&&sb[i]-ea[j]>=T){
	  mb--;
	  j++;
	}
      }
    }
    cout<<"Case #"<<c++<<": "<<ma<<" "<<mb<<endl;
  }
}
