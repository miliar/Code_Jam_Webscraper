#include <cstdio>

char t[60][60];
int n, k;

bool test1(int i, int j)
{
  for (int q = 1; q < k; q++)
    if (t[i][j] != t[i][j+q])
      return false;
//  printf("True1\n");
  return true;
}

bool test2(int i, int j)
{
  for (int q = 1; q < k; q++)
    if (t[i][j] != t[i+q][j])
      return false;
//  printf("True2\n");
  return true;
}

bool test3(int i, int j)
{
  for (int q = 1; q < k; q++)
    if (t[i][j] != t[i+q][j+q])
      return false;
//  printf("True3\n");
  return true;
}

bool test4(int i, int j)
{
  for (int q = 1; q < k; q++)
    if (t[i][j] != t[i-q][j+q])
      return false;
//  printf("True4\n");
  return true;
}

int main()
{
  int teste;
  scanf("%d\n", &teste);
  for (int T = 1; T <= teste; T++)
  {
    bool red = false, blue  = false;
    scanf("%d %d\n", &n, &k);
    for (int i = 0; i < n; i++)
    {
      scanf("%s\n", t[i]);
      //printf("%s\t", t[i]);
      int j = n-1;
      int pos = 0;

      while (j >= 0 && t[i][j] != '.')
      {
        j--;
      }
      while (j >= 0)
      {
        while (t[i][j] == '.')
          j--, pos++;

        while (j >= 0 && t[i][j] != '.')
        {
          t[i][j+pos] = t[i][j];
          t[i][j] = '.';
          j--;
        }

        j--;
        pos++;
      }
      //printf("%s\n", t[i]);
    }
    
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
      {
        if (t[i][j] != '.')
        {
          if ((j+k <= n && test1(i,j)) || (i+k <= n && test2(i,j)) || (i+k <= n && j+k <= n && test3(i,j)) || (i-k >= -1 && j+k <= n && test4(i,j)))
          {
            if (t[i][j] == 'R')
              red = true;
            else
              blue = true;
          }
        }
      }
    
    printf("Case #%d: ", T);
    if (red && blue)
      printf("Both\n");
    else if (!red && !blue)
      printf("Neither\n");
    else if (red)
      printf("Red\n");
    else
      printf("Blue\n");
    //printf("\n");
  }
  return 0;
}

