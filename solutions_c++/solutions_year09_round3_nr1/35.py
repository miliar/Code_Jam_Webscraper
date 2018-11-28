#include <iostream>

using namespace std;

long long Solve( string S )
{
  int Index[256];

  for (int i = 0; i < 256; i++)
    Index[i] = -1;

  int Base = 0;
  for (int i = 0; i < S.size(); i++)
    if (Index[(int) S[i]] == -1)
    {
      if (i == 0)
        Index[(int) S[i]] = 1;
      else if (Base == 1)
        Index[(int) S[i]] = 0;
      else
        Index[(int) S[i]] = Base;
      Base++;
    }

  if (Base < 2)
    Base = 2;

  long long Result = 0;
  for (int i = 0; i < S.size(); i++)
    Result = Result * Base + Index[(int) S[i]];

  return Result;
}

int main()
{
  int T;
  cin >> T;
  string EmptyStr;
  getline( cin, EmptyStr );
  for (int i = 0; i < T; i++)
  {
    string S;
    getline( cin, S );

    cout << "Case #" << i + 1 << ": " << Solve( S ) << endl;
  }
  return 0;
}

