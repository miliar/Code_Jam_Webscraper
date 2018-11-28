#include <iostream>
#include <string>

using namespace std;

int Height, Width;
int Map[100][100];

int ParentDeltaX[100][100];
int ParentDeltaY[100][100];

int DeltaX[4] = {0, -1, 1, 0};
int DeltaY[4] = {-1, 0, 0, 1};

char Label[100][100];
bool HasLabel[100][100];

void FindParents()
{
  for (int y = 0; y < Height; y++)
    for (int x = 0; x < Width; x++)
    {
      int dX = 0;
      int dY = 0;
      for (int k = 0; k < 4; k++)
        if ((x + DeltaX[k] >= 0) && (x + DeltaX[k] < Width) && (y + DeltaY[k] >= 0) && (y + DeltaY[k] < Height))
          if (Map[y + dY][x + dX] > Map[y + DeltaY[k]][x + DeltaX[k]])
          {
            dX = DeltaX[k];
            dY = DeltaY[k];
          }

      ParentDeltaX[y][x] = dX;
      ParentDeltaY[y][x] = dY;
    }
}

char LastUnusedLabel;

char FindALabel( int y, int x )
{
  if (HasLabel[y][x])
    return Label[y][x];

  char CurLabel;
  if ((ParentDeltaX[y][x] == 0) && (ParentDeltaY[y][x] == 0))
  {
    CurLabel = LastUnusedLabel;
    LastUnusedLabel++;
  }
  else
    CurLabel = FindALabel( y + ParentDeltaY[y][x], x + ParentDeltaX[y][x] );

  HasLabel[y][x] = true;
  Label[y][x] = CurLabel;

  return CurLabel;
}

void FindLabels()
{
  for (int i = 0; i < Height; i++)
    for (int j = 0; j < Width; j++)
      HasLabel[i][j] = false;
  LastUnusedLabel = 'a';

  for (int i = 0; i < Height; i++)
    for (int j = 0; j < Width; j++)
      FindALabel( i, j );
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++)
  {
    cin >> Height >> Width;
    for (int j = 0; j < Height; j++)
      for (int k = 0; k < Width; k++)
        cin >> Map[j][k];

    FindParents();
    FindLabels();

    cout << "Case #" << i + 1 << ":" << endl;
    for (int j = 0; j < Height; j++)
    {
      for (int k = 0; k < Width; k++)
      {
        if (k > 0)
          cout << " ";
        cout << Label[j][k];
      }
      cout << endl;
    }
  }
  return 0;
}

