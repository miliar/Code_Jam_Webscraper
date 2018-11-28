#include<iostream>
#include<map>
using namespace std;
int main(){
  int T;
  cin >> T;
  for(int tc =1; tc<=T;++tc){
    int N;
    int ans = 0;
    map<int,int> wires;
    cin >> N;
    for(int i = 0; i < N; ++i){
      int A, B;
      cin>>A>>B;
      wires[A]=B;
      
    }
    for(map<int,int>::iterator itm = wires.begin();
	itm!=wires.end();++itm){
      for(map<int,int>::iterator itmm = itm;
	  itmm!=wires.end();
	  ++itmm){
	if( itmm->second < itm->second ){
	    ++ans;
	}
      }
    }
    printf("Case #%d: %d\n", tc, ans );
  }
  return 0;
}
