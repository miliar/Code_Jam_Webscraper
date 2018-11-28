#include <iostream>
#include <string>

using namespace std;

int Solve( string S )
{
  string T = "welcome to code jam";
  int Count[19];

  for (int i = 0; i < 19; i++)
    Count[i] = 0;

  for (int i = 0; i < S.size(); i++)
  {
    int Count2[19];
    if (S[i] == T[0])
      Count2[0] = (Count[0] + 1) % 10000;
    else
      Count2[0] = Count[0];
    for (int j = 1; j < 19; j++)
      if (S[i] == T[j])
        Count2[j] = (Count[j] + Count[j - 1]) % 10000;
      else
        Count2[j] = Count[j];

    for (int j = 0; j < 19; j++)
      Count[j] = Count2[j];
  }

  return Count[18];
}

int main()
{
  int N;
  cin >> N;

  string EmptyStr;
  getline( cin, EmptyStr, '\n' );

  for (int i = 0; i < N; i++)
  {
    string S;
    getline( cin, S, '\n' );

    cout << "Case #" << i + 1 << ": ";
    int Count = Solve( S );
    if (Count < 10)
      cout << "000";
    else if (Count < 100)
      cout << "00";
    else if (Count < 1000)
      cout << "0";
    cout << Count << endl;
  }

  return 0;
}

