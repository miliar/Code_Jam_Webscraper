#include <iostream.h>

unsigned long int get_gcd(unsigned long int a, unsigned long int b);

int main() {

    unsigned int C;
    unsigned int N;
    
    cin >> C;
    
    unsigned int i;
    for (i = 0; i < C; i++) {
        cin >> N;
        if (N == 2) {

              unsigned long long int time1, time2;
              cin >> time1;
              cin >> time2;

              unsigned long long int temp; 
              if (time1 > time2) {
                 temp = time2;
                 time2 = time1;
                 time1 = temp;                     
              }

              unsigned long long int difference;
              difference = time2 - time1;

              unsigned long long int time_pointer = time1;
              if (difference == 0) {
                 cout << "Case #" << i+1 << ": 0" << endl;
              } else {
                while ( time_pointer > difference ) time_pointer -= difference;
                cout << "Case #" << i+1 << ": " << (difference - time_pointer) << endl;
              }
              
        } else if (N ==3) {

              unsigned long long int times[3];
              unsigned int j;
              for (j = 0; j < N; j++) {
                  cin >> times[j];
              }
              unsigned long long int temp;
              
              if (times[0] > times[1]) {temp = times[1]; times[1] = times[0]; times[0] = temp; }
              if (times[1] > times[2]) {temp = times[1]; times[1] = times[2]; times[2] = temp; }
              if (times[0] > times[1]) {temp = times[1]; times[1] = times[0]; times[0] = temp; }

              unsigned long long int differences[2];
              differences[0] = times[1] - times[0];
              differences[1] = times[2] - times[1];             

              if ((differences[0] == 0) && (differences[1] == 0)) {
                 cout << "Case #" << i+1 << ": 0" << endl;                                                                                
              } else {

                  unsigned long long int gcd;
    
                  if (differences[0] == 0) {
                     gcd = differences[1];
                  } else if (differences[1] == 0) {
                     gcd = differences[0];
                  } else {
                      if (differences[0] == differences[1]) {
                         gcd = differences[0];
                      } else if (differences[0] > differences[1]) {
                             gcd = get_gcd(differences[0], differences[1]);
                      } else {
                             gcd = get_gcd(differences[1], differences[0]);
                      }
                  }
    
                  unsigned long long int time_pointer = times[0];
                  
                  while ( time_pointer > gcd) {
                        time_pointer -= gcd;
                  }
                  
                  cout << "Case #" << i+1 << ": " << (gcd - time_pointer) << endl;

              }


        } else {
               cout << "N cant be this" << endl;
        }
    }
}

unsigned long int get_gcd(unsigned long int a, unsigned long int b) {

         do {
             unsigned long temp;
             a = a - b;
             if (a == b) return b;
             if (a < b) {
                   temp = a;
                   a = b;
                   b = temp;
             }
         } while(a != 0);
         return b;
}
