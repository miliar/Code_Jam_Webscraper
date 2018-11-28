#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
  int T; cin >> T;
  
  for(int t=0; t < T; ++t){
    int A,B; cin >> A; cin >> B;
    
    double Ex = 2.0 + B; //Case 3
    
    vector<double> Pi;
    for(int i=0; i < A; ++i){
      double tmp; cin >> tmp;
      Pi.push_back(tmp);
    }
    
    for(int i=1; i < A; ++i)	//Pi everything is ok to i'th character
      Pi[i] *= Pi[i-1];
    
    
    //Case 1

    double tmpEx = Pi[A-1]*(double)(B - A + 1) + (1.0-Pi[A-1])*(double)(B-A+1 + B + 1);
    Ex = min(Ex, tmpEx);

    //Case 2
    
    for(int k=1; k < A; ++k){ //k backspace
      tmpEx = Pi[A-k-1]*(double)(2*k + B - A + 1) + (1.0-Pi[A-k-1])*(double)(2*k + B-A+1 + B + 1);
      Ex = min(Ex, tmpEx);
    }
    
    cout << "Case #" << t+1 <<": " << Ex << endl;
    
  }
  
  
  
  return 0;
}
