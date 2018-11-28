#include <iostream>
#include <string>

using namespace std;

int N;
string Matrix[50];

bool IsPermissible( int r, int c )
{
  for (int i = c + 1; i < N; i++)
    if (Matrix[r][i] == '1')
      return false;

  return true;
}

int Solve()
{
  int Swap = 0;
  for (int c = 0; c < N; c++)
  {
    bool test = false;
    int r = c;
    for (; r < N; r++)
      if (IsPermissible(r, c))
      {
        test = true;
        break;
      }
    if (test)
    {
      Swap += r - c;
      string Temp = Matrix[r];
      for (int k = r; k > c; k--)
        Matrix[k] = Matrix[k - 1];
      Matrix[c] = Temp;
    }
  }

  return Swap;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++)
  {
    cin >> N;

    string S;
    getline( cin, S );

    for (int j = 0; j < N; j++)
    {
      getline( cin, S );
      Matrix[j] = S;
    }

    cout << "Case #" << i + 1 << ": " << Solve() << endl;
  }

  return 0;
}
