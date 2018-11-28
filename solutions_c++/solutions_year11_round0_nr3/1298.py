#include <iostream>
using namespace std;
int main() {
  int TT; cin >>TT;
  for (int T = 1; T<=TT; T++){
  cout <<"Case #"<<T<<": ";
     long long  sum = 0 ;
     int max = 0x3fffffff ;
     int P = 0;
     int N;
     cin >> N;
     while (N--)  {
        int tmp;
        cin >> tmp;
        P ^= tmp;
        sum += tmp;
        if (tmp<max) max = tmp;
     }
     if (P) cout << "NO"<< endl;
            else cout << sum - max << endl;
  }
}
