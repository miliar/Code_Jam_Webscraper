#include <iostream>
#include <string>

using namespace std;

typedef bool Pattern[15][26];

string Dic[10000];
int DicCount;
int WordLength;

void ParsePattern( Pattern &P, string S )
{
  int Index = 0;
  for (int i = 0; i < WordLength; i++)
  {
    for (int j = 0; j < 26; j++)
      P[i][j] = false;
    if (S[Index] == '(')
    {
      Index++;
      while (S[Index] != ')')
      {
        int c = (int)(S[Index]) - 97;
        P[i][c] = true;
        Index++;
      }
      Index++;
    }
    else
    {
      int c = (int)(S[Index]) - 97;
      P[i][c] = true;
      Index++;
    }
  }
}

bool Match( Pattern &P, string S )
{
  for (int i = 0; i < WordLength; i++)
  {
    int c = (int)(S[i]) - 97;
    if (!P[i][c])
      return false;
  }

  return true;
}

int main()
{
  int N;
  cin >> WordLength >> DicCount >> N;

  for (int i = 0; i < DicCount; i++)
    cin >> Dic[i];

  for (int i = 0; i < N; i++)
  {
    string PatternStr;
    cin >> PatternStr;

    int Count = 0;
    Pattern P;
    ParsePattern( P, PatternStr );
    for (int j = 0; j < DicCount; j++)
      if (Match( P, Dic[j] ))
        Count++;

    cout << "Case #" << i + 1 << ": " << Count << endl;
  }

  return 0;
}

