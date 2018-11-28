#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
  int N;
  string str;
  const string wel = "welcome to code jam";

  cin >> N;
  getline(cin, str);
  for( int ca = 1 ; ca <= N ; ++ca ) {
    getline(cin, str);
    vector<int> subs(str.size() + 1, 1);
    subs[str.size()] = 0;

    for( int j = wel.size() - 1 ; j >= 0 ; --j ) {
      for( int i = str.size() - 1 ; i >= 0 ; --i ) {
        if( str[i] == wel[j] ) {
          subs[i] = (subs[i] + subs[i + 1]) % 10000;
        } else {
          subs[i] = subs[i + 1];
        }
      }
    }
    // compute
    printf("Case #%d: %04d\n", ca, subs[0]);
  }
}
