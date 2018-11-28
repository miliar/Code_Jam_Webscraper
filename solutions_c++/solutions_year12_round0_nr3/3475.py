#include <iostream>
#include <sstream>
using namespace std;


string convert_int(int number){
  stringstream ss;
  ss << number;
  return ss.str();
}

int main(){
  int T;
  cin >> T;

  for (int proba = 0; proba < T; proba++){
    int A,B;
    cin >> A >> B;
    int res = 0;
    for (int a = A;a <=B; a++){
      for (int b = a+1; b<=B; b++){
        string converted_a = convert_int(a);
        string converted_b = convert_int(b);

        if (converted_a.length() == converted_b.length()){
          converted_b = converted_b + converted_b;
          int found = converted_b.find(converted_a);
          if (found != string::npos)
            res++;
        }
      }
    }
    cout << "Case #" << proba+1 << ": " << res << endl;
  }
}
