#include <iostream>
#include <set>

using namespace std;

int N, k;
int Point[100][25];

bool Graph[100][100];
set<int> Chart[100];
int HasDecided[100];
int ChartCount;

bool Cross( int m, int n )
{
  for (int i = 0; i < k; i++)
    if (Point[m][i] == Point[n][i])
      return true;

  for (int i = 0; i < k - 1; i++)
    if (Point[m][i] < Point[n][i] && Point[m][i + 1] > Point[n][i + 1])
      return true;
    else if (Point[m][i] > Point[n][i] && Point[m][i + 1] < Point[n][i + 1])
      return true;

  return false;
}

void MakeGraph()
{
  for (int i = 0; i < N; i++)
  {
    Graph[i][i] = false;
    for (int j = i + 1; j < N; j++)
      if (Cross( i, j ))
        Graph[i][j] = Graph[j][i] = false;
      else
        Graph[i][j] = Graph[j][i] = true;
  }
}

int GeneralMinimum;

bool Permissible( int Var, int ChartNo )
{
  for (set<int>::iterator it = Chart[ChartNo].begin(); it != Chart[ChartNo].end(); it++)
    if (!Graph[Var][*it])
      return false;

  return true;
}

int Solve( int Layer )
{
  if (ChartCount >= GeneralMinimum)
    return GeneralMinimum;
  if (Layer == N)
  {
    if (GeneralMinimum > ChartCount)
      GeneralMinimum = ChartCount;
    return ChartCount;
  }

  int DecisionVar = -1;
  int CurrentConflict, FutureConflict;
  for (int i = 0; i < N; i++)
    if (!HasDecided[i])
    {
      int TempCurrentConflict = 0, TempFutureConflict = 0;
      for (int j = 0; j < N; j++)
        if (!Graph[i][j])
          if (HasDecided[j])
            TempCurrentConflict++;
          else
            TempFutureConflict++;
      if (DecisionVar < 0)
      {
        DecisionVar = i;
        FutureConflict = TempFutureConflict;
        CurrentConflict = TempCurrentConflict;
      }
      else if ((TempCurrentConflict > CurrentConflict) || (TempCurrentConflict == CurrentConflict && TempFutureConflict > FutureConflict))
      {
        DecisionVar = i;
        FutureConflict = TempFutureConflict;
        CurrentConflict = TempCurrentConflict;
      }
    }

  int Min = -1;
  HasDecided[DecisionVar] = true;
  for (int i = 0; i < ChartCount; i++)
    if (Permissible( DecisionVar, i ))
    {
      Chart[i].insert( DecisionVar );
      int TempMin = Solve( Layer + 1 );
      if (Min < 0 || TempMin < Min)
        Min = TempMin;
      Chart[i].erase( DecisionVar );
    }

  Chart[ChartCount].clear();
  Chart[ChartCount].insert( DecisionVar );
  ChartCount++;
  int TempMin = Solve( Layer + 1 );
  if (Min < 0 || TempMin < Min)
    Min = TempMin;
  ChartCount--;
  Chart[ChartCount].clear();
  HasDecided[DecisionVar] = false;

  return Min;
}

int main()
{
  int T;
  cin >> T;

  for (int i = 0; i < T; i++)
  {
    cin >> N >> k;
    for (int j = 0; j < N; j++)
      for (int l = 0; l < k; l++)
        cin >> Point[j][l];

    MakeGraph();
    for (int j = 0; j < 100; j++)
      HasDecided[j] = false;
    GeneralMinimum = N;
    ChartCount = 0;
    for (int j = 0; j < 100; j++)
      Chart[j].clear();

    cout << "Case #" << i + 1 << ": " << Solve( 0 ) << endl;
  }

  return 0;
}


