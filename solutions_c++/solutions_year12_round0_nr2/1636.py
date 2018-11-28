#include <vector>
#include <iostream>


using namespace std;


int dancing(int S, int p,vector<int> &points){
  if(p==0) return points.size();
  int winners =0;
  int m = max(p,p*3-2);
  int m2 = max(p*3-4,p);
  for(int i = 0; i< points.size();++i){
    if(m<=points[i]){
      ++winners;
    }else if(S && m2<=points[i]){
      ++winners;
      --S;
    }
  }
  return winners;
}

int main() {
  int T;
  cin>>T>>ws;
  for(int t = 1 ;t<=T;++t) {
    int N,S,P,p;
    vector<int> points;
    cin >> N >> S>> P;
    while(N--){
      cin>>p;
      points.push_back(p);
    }
    cout << "Case #"<<t<<": "<<dancing(S,P,points)<<endl;
  }
}
