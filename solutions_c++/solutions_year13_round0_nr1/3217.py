#include <stdio.h>
#include <assert.h>

using namespace std;


static const char *sentence[] = {
  "O won",
  "X won",
  "Draw",
  "Game has not completed"
};

static int process(const char *tab, bool ongoing)
{
  // for (int i = 0; i < 16; i++)
  //   printf("%d ",tab[i]);

  int sum;
  for (int i = 0; i < 4; i++) {
    sum = tab[4*0 + i] + tab[4*1 + i] + tab[4*2 + i] + tab[4*3 + i];
    if (sum >= 10)
      continue;
    if (sum <= 1)
      return 0;
    if (sum >= 7)
      return 1;
  }

  for (int i = 0; i < 4; i++) {
    sum = tab[4*i + 0] + tab[4*i + 1] + tab[4*i + 2] + tab[4*i + 3];
    if (sum >= 10)
      continue;
    if (sum <= 1)
      return 0;
    if (sum >= 7)
      return 1;
  }

  sum = tab[0] + tab[5] + tab[10] + tab[15];
  if (sum < 10) {
    if (sum <= 1)
      return 0;
    if (sum >= 7)
      return 1;
  }

  sum = tab[3] + tab[6] + tab[9] + tab[12];
  if (sum < 10) {
    if (sum <= 1)
      return 0;
    if (sum >= 7)
      return 1;
  }

  if (!ongoing)
    return 2;

  return 3;
}




int main(int argc, const char *argv[])
{
  if (argc != 2)
    return 1;
  const char *filename = argv[1];

  FILE *f = fopen(filename, "r");
  if (f == NULL)
    return 2;

  int nb_test;
  fscanf(f, "%d", &nb_test);

  for (int i = 0; i < nb_test; i++) {
    bool ongoing = false;
    char a;
    char tab[16];
    int j = 0;
    while (j != 16) {
      fscanf(f, "%c", &a);
      switch (a) {
      case 'X': tab[j] = 2; j++; break;
      case 'T': tab[j] = 1; j++; break;
      case 'O': tab[j] = 0; j++; break;
      case '.': tab[j] = 10; j++; ongoing = true; break;
      case '\n': break;
      default: assert(false);
      }
    }

    printf("Case #%d: %s", i + 1, sentence[process(tab, ongoing)]);
    printf("\n");
  }


  return 0;
}
