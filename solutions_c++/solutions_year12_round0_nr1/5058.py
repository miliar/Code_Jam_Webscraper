#include <stdio.h>

int main()
{
  char cifra[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q', 'Z'};
  char line [101];

  int i, n;
  scanf("%d", &n);
  for (i = 0; i < n; i++)
  {
    scanf(" %[^\n]", line);
    int j = 0;
    printf("Case #%d: ", i + 1);
    while (line[j] != '\0')
    {
      if (line[j] != ' ')
        printf("%c", cifra[line[j] - 'a']);
      else
        printf(" ");
      j++;
    }
    printf("\n");
  }

  return 0;
}

