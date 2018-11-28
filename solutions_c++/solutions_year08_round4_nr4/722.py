#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

char buf[50010];

int main()
{
  int N;
  cin >> N;

  for (int cas = 1; cas <= N; cas++) {
    int k;
    cin >> k;
    cin >> buf;

    //cout << k << " '" << buf << "'" << endl;

    int perm[20];
    int minv = strlen(buf);
    
    for (int i = 0; i < k; i++) perm[i] = i;

    do {
      int count = 0;
      char prev = 0;
      for (int i = 0; buf[i]; i++) {
        char c = buf[(i/k)*k+perm[i%k]];
        if (c != prev) {
          count++;
          prev = c;
        }
      }
      //for (int i = 0; i < k; i++) cout << perm[i] << " ";
      //cout << endl;
      //cout << count << endl;
      if (minv > count) {
        minv = count;
      }
    } while (next_permutation(&perm[0], &perm[k]));
    cout << "Case #" << cas << ": " << minv << endl;
  }
  
  return 0;
}

