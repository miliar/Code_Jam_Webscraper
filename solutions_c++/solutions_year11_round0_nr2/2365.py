#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <vector>
#include <string>

using namespace std;

const int MAX = 26;
char combine[MAX][MAX];
bool oppose[MAX][MAX];
const int MAX_LEN = 110;
int n;
char list[MAX_LEN];
int m;
char newlist[MAX_LEN];

void clearall()
{
  for (int i = 0; i < MAX; i++)
  {
    for (int j = 0; j < MAX; j++)
    {
      combine[i][j] = 0;
      oppose[i][j] = false;
    }
  }
}

void readinput()
{
  int qty;
  char comb[4];
  scanf("%d", &qty);
  for (int i = 0; i < qty; i++)
  {
    scanf("%s", comb);
    int j = comb[0] - 'A';
    int k = comb[1] - 'A';
    char c = comb[2];
    combine[j][k] = combine[k][j] = c;
    //printf("c %d %d\n", j, k);
  }
  scanf("%d", &qty);
  for (int i = 0; i < qty; i++)
  {
    scanf("%s", comb);
    int j = comb[0] - 'A';
    int k = comb[1] - 'A';
    oppose[j][k] = oppose[k][j] = true;
    //printf("o %d %d\n", j, k);
  }
  scanf("%d %s", &n, list);
  //printf("%d %s\n", n, list);
}

void process()
{
  m = 0;
  for (int i = 0; i < n; i++)
  {
    newlist[m++] = list[i];
    // check if combine
    if (m > 1)
    {
      int a = newlist[m-1] - 'A';
      int b = newlist[m-2] - 'A';
      if (combine[a][b])
      {
        newlist[m-2] = combine[a][b];
        m--;
      }
    }
    // check if oppose
    int a = newlist[m-1] - 'A';
    for (int j = 0; j < m-1; j++)
    {
      int b = newlist[j] - 'A';
      if (oppose[a][b])
      {
        m = 0;
        break;
      }
    }
  }
  newlist[m] = '\0';
  //printf("%d %s\n", m, newlist);
}

void printoutput(int testcase)
{
  printf("Case #%d: [", testcase);
  for (int i = 0; i < m; i++)
  {
    if (i > 0) printf(", ");
    printf("%c", newlist[i]);
  }
  printf("]\n");
}

int main()
{
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; test++)
  {
    clearall();
    readinput();
    process();
    printoutput(test);
  }
  return 0;
}
