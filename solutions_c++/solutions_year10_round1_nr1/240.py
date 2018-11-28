#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;

int testID;
char map[100][100];

int N, K;
bool checkPosi(int i, int j, char c)
{
  bool rowOK = true;
  for (int nowi = i; nowi < i + K; ++nowi)
    if (nowi >= N || map[nowi][j] != c) 
    {
      rowOK = false;
      break;
    }

  if (rowOK)
    return true;

  bool colOK = true;
  for (int nowj = j; nowj < j + K; ++nowj)
    if (nowj >= N || map[i][nowj] != c)
    {
      colOK = false;
      break;
    }
  if (colOK)
    return true;

  bool digOK = true;
  for (int nowi = i, nowj = j; nowi < i + K; ++nowi, ++nowj)
    if (nowi >= N || nowj >= N || map[nowi][nowj] != c)
    {
      digOK = false;
      break;
    }

  if (digOK)
    return true;

  digOK = true;
  for (int nowi = i, nowj = j; nowi < i + K; ++nowi, --nowj)
    if (nowi >= N || nowj < 0 || map[nowi][nowj] != c)
    {
      digOK = false;
      break;
    }
  if (digOK)
    return true;

  return false;
}

void deal()
{
  scanf("%d%d", &N, &K);

  string line;
  getline(cin, line);
  for (int i = 0; i < N; ++i)
  {
    getline(cin, line);
    for (int j = 0; j < N; ++j)
      map[i][j] = line[j];
  }

  for (int i = 0; i < N; ++i)
    for (int j = N - 1; j >= 0; --j)
      if (map[i][j] != '.')
      {
        char now = map[i][j];
        while (j + 1 < N && map[i][j + 1] == '.')
        {
          map[i][j] = '.';
          j++;
        }
        map[i][j] = now;
      }

  bool rok = false;
  bool bok = false;

  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
    {
      if (checkPosi(i, j, 'R'))
        rok = true;
      if (checkPosi(i, j, 'B'))
        bok = true;
    }


  if (rok && bok)
    cout << "Case #" << testID << ": " << "Both" << endl;
  if (!rok && !bok)
    cout << "Case #" << testID << ": " << "Neither" << endl;
  if (rok && !bok)
    cout << "Case #" << testID << ": " << "Red" << endl;
  if (!rok && bok)
    cout << "Case #" << testID << ": " << "Blue" << endl;
}

int main()
{
  int T;
  scanf("%d", &T);
  for (testID = 1; testID <= T; ++testID)
    deal();
  return 0;
}
