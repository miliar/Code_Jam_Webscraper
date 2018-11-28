#include <iostream>
#include <vector>
using namespace std;

int main(){
  int T;
  cin >> T;
  for (int i=0; i<T; i++){
    int N,S,p;
    cin >> N >> S >> p;
    vector<int> points;
    for (int j=0; j<N; j++){
      int dummy;
      cin >> dummy;
      points.push_back(dummy);
    }

    int minimum_without_suprise = 3*p - 2;
    int minimum_with_suprise = 3*p - 4;
    int googlers = 0;
    for (int j=0; j<N; j++){
      if (points[j] >= minimum_without_suprise){
        googlers++;
      } else if (S > 0 && points[j] >= minimum_with_suprise){
        if (p != 1) {
          --S;
          googlers++;
        }
      }
    }
    cout << "Case #" << i+1 << ": " << googlers << endl;
  }
}
