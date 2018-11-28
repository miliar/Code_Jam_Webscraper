
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main(int argc, char **argv) {
  if(argc != 2) {
    cout << "Missing filename" << endl;
    return -1;
  }

  ifstream fp(argv[1]);
  
  int T;
  fp >> T;

  for(int i = 0; i < T; i++) {
    unsigned int R, k, N, tmp;
    queue<unsigned int> line, riders;
    fp >> R;
    fp >> k;
    fp >> N;
    for(int j = 0; j < N; j++) {
      fp >> tmp;
      line.push(tmp);
    }
    
    unsigned int total_money = 0;
    for(int j = 0; j < R; j++) {
      unsigned int passengers = 0;
      
      while(!line.empty() && line.front() <= k-passengers) {
        passengers += line.front();
        riders.push(line.front());
        line.pop();
      }
      
      while(!riders.empty()) {
        line.push(riders.front());
        riders.pop();
      }
      total_money += passengers;
//      cout << "P" << j << "\t" << passengers << "\t" << total_money << endl;
    }


    cout << "Case #" << (i+1) << ": " << total_money << endl;
  }

}

