#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

string base = "welcome to code jam";

int main () {
  int N;
  
  scanf ("%d", &N);
  
  getchar();
  
  for (int n = 1; n <= N; n++) {
    string line;
    for (char c = getchar(); c != '\n'; c = getchar())
      line.push_back(c);
    
    vector<vector<int> > table (19);
    for (int i = 0; i < 19; i++)
      table[i] = vector<int> (line.size() + 1, 0);
    
    for (int i = line.size()-1; i >= 0; i--) {
      if (base[18] == line[i])
        table[18][i] = (table[18][i+1] + 1)%10000;
      else
        table[18][i] = table[18][i+1];
    }
    
    for (int i = 17; i >= 0; i--) {
      for (int j = line.size()-1; j >= 0; j--) {
        if (base[i] == line[j])
          table[i][j] = (table[i][j+1] + table[i+1][j+1])%10000;
        else
          table[i][j] = table[i][j+1];
      }
    }
    printf ("Case #%d: %04d\n", n, table[0][0]);
  }
  
  return 0;
}
