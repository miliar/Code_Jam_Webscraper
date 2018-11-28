#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<deque>
#include<queue>
#include<complex>
#include<string>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<ctime>
using namespace std;

#define REP(i,a,n) for(int i = a ; i < n ; i++)
#define rep(i,n) REP(i,0,n)

typedef long long ll;

pair<int,int> in[100010];
double x[100010];
double y[100010];
vector<double> tx,ty,tr;
int n, w,h;
bool iCC(int idx , double cx , double cy , double cr){
  double dx = tx[idx] - cx;
  double dy = ty[idx] - cy;
  double d = sqrt(dx*dx + dy*dy);
  if(d > tr[idx] + cr + 0.0000001)return false;
  else return true;
}
void solve(){
  for(int i = 2 ; i < n ; i++){
    while(true){
      int cr = in[i].first * -1;
      double cx = random();
      while(cx > w){
        cx /= 10.0;
      }
      double cy = random();
      while(cy > h){
        cy /= 10.0;
      }
      bool f = true;
      for(int j = 0 ; j < i ; j++){
        if(iCC(j , cx , cy , cr)){
          f = false;
        }
      }
      if(f){
        x[in[i].second] = cx;
        y[in[i].second] = cy;
        tx.push_back(cx);
        ty.push_back(cy);
        tr.push_back(in[i].first*-1);
        break;
      }
    }
  }
}

int main(){
  srandom((unsigned int)time(NULL));
  int T;
  cin>>T;
  for(int t = 1 ; t <= T ; t++){
    tx.clear();
    ty.clear();
    tr.clear();
    cin>>n>>w>>h;
    rep(i,n){
      cin>>in[i].first;
      in[i].first *= -1;
      in[i].second = i;
    }
    sort(in,in+n);
    x[in[0].second] = 0;
    y[in[0].second] = 0;
    tx.push_back(0);
    ty.push_back(0);
    tr.push_back(in[0].first*-1);

    if(n >= 2){
      x[in[1].second] = w;
      y[in[1].second] = h;
      tx.push_back(w);
      ty.push_back(h);
      tr.push_back(in[1].first*-1);
    }
    solve();
    cout<<"Case #"<<t<<": ";
    rep(i,n){
      if(i)cout<<" ";
      printf("%.8f %.8f",x[i],y[i]);
    }
    cout<<endl;
  }
}
