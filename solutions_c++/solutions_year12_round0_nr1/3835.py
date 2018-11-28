#include <stdio.h>
#include <string.h>

char assoc[] = {
  'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'
};

int main() {
  char str[1024];
  int n;
  scanf("%d", &n);
  gets(str); // Stupid newlines
  for (int i = 0; i < n; i++) {
    gets(str);
    for (int j = 0; j < strlen(str); j++) {
      if (str[j] <= 'z' && str[j] >= 'a') {
        str[j] = assoc[str[j] - 'a'];
      }
    }
    printf("Case #%d: %s\n", i + 1, str);
  }
}
