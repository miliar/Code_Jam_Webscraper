#include <iostream>
using namespace std;

int main(){
    int t, T;
    cin >> T;
    for(t = 1; t <= T; t++){
          int R, k, N, i, ptr, income;
          income = ptr = 0;
          int *size;
          cin >> R >> k >> N;
          size = new int[N];
          for(i = 0; i < N; i++){
                cin >> size[i];
          }
          for(i = 0; i < R; i++){
                int start = ptr;
                int car = size[ptr++];
                if(ptr == N){
                       ptr = 0;
                }
                while(car + size[ptr] <= k && ptr != start){
                          car += size[ptr++];
                          if(ptr == N){
                                 ptr = 0;
                          }
                }
                income += car;
          }
          cout << "Case #" << t << ": " << income << endl;
          delete [] size;
    }
    return 0;
}
