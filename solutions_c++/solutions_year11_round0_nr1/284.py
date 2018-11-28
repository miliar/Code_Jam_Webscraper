#include <iostream>
#include <vector>
#include <utility>
//#include "../print.hpp"

using namespace std;

int INF = 1000000;

int solve(vector<int > & o, vector<int> & b, vector<char>& turns){
  int poso = 0;
  int posb = 0;
  o.push_back(INF);
  b.push_back(INF);

  int pointert = 0;
  int pointero = 0;
  int pointerb = 0;
  int tick = 0;

  //  print(o);
  //  print(b);
  //print(turns);



  while(pointert < turns.size()){
    bool flag = false;
    tick++;
    //    cout << "time :" << tick <<endl;;
    if(o[pointero] > poso){
      poso++;
      //      cout << "o walked plus" <<endl;
    }else if(o[pointero] < poso){
      poso--;
      //      cout << "o walked minus" <<endl;
    }else if (o[pointero] == poso && turns[pointert] == 'O'){
      //      cout << "o pushed" <<endl;
      pointero++;
      pointert++;
      flag = true;
    }
    if(b[pointerb] > posb){
      //      cout << "b walked plus" <<endl;
      posb++;
    }else if(b[pointerb] < posb){
      posb--;
      //      cout << "b walked minus" <<endl;
    }else if (b[pointerb] == posb && turns[pointert] == 'B'){
      if(! flag){
	//	cout << "b pushed" <<endl;
	pointerb++;
	pointert++;
      }
    }
  }
  return tick;
}


int main(){
  int t;cin >> t;
  for(int i = 1;i<=t;i++){
    int n;cin >> n;
    vector<int > o, b;
    vector<char> turns(n);
    for(int j = 0;j < n;j++){
      char r;int p;cin >> r >> p;
      p--;
      turns[j] = r;
      if(r == 'O'){
	o.push_back(p);
      }else{
	b.push_back(p);
      }
    }

    int ans = solve(o, b, turns);
    cout << "Case #" << i << ": " << ans <<endl;
  }
  return 0;

}
