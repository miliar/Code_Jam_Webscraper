#include <stdio.h>
#include <string.h>

static const char* ref = "welcome to code jam";
static const int ref_length = 19;

const int line_length = 500;
static char line[line_length + 1];

static int numbers[ref_length][line_length];

int answer(char* line);

int main(int argc, char** argv) {
  int n;
  scanf("%d", &n);
  fgets(line, line_length + 1, stdin);
  for (int i = 1; i <= n; i++) {
    fgets(line, line_length + 1, stdin);
    printf("Case #%d: %04d\n", i, answer(line));


  }
  return 0;
}

int answer(char* line) {
  line = strchr(line, ref[0]);
  if (line == NULL) {
    return 0;
  }
  int length = strlen(line);
  if (line[length - 1] == '\n') {
    line[length - 1] = '\0';
    length--;
  }
  if (length < ref_length) {
    return 0;
  }
  memset(numbers, 0, line_length*ref_length);
  numbers[0][0] = 1;
  for (int j = 1; j < length; j++) {
    if (ref[0] == line[j]) {
      numbers[0][j] = (numbers[0][j-1] + 1) % 10000;
    } else {
      numbers[0][j] = numbers[0][j-1];
    }
  }
  for (int i = 1; i < ref_length; i++) {
    for (int j = 1; j < length; j++) {
      if (ref[i] == line[j]) {
        numbers[i][j] = (numbers[i][j-1] + numbers[i-1][j-1]) % 10000;
      } else {
        numbers[i][j] = numbers[i][j-1];
      }
    }
  }
  return numbers[ref_length - 1][length - 1];
}

