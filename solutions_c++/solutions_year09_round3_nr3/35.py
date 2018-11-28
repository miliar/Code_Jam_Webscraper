#include <iostream>

using namespace std;

int P, Q;
int CellNo[100];

bool HasBeenComputed[100][100];
int Mem[100][100];

int Solve( int q1, int q2 )
{
  if (q1 > q2)
    return 0;
  if (HasBeenComputed[q1][q2])
    return Mem[q1][q2];

  int p1, p2;
  if (q1 > 0)
    p1 = CellNo[q1 - 1] + 1;
  else
    p1 = 1;
  if (q2 < Q - 1)
    p2 = CellNo[q2 + 1] - 1;
  else
    p2 = P;

  int People = p2 - p1 + 1;

  int Min = Solve( q1 + 1, q2 );
  for (int i = q1 + 1; i <= q2; i++)
    if (Min > Solve( q1, i - 1 ) + Solve( i + 1, q2 ))
      Min = Solve( q1, i - 1 ) + Solve( i + 1, q2 );

  Mem[q1][q2] = Min + People - 1;
  HasBeenComputed[q1][q2] = true;
  return Mem[q1][q2];
}

int main()
{
  int N;
  cin >> N;
  for (int i = 0; i < N; i++)
  {
    cin >> P >> Q;
    for (int j = 0; j < Q; j++)
      cin >> CellNo[j];

    for (int j = 0; j < 100; j++)
      for (int k = 0; k < 100; k++)
        HasBeenComputed[j][k] = false;
    cout << "Case #" << i + 1 << ": " << Solve( 0, Q - 1 ) << endl;
  }
}

