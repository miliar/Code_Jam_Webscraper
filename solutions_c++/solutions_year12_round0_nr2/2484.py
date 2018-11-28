#include <iostream>
#include <string>
using namespace std;

int main () {
  int i,j,t;
  int T;
  cin>>T;
  for(t=0;t<T;t++) {
    int n,s,p,y=0;
    cin>>n>>s>>p;
    for(i=0;i<n;i++) {
      int total;
      cin>>total;
      if(p<=total/3)
	y++;
      else if(p==(total/3+1)){
	if((total%3)>0) 
	  y++;
	else if(s>0 && total>0) {
	  y++;
	  s--;
	}
      } else if(p==(total/3+2)){
	if(((total%3)==2) && (s>0)) {
	  y++;
	  s--;
	}
      }
    }
    cout<<"Case #"<<t+1<<": "<<y<<"\n";
  }
  return 0;
}
