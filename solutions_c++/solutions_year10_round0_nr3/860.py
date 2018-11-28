#include <iostream>
using namespace std;
int g[1006];
struct node{
  int x,y,t;
}h[1006];
long v[1006],hh[1006];

int main(){
  int t;
  int o;
  
  cin >> t;
  o = t;
  
  while (t--){
    cout << "Case #"<<o-t <<": ";
    int r,k,n;
    cin >> r >> k >> n;
    for (int i = 0; i < n; ++i)
      cin >> g[i];
    int x,y;
    x = 0;
    y = 0;
    int t = g[0];
    while (t+g[y+1]<=k&& y+1<n){
      t+=g[y+1];
      ++y;
    }
    for (int i = 0; i < n; ++i){
      h[i].x = x;
      h[i].y = y;
      h[i].t = t;
      ++x;
      t-=g[i];
      while(t+g[(y+1)%n]<=k && y+1-x<n){
	t+=g[(y+1)%n];
	++y;
      }	
    }  
    int rr = 1;
    long long gg=h[0].t;
    int i= (h[0].y+1)%n;
    while (rr<r){
      ++rr;
      gg+=h[i].t;
      i = (h[i].y+1)%n;
    }
    cout << gg <<endl;
  }
}
