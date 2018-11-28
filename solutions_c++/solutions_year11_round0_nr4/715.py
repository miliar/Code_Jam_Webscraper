#include <iostream>
#include <algorithm>

#define N 1000

using namespace std;
int main(){
  int case_num, i,j, num, buf;
  double answer;
  cin >> case_num;
  for(j=0; j<case_num ; j++){
    answer =0.0;
    cin >> num;
    for(i=0;i<num; i++){
      cin >> buf;
      if(buf!=i+1)answer+=1;
    }
    cout <<endl<< "Case #" << j+1 << ": ";
    //    cout << setprecision(6);
    cout.precision(6);
    cout.setf(ios::fixed);
    cout << answer;
  }//one case
    cout << endl;
    return 0;
}
