/*! if g++ -O2 main.cpp; then ./a.out < test.in; fi
 */

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <cstdlib>



using namespace std;

class robot_status{
public:
  int pos;
  int time;
  robot_status(){
    pos = 1;
    time = 0;
  }

  int receive_order(int now, int button_pos){
    if(now - time >= abs(button_pos - pos)){
      time = now + 1;
    }
    else{
      time += abs(button_pos - pos) + 1;
    }
    pos = button_pos;
    return time;
  }

  void print(string s){
    cout << s << "\t" << time << "\t" << pos << endl;
  }
};

void solve(int x){
  int n;
  cin >> n;
  vector<char> r(n);
  vector<int>  p(n);
  for(int i = 0; i < n; ++i){
    cin >> r[i] >> p[i];
  }

  int now = 0;
  robot_status blue, orange;
  for(int i = 0; i < n; ++i){
    now = (r[i] == 'B' ? &blue : &orange)->receive_order(now, p[i]);

//     //debug
//     cout << i << "th order\tnow " << now << "\trobot " << r[i] << "\tbutton " << p[i] << endl;
//     blue.print("blue");
//     orange.print("orange");
  }

  cout << "Case #" << x << ": " << now << endl;
}

int main(int argc, char *argv[]){
  int n;
  cin >> n;

  for(int i = 0; i < n; ++i){
    solve(i + 1);
  }

  return 0;
}
