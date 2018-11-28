
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int a[501][501];
long long b[501][501];
long long sum(int x1,int y1,int x2,int y2){
  return b[x2][y2]-b[x2][y1-1]-b[x1-1][y2]+b[x1-1][y1-1];
}
bool ok(int x, int y,int s){
  //  cout << x <<" "<< y << " " << s<<" ";
  double dist = (double)s/2-0.5;
  long double bal = 0;
  bal+=sum(x,y+1,x,y+s-2)*dist;
  //  cout << "dist = "<< dist<<" bal = " <<sum(x,y+1,x,y+s-2)*dist <<endl;
  dist-=1;
  for (int i = x+1;i<x+s-1;++i){
    bal+=sum(i,y,i,y+s-1)*dist;
    //    cout << "dist = "<< dist<<" bal = " <<sum(i,y,i,y+s-1)*dist <<endl;
    dist-=1;
  }
  bal+=sum(x+s-1,y+1,x+s-1,y+s-2)*dist;
  //  cout << "dist = "<< dist<<" sum = "<< sum(x+s-1,y+1,x+s-1,y+s-2) << " bal = " <<sum(x+s-1,y+1,x+s-1,y+s-2)*dist <<endl;
  if (bal>1e-6||bal<-1e-6)
    return false;
  dist = (double)s/2-0.5;
  bal = 0;
  bal+=sum(x+1,y,x+s-2,y)*dist;
  //  cout << "dist = "<< dist<<" bal = " <<sum(x+1,y,x+s-2,y)*dist <<endl;
  dist-=1;

  for (int j = y+1;j<y+s-1;++j){
    bal+=sum(x,j,x+s-1,j)*dist;
    //    cout << "dist = "<< dist<<" bal = " <<sum(x,j,x+s-1,j)*dist<<endl;
    dist-=1;
  }
  bal+=sum(x+1,y+s-1,x+s-2,y+s-1)*dist;
  //  cout << "dist = "<< dist<<" bal = " <<sum(x+1,y+s-1,x+s-2,y+s-1)*dist<<endl;
  if (bal>1e-6||bal<-1e-6)
    return false;

  return true;
}
int main(){
  int t;
  cin >> t;
  for (int kkk=1;kkk<=t;++kkk){
    cout << "Case #"<<kkk<<": ";
    int r,c,d;
    cin >> r >> c >>d;
    for (int i = 1; i <= r ; ++ i){
      string s;
      cin >> s;
      for (int j = 1; j <= c;++j)
	a[i][j] = s[j-1]-48+d;
    }
    memset (b,0,sizeof b);
    b[1][1]= a[1][1];
    for (int i= 2; i <= r;++i)
      b[i][1] = a[i][1]+b[i-1][1];
    for (int i= 2; i <= c;++i)
      b[1][i] = a[1][i]+b[1][i-1];
    for (int i = 2; i <= r; ++i)
      for (int j = 2 ; j <= c;++j){
	b[i][j] = b[i-1][j]+b[i][j-1]-b[i-1][j-1]+a[i][j];
      }
    int ans;
    ans= 0;
    for (int i = 3; i <=min(r,c);++i){
      //      cout << "i: "<<i<<endl;
      for (int j = 1; j+i-1<=r;++j)
	for (int k = 1; k+i-1<=c;++k){
	  if (ok(j,k,i)){
	    ans = i;
	    //    cout << i << " " << j << " " << k << endl;
	  }
	}
    }
    if (ans==0)
      cout << "IMPOSSIBLE\n"; else cout << ans<<endl;
  }
}
