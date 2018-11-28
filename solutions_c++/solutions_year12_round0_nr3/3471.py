#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
  ifstream ifs("C-small-attempt2.in");
  ofstream ofs("outputCs");
  int t,a,b;
  string s;
  ifs >> t;
  for(int i=0;i<t;i++){
    int ans=0;
    ifs >> a >> b;
    if(a >= 10 && a < 100){
      for(int n=a;n<=b;n++){
	int p,q,m;
	p = n/10;
	q = n%10;
	m = q*10+p;
	if(m >= a && m <= b && n != m){
	  if(i==1) cout << n << endl;
	  ans++;}
      }
    }
    else if(a >= 100){
      for(int n=a;n<=b;n++){
	int p1,p2,q1,q2,m1,m2;
	p1 = n/100;
	q1 = n%100;
	p2 = n/10;
	q2 = n%10;
	m1 = q1*10+p1;
	m2 = q2*100+p2;
	if(m1 >= a && m1 <= b && n != m1)
	  ans++;	
	if(m2 >= a && m2 <= b && n != m2)
	  ans++;	
      }
    }
    if(ans%2 == 1) cout << i+1 << endl;
    ofs << "Case #" << i+1 << ": " << ans/2 << endl; 
  }
  return 0;
}
      
