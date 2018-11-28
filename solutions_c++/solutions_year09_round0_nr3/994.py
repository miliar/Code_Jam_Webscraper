
#include <iostream>
#include <cstring>
using namespace std;

int nletters = 19;
char letters[] = "welcome to code jam";

unsigned int m[501][20];

void solve(int T)
{
  string line;
  int total = 0;
  getline(cin, line);

//  cout << line << endl;

  memset(m, 0, sizeof m);
  for (int i = 0; i < line.size(); i++)
    m[i][nletters] = 1;

  for (int i = line.size() - 1; i >= 0; i--)
    for (int j = nletters - 1; j >= 0; j--)
    {
      m[i][j] = m[i+1][j];
      if (line[i] == letters[j])
        m[i][j] = (m[i][j] + m[i][j+1])%10000;
    }

//  for (int i = 0; i < line.size(); i++)
//    for (int j = 0; j < nletters; j++)
//      printf("%3d%c", m[i][j], j+1==nletters?'\n':' ');


  printf("Case #%d: %.4d\n", T, m[0][0]);
}

int main()
{
  int T;
  string line;

  cin >> T;
  getline(cin, line);

  for (int i = 0; i < T; i++)
    solve(i+1);

  return 0;
}
