#include <iostream>

using namespace std;

int mas1[1000][2];
int mas2[1000][2];
int col1, col2;

int parse(char *s)
{
  return ((s[0] - 48) * 10 + s[1] - 48) * 60 + (s[3] - 48) * 10 + s[4] - 48;
}

void sort1()
{
  int i, j, tmp;

  for (i = 0; i < col1 + col2; i++)
    for (j = i + 1; j < col1 + col2; j++)
      if (mas1[i][0] > mas1[j][0] || (mas1[i][0] == mas1[j][0] && mas1[i][1] > mas1[j][1]))
      {
        tmp = mas1[i][0];
        mas1[i][0] = mas1[j][0];
        mas1[j][0] = tmp;

        tmp = mas1[i][1];
        mas1[i][1] = mas1[j][1];
        mas1[j][1] = tmp;
      }
}

void sort2()
{
  int i, j, tmp;

  for (i = 0; i < col1 + col2; i++)
    for (j = i + 1; j < col1 + col2; j++)
      if (mas2[i][0] > mas2[j][0] || (mas2[i][0] == mas2[j][0] && mas2[i][1] > mas2[j][1]))
      {
        tmp = mas2[i][0];
        mas2[i][0] = mas2[j][0];
        mas2[j][0] = tmp;

        tmp = mas2[i][1];
        mas2[i][1] = mas2[j][1];
        mas2[j][1] = tmp;
      }
}

int main()
{
  int i, j, t, test, tt, tmp, ans1, ans2, mm;
  char s1[100], s2[100];

  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> test;

  for (tt = 0; tt < test; tt++)
  {
    cin >> t >> col1 >> col2;

    for (i = 0; i < col1; i++)
    {
      cin >> s1 >> s2;

      tmp = parse(s1);
      mas1[i][0] = tmp;
      mas1[i][1] = 1;

      tmp = parse(s2);
      mas2[i][0] = tmp + t;
      mas2[i][1] = -1;
    }

    for (i = 0; i < col2; i++)
    {
      cin >> s1 >> s2;

      tmp = parse(s1);
      mas2[i + col1][0] = tmp;
      mas2[i + col1][1] = 1;

      tmp = parse(s2);
      mas1[i + col1][0] = tmp + t;
      mas1[i + col1][1] = -1;
    }  

    sort1();
    sort2();

    /*for (i = 0; i < col1 + col2; i++)
      cout << mas1[i][0] << ' ' << mas1[i][1] << endl;
    
    cout << endl;
    for (i = 0; i < col1 + col2; i++)
      cout << mas2[i][0] << ' ' << mas2[i][1] << endl;*/

    ans1 = ans2 = 0;

    mm = 0;
    for (i = 0; i < col1 + col2; i++)
    {
      mm += mas1[i][1];
      if (mm > ans1)
        ans1 = mm;
    }

    mm = 0;
    for (i = 0; i < col1 + col2; i++)
    {
      mm += mas2[i][1];
      if (mm > ans2)
        ans2 = mm;
    }

    cout << "Case #" << tt + 1 << ": " << ans1 << ' ' << ans2 << endl;
  }

  return 0;
}