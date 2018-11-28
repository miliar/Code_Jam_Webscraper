#include <iostream>
#include <cstdlib>
using namespace std;
int main(){
  int T;cin >> T;
  for(int c=1;c<=T;++c){
    int N;cin >> N;
    char r;
    int p;
    int op=1, ot=0, bp=1, bt=0;
    for(int i=0;i<N;++i){
      cin>>r>>p;
      if(r=='O'){
        ot=max(bt+1,ot+std::abs(p-op)+1);
        op=p;
      }else{
        bt=max(ot+1,bt+std::abs(p-bp)+1);
        bp=p;
      }
    }
    cout << "Case #"<<c<<": "<<max(bt,ot)<< endl;
  }
}
