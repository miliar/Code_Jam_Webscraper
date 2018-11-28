#include <iostream> 

using namespace std;   

int main (int argc, char const *argv[])
{
  int T;
  cin >> T;
  
  for (int i = 1; i <= T; i++) {
    unsigned int N, K;
    cin >> N;
    cin >> K;    
    
    bool result = (K % (1u << N)) + 1u == (1u << N);
     
    cout << "Case #" << i << ": ";
    if (result) {
       cout << "ON";
    } else {
      cout << "OFF";
    } 
    
      cout << endl;       
    
  }
  
  return 0;
}