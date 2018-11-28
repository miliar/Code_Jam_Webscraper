#include <iostream>
#include <vector>
using namespace std;

int runTestCase(int numCandy, int values[]){
  int smallest = values[0];
  for(int i=1; i<numCandy; i++){
    if(smallest > values[i]) smallest = values[i];
  }
  return smallest;
}

int main(int argc, char *argv[]){
	int numTests;
  cin >> numTests;
  for(int i=1; i<=numTests; i++){
    int numCandy;
    int candyValues[10000];
    unsigned int result = 0;
    unsigned int total = 0;
    bool possible=true;
    
    cin >> numCandy;
    for(int j=0; j<numCandy; j++){
      cin >> candyValues[j];
      result ^= candyValues[j];
      total += candyValues[j];
    }
    if(result != 0) possible = false;
    
    if(possible)
      result = total - runTestCase(numCandy, candyValues);
    cout << "Case #" << i << ": ";
    if(!possible) cout << "NO";
    else cout << result;
    cout << endl;
  }
  
  return 0;
}