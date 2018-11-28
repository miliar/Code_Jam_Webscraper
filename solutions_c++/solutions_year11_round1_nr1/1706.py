#include <iostream>

using namespace std;

int main() {
  int T, N, PD, PG,j,k;
  cin >> T;
  for(int i = 1; i <=T; i++) {
    cin >> N >> PD >> PG;
    cout << "Case #" << i << ": ";
    if(PD != 100 && PG == 100) { cout <<"Broken\n"; continue; }
    if(PD != 0 && PG == 0) {cout << "Broken\n"; continue; }
    if(PD == 100 && PG == 100) {cout <<"Possible\n"; continue; }
    if(PD == 0 && PG == 0) {cout << "Possible\n"; continue; }

    int a = PD; int b = 100;
    if(a%5 == 0) {a = a/5; b = b/5;}
    if(a%5 == 0) {a = a/5; b = b/5;}
    if(a%2 == 0) {a = a/2; b = b/2;}
    if(a%2 == 0) {a = a/2; b = b/2;}
    if(b > N) {cout <<"Broken\n"; continue; }
    cout <<"Possible\n";
    /*    
    int d = PG; int e = 100;
    if(d%5 == 0) {d = d/5; e = e/5;}
    if(d%5 == 0) {d = d/5; e = e/5;}
    if(d%2 == 0) {d = d/2; e = e/2;}
    if(d%2 == 0) {d = d/2; e = e/2;}
    float up = (e*a - d*b)/(d-e);

    for(k = 0; k <= up; k++) {
      if((d*(k+b))%e == 0 && ((d*(k+b))/e) -a >= 0) {
        cout <<"Possible\n";
        break;
      }
    }

    if(k > up)
      cout <<"Broken\n";
  */
  }
}
