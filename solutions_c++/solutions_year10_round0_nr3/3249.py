#include <iostream>
#include <fstream>

using namespace std;

int main() {

  fstream file;
  file.open("C-small-attempt0.in");
  int index, total, T, R, k, N;
  file >> T;
  int c = 1;
  for (int i = 0; i < T; i++) {
    file >> R >> k >> N;
    int arr[1000] = {0};
    index = 0;
    int euros = 0;
    for (int j = 0; j < N; j++) {
      file >> arr[j];
    }
    while (R > 0) {
      //keep adding onto total from groups until it can't take any more
      total = 0; 
      int count = 0;
      while (total + arr[index] <= k) {
        total += arr[index];
        index++;
        if (index >= N)
          index = 0;
        count ++;
        if ( count >= N )
          break;
      }
      //add total onto euros
      euros += total;
      R--;
    }
    cout << "Case #" << c << ": " << euros << "\n";
    c++;
  }
  return 0;
}
    


