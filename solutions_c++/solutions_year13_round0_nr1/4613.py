#include <cstdio>
#include <cstring>

using namespace std;

int t;
char b[4][5];
int ilex1[4], ileo1[4], ilex2[4], ileo2[4], ilex3[2], ileo3[2];
bool dot;

int main()
{
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    for (int j = 0; j < 4; j++) scanf("%s", b[j]);
    dot = false;
    memset(ilex1, 0, sizeof(ilex1));
    memset(ilex2, 0, sizeof(ilex1));
    memset(ileo1, 0, sizeof(ilex1));
    memset(ileo2, 0, sizeof(ilex1));
    memset(ilex3, 0, sizeof(ilex3));
    memset(ileo3, 0, sizeof(ilex3));
    for (int j = 0; j < 4; j++)
    {
      for (int k = 0; k < 4; k++)
      {
        if (b[j][k] == 'X' || b[j][k] == 'T') ilex1[j]++, ilex2[k]++;
        if (b[j][k] == 'O' || b[j][k] == 'T') ileo1[j]++, ileo2[k]++;
        if (b[j][k] == '.') dot = true;
      }
      if (b[j][j] == 'X' || b[j][j] == 'T') ilex3[0]++;
      if (b[3-j][j] == 'X' || b[3-j][j] == 'T') ilex3[1]++;
      if (b[j][j] == 'O' || b[j][j] == 'T') ileo3[0]++;
      if (b[3-j][j] == 'O' || b[3-j][j] == 'T') ileo3[1]++;
    }
    bool xwin = false, owin = false;
    for (int j = 0; j < 4; j++)
    {
      if (ilex1[j] == 4 || ilex2[j] == 4 || (j < 2 && ilex3[j] == 4)) xwin = true;
      if (ileo1[j] == 4 || ileo2[j] == 4 || (j < 2 && ileo3[j] == 4)) owin = true;
    }
    printf("Case #%d: ", i+1);
    if (xwin) printf("X won\n");
    else if (owin) printf("O won\n");
    else if (dot) printf("Game has not completed\n");
    else printf("Draw\n");
  }
  return 0;
}
