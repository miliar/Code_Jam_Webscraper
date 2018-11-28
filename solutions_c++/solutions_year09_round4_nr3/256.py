#include <iostream>
#include <algorithm>
using namespace std;
int n,k;

struct chart{
  int price[30];
  bool operator<(const chart b)const{
    for (int i = 0; i < k; ++i)
      if (price[i]!=b.price[i])
	return price[i]<b.price[i];
    return false;
  }
  
  bool cover(const chart b)const{
    bool pk = true;
    for (int i = 0; i < k; ++i)
      if (price[i]<=b.price[i])
	pk = false;
    return pk;
  }
  
}a[106];
//int m;

bool c[106][106],vx[106];
long my[106];

bool aug(long x) {
  if (vx[x])
    return false;
  vx[x] = true;
  for (int y = 0; y < n; ++y)
    if (c[x][y] && (!my[y] || aug(my[y]))) {
      my[y] = x;
      return true;
    }
  return false;
} 
int main(){
  int t;
  cin >> t;
  
  for (int cnas = 1; cnas<=t; ++cnas){
    cout << "Case #"<<cnas<<": ";
    cin >> n >> k;
    for (int i = 0; i<n; ++i){
      for (int j = 0; j < k; ++j)
	cin >> a[i].price[j];
    }    
    sort(a,a+n);
    //    for (int i = 0; i < n; ++i)
    //      cout << a[i].price[0]<<" "<< a[i].price[1]<<endl;
    
    memset(c,0,sizeof c);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j){
	if (a[i].cover(a[j])){
	  c[i][j] = true;
	  //	  cout << i <<" "<< j <<endl;
	  
	}	
      }
    
    //    int ans = 0;
    int f = 0;
    memset(my, 0, sizeof my);
    for (int i = 0; i < n; ++i) {
      memset(vx, 0, sizeof vx);
      if (aug(i)) ++f;
    }
    cout <<n-f <<endl;
    
    //    cout << n+m-f <<endl;
  }
}
