#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
     int cases;
     cin >> cases;
     for(int k=1; k<=cases; k++) {
          int num;
          cin >> num;
          long a[num];
          long b[num];
          memset(a, 0, sizeof(long) * num);
          memset(b, 0, sizeof(long) * num);

          for(int i=0; i<num; i++) cin >> a[i];
          for(int i=0; i<num; i++) cin >> b[i];

          sort(a, a+num);
          sort(b, b+num);

          long min = LONG_MAX;
          long sum = 0;

          for(int i=0; i<num; i++) 
               sum += a[i] * b[ num - i - 1];

          if(sum < min) 
               min = sum;
          sum = 0;
          for(int i=0; i<num; i++) {
               sum += b[i] * a[num - i - 1];
          }

          if(sum < min) 
               min = sum;

//           do {
//                long sum = 0;
//                for(int i=0; i<num; i++) {
//                     do {
//                          sum = 0;
//                          for(int j=0; j<num; j++) {
//                               if(sum > min) break;
//                               sum += a[j] * b[j];
//                          }
//                          if(sum < min) min = sum;

//                     } while(next_permutation(b, b+num));
//                }

//           } while(next_permutation(a, a+num));

          cout << "Case #" << k << ": " << min << endl;
     }
     return 0;
}
