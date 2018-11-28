#include <iostream>
using namespace std;

const int MAXI = 1000001;
int maxwin[MAXI];
int T, A1, A2, B1, B2;

int main(int argc, char *argv[]) {
  maxwin[1] = 0;
  maxwin[2] = 1;
  maxwin[3] = 1;
  maxwin[4] = 2;
  maxwin[5] = 3;
  maxwin[6] = 3;
  maxwin[7] = 4;
  maxwin[8] = 4;
  maxwin[9] = 5;
  int curmaxwin = 2;
  for(int i = 10; i <= MAXI; i++) {
    while(maxwin[curmaxwin+1] < i-(curmaxwin+1)) {
      curmaxwin++;
    }
    maxwin[i] = curmaxwin; 
  }
 
  cin >> T >> ws;
  long long count = 0;
  for(int t=1; t<=T; t++) {
    cin >> A1 >> A2 >> B1 >> B2 >> ws;
    count = 0;
    for(int A = A1; A <= A2; A++) {
      if(B1 <= maxwin[A]) count += min(maxwin[A],B2) - B1 + 1;
    }
    for(int B = B1; B <= B2; B++) {
      if(A1 <= maxwin[B]) count += min(maxwin[B],A2) - A1 + 1;
    }
    cout << "Case #" << t << ": " << count << endl;
  }
  
  return 0;
}
