#include <iostream>
#include <fstream>
#include <string>

using namespace std;

typedef long long ll;

void masol(ll honnan[][2], ll hova[][2], int N) {
     for (int i=0; i<N; ++i) {
         hova[i][0] = honnan[i][0];
         hova[i][1] = honnan[i][1];     
     }
}

void gyorsit(ll ezt[][2], ll gyors[][2], int N) {
     for (int i=0; i<N; ++i) {
         ll ujsum = ezt[i][1];
         ll ujpos = ezt[i][0];
         gyors[i][0] = ujpos + ezt[(i + ujpos) % N][0];
         gyors[i][1] = ujsum + ezt[(i + ujpos) % N][1];
     }
}

int main () {
  ifstream myfile("C-large.in");

  if (myfile.is_open())
  {
    int T;
    // T test cases
    myfile >> T;

    for (int i=0; i<T; ++i) {
        int R, k, N;
        // R rides
        myfile >> R;
        // k places
        myfile >> k;
        // N groups
        myfile >> N;
        
        int g[N];
        for (int j=0; j<N; ++j) {
           myfile >> g[j];
        }
        
        ll mo = 0;
        if (N < 2) mo = g[0] * R;
        else {
             ll info[N][2];
             for (int j=0; j<N; ++j) {
               ll sum = 0;
               ll l;
               for (l = 0; l<N; l++) {
                   if ((sum + g[(l+j)%N]) <= k) sum += g[(l+j)%N];
                   else break;
               }
               info[j][0] = l;
               info[j][1] = sum;
             }
             
             ll orig[N][2];
             ll uj[N][2];
             masol(info, orig, N);
             int db=0;
             for (; db<13; db++)
             {
                 gyorsit(orig, uj, N); 
                 masol(uj, orig, N);
             }
             
//             for (int c=0; c<N; c++){
//                 cout << orig[c][0] << ", " << orig[c][1] << endl;
//             }

             ll pos = 0;
             ll sum = 0;
             int i;
             for (i = 0; i <= R-(1 << db); i+=(1 << db)) {
                sum += orig[pos][1];
                pos = (pos + orig[pos][0]) % N;
             }
             for (; i < R; ++i) {
                sum += info[pos][1];
                pos = (pos + info[pos][0]) % N;
             }
             
             mo = sum;

        }
        
        cout << "Case #" << i+1 << ": " << mo << endl; 
        cerr << "Case #" << i+1 << ": " << mo << endl; 
    }
    
    myfile.close();
  }

  else cout << "Unable to open file"; 

  return 0;
}


