#include <iostream>

using namespace std;

bool Possible( string S, int Index )
{
  for (int i = Index + 1; i < S.size(); i++)
    if (S[Index] < S[i])
      return true;

  return false;
}

void Swap( string &S, int n, int m )
{
  char Temp = S[n];
  S[n] = S[m];
  S[m] = Temp;
}

void Sort( string &S, int sIndex, int eIndex )
{
  for (int i = sIndex; i <= eIndex; i++)
    for (int j = i + 1; j <= eIndex; j++)
      if (S[i] > S[j])
        Swap( S, i, j );
}

string Change( string S, int Index )
{
  bool Test = false;
  int MinIndex;
  for (int i = Index + 1; i < S.size(); i++)
    if (S[Index] < S[i])
      if (Test)
      {
        if (S[MinIndex] > S[i])
          MinIndex = i;
      }
      else
      {
        Test = true;
        MinIndex = i;
      }

  Swap( S, Index, MinIndex );
  Sort( S, Index + 1, S.size() - 1 );

  return S;
}

string Next( string S )
{
  for (int i = S.size() - 1; i >= 0; i--)
    if (Possible( S, i ))
      return Change( S, i );

  S += '0';
  Sort( S, 0, S.size() - 1 );
  for (int n = 1; n < S.size(); n++)
    if (S[n] != '0')
    {
      Swap( S, 0, n);
      return S;
    }

  return S;
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
    cout << "Case #" << i + 1 << ": " << Next( S ) << endl;
  }
}

