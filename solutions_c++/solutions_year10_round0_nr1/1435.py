#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

#define OFF 1
#define ON 0

int test(int N, int K) {
  int l = 1 << N;
  return (K + 1) % l;
}

int main(int argc, const char *argv[]) {
  istream *tmp;
  ifstream file;
  string strOn = "ON";
  string strOff = "OFF";

  if (argc > 1) {
    file.open(argv[1], ios::in);
    tmp = &file;
  } else {
    tmp = &cin;
  }

  int num = 0;
  istream& input = *tmp;

  input >> num;

  int N = 0, K = 0;
  int i = 1;

  while(i <= num) {
    input >> N;
    input >> K;
    cout << "Case #" << i << ": ";
    if (test(N, K) == ON) {
      cout << strOn;
    } else {
      cout << strOff;
    }
    cout << "\n";
    i++;
  }
}
