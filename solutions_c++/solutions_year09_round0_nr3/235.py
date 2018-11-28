#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
  int N, L, total, a, b, c, d;
  int counts[19][500];
  string welcome = "welcome to code jam";
  string text;
  
  cin >> N >> ws;
  for(int n=1; n<=N; n++) {
    getline(cin, text);
    L = text.length();
    for(int j=0; j<L; j++) {
      if(text[j] == welcome[0]) {
        counts[0][j] = 1;
      } else {
        counts[0][j] = 0;
      }
    }

    for(int i=1; i<19; i++) {
      total = 0;
      for(int j=0; j<L; j++) {
        if(text[j] == welcome[i]) {
          counts[i][j] = total;
        } else {
          counts[i][j] = 0;
        }
        total += counts[i-1][j];
        total = total % 10000;
      }
    }

    total = 0;
    for(int j=0; j<L; j++) {
      total += counts[18][j];
      total = total % 10000;
    }
    a = (total % 10000) / 1000;
    b = (total % 1000) / 100;
    c = (total % 100) / 10;
    d = (total % 10);
    cout << "Case #" << n << ": " << a << b << c << d << endl;
  }

  return 0;
}
