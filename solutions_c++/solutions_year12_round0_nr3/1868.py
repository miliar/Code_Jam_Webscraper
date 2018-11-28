#include<iostream>
#include<vector>
#include<set>

using namespace std;
int ipow(int a, int b){
  int w=1;
  while(b>0){
    if (b%2) w*=a;
    a*=a;
    b/=2;
  }
  return w;
}


int pert(int n, int q, int l){
  return n/ipow(10,q)+ipow(10,l-q)*(n%ipow(10,q));
}
  

int main(){
  int T, h;
  cin>>T;
  set<int> s=set<int>();
  for (int t=0;t<T;t++){
    int A,B;
    cin>>A>>B;
    int l=0;
    int x=0;
    while (A/ipow(10,l)>0) l++;
    for (int n=A;n<B;n++){
      s.clear();
      if (n/ipow(10,l)>0) l++;
      for (int i=1;i<l;i++){
	h=pert(n,i,l);
	if (h>n && h<=B) s.insert(h);
      }
      x+=s.size();
	  
    }
    cout<<"Case #"<<t+1<<": "<<x<<endl;
  }
  return 0;
}
