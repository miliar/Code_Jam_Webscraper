#include <iostream> 

using namespace std;   

int main (int argc, char const *argv[])
{
  int T;
  cin >> T;
  
  for (int i = 1; i <= T; i++) {
    unsigned int R, k, N;
    unsigned int *g;
    cin >> R;
    cin >> k;
    cin >> N;
    
    unsigned int y = 0;
    
    g = new unsigned int[N]; 
    for (unsigned int j = 0; j < N; j++) {
      cin >> g[j];
    }  
    
    int current = 0;
    
    for (unsigned int j = 1; j <= R; j++) {
      unsigned int sum = 0; 
      unsigned int group_count = 0;
      while (sum + g[current] <= k && group_count < N) {
        sum += g[current];
        current = (current + 1) % N;  
        group_count++;
      }          
      y += sum;
    }         
     
    delete g;
     
    cout << "Case #" << i << ": " << y << endl;
            
  }
  
  return 0;
}