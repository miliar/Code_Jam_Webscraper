#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<cstdlib>
using namespace std;
#define REP(i,b,n) for(int i=b;i<n;i++)
#define rep(i,n)      REP(i,0,n)
#define pb push_back 
#define mp make_pair
#define ALL(C)   (C).begin(),(C).end()
template<class T> void vp(T &a,int p){rep(i,p)cout << a[i]<<" ";cout << endl;} 

typedef complex<double>P;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
const int N = 500;
const double eps = 1e-10;
int m[N][N];

double getsum1(int ii,int jj,int k,bool isx){
  double sum=0;
    REP(j,jj,jj+k){
  REP(i,ii,ii+k){

      if ((i == ii && j==jj) ||
	  (i == ii+k-1 && j == jj)||
	  (i == ii && j == jj+k-1)||
	  (i == ii+k-1 && j == jj+k-1))continue;
      double tmp=isx?j+0.5:i+0.5;
      //cout <<i <<" " << j <<" " <<  tmp <<" " << m[i][j] << endl;
      sum+=m[i][j]*tmp;
    }
  }
    //cout << sum << endl;
  return sum;
}

double getsum2(int ii,int jj,int k,bool isx){
  double sum=0;
  REP(i,ii,ii+k){
    REP(j,jj,jj+k){
      if ((i == ii && j==jj) ||
	  (i ==ii+k-1 && j == jj)||
	  (i ==ii && j == jj+k-1)||
	  (i ==ii+k-1 && j==jj+k-1))continue;
      sum+=m[i][j];
    }
  }
  return sum;
}

bool isinrect(int y1,int y2,int x1,int x2,int y,int x){
  return x1 <= x && x <= x2 && y1 <= y && y <= y2;
}

bool isinrect_st(int y1,int y2,int x1,int x2,int y,int x){
  return x1 < x && x < x2 && y1 < y && y < y2;
}


bool isin(double i,double j,int k,double y,double x){
  double cy,cx;
  if (k%2 == 1){
    cy=(i+0.5 +i+k-0.5)/2;cx=(j+0.5 +j+k-0.5)/2;
  }else {
    cy=(i+i+k)/2;cx=(j+j+k)/2;
  }
  //if (i == 0 && j == 1 && k == 5)
  //cout << cy <<" " << y <<" " << cx <<" " << x << endl;
  return abs(cy-y) < eps && abs(cx-x) < eps;
  if (!isinrect(i,i+k,j,j+k,y,x))return false;
  return 
    !isinrect(i,i+1,j,j+1,y,x) &&
    !isinrect(i,i+1,j+k-1,j+k,y,x) &&
    !isinrect(i+k-1,i+k,j,j+1,y,x) &&
    !isinrect(i+k-1,i+k,j+k-1,j+k,y,x);
}

int solve(int r,int c){
  int ret=0;
  for(int k=3;k<=min(r,c);k++){
    for(int i=0;i+k<=r;i++){
      for(int j=0;j+k <= c;j++){
	double ue=getsum1(i,j,k,true);
	double sita=getsum2(i,j,k,true);
	double x=ue/sita;
	ue=getsum1(i,j,k,false);
	//sita=getsum2(i,j,k,false);
	double y=ue/sita;
	//cout << ue <<" " << sita <<" "<<ue/sita <<  endl;
	//cout << x <<" "<< y << endl;
	if (isin(i,j,k,y,x)){ret=k;break;}
      }
      if (ret==k)break;
    }
  }
  return ret;
}

main(){
  int te;
  cin>>te;
  rep(tc,te){
    int r,c,d;
    cin>>r>>c>>d;
    rep(i,r)rep(j,c)m[i][j]=d;
    rep(i,r){
      rep(j,c){
	char a;
	cin>>a;
	m[r-1-i][j]+=(a-'0');
      }
    }
    int ans=solve(r,c);
    cout <<"Case #" << tc+1  << ": " ;
    if (ans==0)cout <<"IMPOSSIBLE"<<endl;
    else cout << ans << endl;
  }
  return false;
}
