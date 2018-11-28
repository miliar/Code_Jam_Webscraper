#include <cstdio>
#include <iostream>
#include <set>

using namespace std;
int tens[10];

int digits(int x){
  int i=0;
  while(x){x/=10;i++;}
  return i;
}

#define rot(x,d,r) ((x)/tens[r]+((x)%tens[r])*tens[d-r]) 

int main(){
  int a,b,t,r,i,u,c,j,d;
  tens[0]=1;
  cin>>t;
  for(i=1;i<9;i++) tens[i]=tens[i-1]*10;
      for (u=0;u<t;u++){
	cin>>a>>b;
	c=0;
	for (i=a;i<=b;i++){
	    d=digits(i);
	    set<int> s;
	    for (r=1; r<d; r++) if((j=rot(i,d,r))>i) if(j<=b) 
						       s.insert(j);
	    c+=s.size();
	}
	cout<<"Case #"<<(u+1)<<": "<<c<<endl;
      }
  return 0;
}
