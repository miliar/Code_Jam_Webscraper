#include <iostream>
#include <vector>
using namespace std;

int rep[2][3][5][7];

void compute_rep() {
  memset(rep, 0, sizeof(rep));
  int computed = 1;
  int i = 0;
  while (computed < 210) {
    i++;
    int a = i%2, b=i%3, c=i%5, d=i%7;

    if (rep[a][b][c][d])
      continue;

    rep[a][b][c][d] = i;
    computed++;
  }
}

long long int ways[40][2][3][5][7];
string val;

void inc(int p, long long int k, long long int v) {
  int a=(k%2+2)%2, b=(k%3 + 3)%3, c=(k%5 + 5)%5, d=(k%7 + 7)%7;
  ways[p][a][b][c][d] += v;
}

int get_rep(string v) {
  int r = 0;
  for (int i = 0; i < v.size(); i++) {
    r = r*10 + v[i] - '0';
    r = rep[r%2][r%3][r%5][r%7];
  }
  return r;
}

void compute_ways(int index) {
  for (int p = index; p >= 1; p--) {
    for (int i = 0; i < 2; i++)
      for (int j = 0; j < 3; j++)
        for (int k = 0; k < 5; k++)
          for(int l = 0; l < 7; l++) {
            long long int v1 = rep[i][j][k][l];
            long long int v2 = get_rep(val.substr(p, index - p + 1));

            inc(index, v1 + v2, ways[p-1][i][j][k][l]);
            inc(index, v1 - v2, ways[p-1][i][j][k][l]);
          }
  }

  long long int v = get_rep(val.substr(0, index + 1));

  inc(index, v, 1);
}

int main() {
  compute_rep();
  int T;
  cin>>T;

  int testcase = 1;
  while (testcase <= T) {
    memset(ways, 0, sizeof(ways));
    cin >> val;
    for (int i = 0; i < val.size(); i++) {
      compute_ways(i);
    }

    long long int res = 0;
    int s = val.size() - 1;
    for (int i = 0; i < 2; i++)
      for (int j = 0; j < 3; j++)
        for (int k = 0; k < 5; k++)
          for(int l = 0; l < 7; l++) {
            if (i == 0 || j == 0 || k == 0 || l == 0)
              res += ways[s][i][j][k][l];
          }

    cout << "Case #" << testcase << ": " << res << endl;
    testcase++;
  }

  return 0;
}
