#include<iostream>
using namespace std;

int t,n;

int abs(int a){
  if(a>0)return a;
  return -a;
}

void solve(){
  cin >> t;
  char c;
  int d;
  for(int i=0 ; i<t ; i++){
    cin >> n;
    int ox=1,ol=0,bx=1,bl=0,cost=0;
    for(int j=0 ; j<n ; j++){
      cin >> c >> d;
      if(c=='O'){
	if(abs(d-ox)>cost-ol)cost+=abs(d-ox)-(cost-ol);
	ox=d;
	ol=++cost;
      }
      if(c=='B'){
	if(abs(d-bx)>cost-bl)cost+=abs(d-bx)-(cost-bl);
	bx=d;
	bl=++cost;
      }
      //  cout << ol << " " <<  bl << " " << cost << endl;
    }
    cout << "Case #" << i+1 << ": " << cost << endl;
  }
}

int main(){
  solve();
  return 0;
}
