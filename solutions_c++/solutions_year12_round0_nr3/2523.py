#include <iostream>
#include <string>
using namespace std;

int m[2000001];

int main () {
  int i,j,t;
  int T;
  cin>>T;
  for(t=0;t<T;t++) {
    int a,b;
    cin>>a>>b;
    for(i=a;i<=b;i++) 
      m[i]=0;
    int y=0,x,digits=0, last, first;
    for(x=1;x<=a;x*=10)
      digits++;
    for(i=a;i<b;i++) {
      int k,n;
      for(j=1,k=1;j<digits;j++) {
	k*=10;
	last = i%k;
	first = i/k;
	n = last*(x/k)+first;
	if((i<n)&&(n<=b)&&(!m[n])) {
	  y++;
	  m[n]=1;
	}
      }
      for(j=1,k=1;j<digits;j++) {
	k*=10;
	int last = i%k;
	int first = i/k;
	n = last*(x/k)+first;
	if(n<=b)
	  m[n]=0;
      }
    }
    cout<<"Case #"<<t+1<<": "<<y<<"\n";
  }
  return 0;
}
