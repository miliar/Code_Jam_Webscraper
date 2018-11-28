#include <iostream>
#include <string>
#include <sstream>

long long gcd(long long a,long long b) {
  if (b>a) return gcd(b,a);
  if (b==0) return a;
  return gcd(b,a%b);
}


using namespace std;

int main() {
  int T;
  cin >> T;

  for (int x2=0;x2<T;x2++) {

    //long long N;
    long long N;
    int PD;
    int PG;

    cin >> N;
    cin >> PD;
    cin >> PG;

    /* long long N;
    if (N1.size()>10) {
      N=1000;
    } else {
      istringstream in(N1);
      in >> N;
      } */


    // Step 1, calculate the GCD(PD,100)
    int g = gcd(PD,100);
    
    // Solvable if N >= 100/g;
    int nt = 100/g;


    
    // I played D<=N games
    // PD is the probabilty that I 
    // won out of the D games.

    // So, Exist an integer 0<D1,D<=N s.t. D1/D = PD/100

    // , i.e., does there exist D1<= D s.t.  100 D1 = PD * D

    //cout << "***" << N << " " << PD << " " << PG << endl;
    bool done = false;
    if (PD==0) done=true;
    if (nt<=N) done = true;

    if (((PG==100)&&(PD<100))||((PG==0)&&(PD>0))) {
      
	cout << "Case #"<<x2+1<<": Broken" << endl;
    } else {
      if (done) {
	cout << "Case #"<<x2+1<<": Possible" <<endl;
      } else {
	cout << "Case #"<<x2+1<<": Broken" <<endl;
      }
    }
  }
}

