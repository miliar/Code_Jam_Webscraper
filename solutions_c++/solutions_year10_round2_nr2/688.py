#include<iostream>
#include<utility>
#include<algorithm>
using namespace std;

int n,k,b,t;
pair<int, int> chicks[51];
bool possible[51];
int swaps[51];

bool pass[51][51];

bool chick_ok(int a){
  int dstA = b- chicks[a].first;
  return (dstA<=t*chicks[a].second);
}





int main(){
  int tst_cse;
  cin>>tst_cse;

  for(int tst=1; tst <=tst_cse; tst++){
  cin>>n>>k>>b>>t;
  for(int i=0; i<n; i++){
    //pair<int,int> tmp;
      int tmp;
      cin>>tmp;
    chicks[i].first = tmp;
  }
  for(int i=0; i<n; i++){ 
     int tmp;
     cin>>tmp;
     chicks[i].second=tmp;
  }

  int swaps =0;
  for(int i=n-1; i>=0 && k>0; i--){
    if(chick_ok(i)){
      k--;
    }else{
      swaps += k;
    }
  }
  if(k>0){
    cout<<"Case #"<<tst<<": "<<"IMPOSSIBLE"<<endl;
  }else{
    cout<<"Case #"<<tst<<": "<<swaps<<endl;
  }


}

}
