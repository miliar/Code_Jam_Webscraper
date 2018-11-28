#include <iostream>

using namespace std;

int main()
{
  int T;
  long long Queue[10000];
  long long Size[10000];
  int NewPos[10000];
  int LastUsedRound[10000];
  long long TotalMoney[10000];

  cin >> T;
  for (int CaseNo = 0; CaseNo < T; CaseNo++)
  {
    long long R, k, N;
    cin >> R >> k >> N;

    for (int i = 0; i < N; i++)
    {
      cin >> Queue[i];
      Queue[N + i] = Queue[i];
    }

    for (int i = 0; i < N; i++)
    {
      Size[i] = 0;
      NewPos[i] = i;
      for (int j = 0; j < N; j++)
        if (Size[i] + Queue[i + j] <= k)
          Size[i] = Size[i] + Queue[i + j];
        else
        {
          NewPos[i] = (i + j) % N;
          break;
        }
    }

    for (int i = 0; i < N; i++)
      LastUsedRound[i] = -1;

    long long Money = 0;
    long long RoundNo = 0;
    int Pos = 0;
    while (true)
    {
      if (RoundNo == R)
        break;
      if (LastUsedRound[Pos] != -1)
      {
        long long DiffMoney = Money - TotalMoney[LastUsedRound[Pos]];
        long long DiffRound = RoundNo - LastUsedRound[Pos];
        long long CycleCount = (R - RoundNo) / DiffRound;
        Money += CycleCount * DiffMoney;
        RoundNo += CycleCount * DiffRound;

        break;
      }

      LastUsedRound[Pos] = RoundNo;
      TotalMoney[RoundNo] = Money;

      Money += Size[Pos];
      RoundNo++;
      Pos = NewPos[Pos];
    }

    while (RoundNo < R)
    {
      Money += Size[Pos];
      RoundNo++;
      Pos = NewPos[Pos];
    }

    cout << "Case #" << CaseNo + 1 << ": " << Money << endl;
  }
}

