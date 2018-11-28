#include <iostream>
#include <vector>
#include <set>
using namespace std;

typedef long long ll;

int main(){
  int N;
  cin>>N;
  for(int i=1; i<=N; i++){
    ll n,A,B,C,D,x,y,M;
    cin>>n>>A>>B>>C>>D>>x>>y>>M;
    vector<vector<ll> > cnt(3,3);
    set<pair<ll,ll> > se;
    for(int j=0; j<n; j++){
      if(se.find(make_pair(x,y))==se.end()){
	se.insert(make_pair(x,y));
	cnt[x%3][y%3]++;
  //cout<<x%3<<" "<<y%3<<endl;
      }
  //cout<<x<<" "<<y<<endl;
      x=(A*x+B)%M;
      y=(C*y+D)%M;
    }
    ll res6=0;
    for(int j=0; j<3; j++){
      for(int k=0; k<3; k++){
	for(int m=0; m<3; m++){
	  for(int n=0; n<3; n++){
	    if(j==m&&k==n){
	      ll hoge=cnt[j][k];
	      res6+=hoge*(hoge-1)*(hoge-2);
	      continue;
	    }
	    int p=(6-j-m)%3;
	    int q=(6-k-n)%3;
	    res6+=cnt[j][k]*cnt[m][n]*cnt[p][q];
	  }
	}
	//cout<<cnt[j][k]<<" ";
      }
      //cout<<endl;
    }
    cout<<"Case #"<<i<<": "<<(res6/6)<<endl;
  }
  return 0;
}
