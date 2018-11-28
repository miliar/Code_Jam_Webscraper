#include <cstdio>
#include <cstring>

char dict[5000][16];

bool possible(const char *word, int index, int word_len) {
  int curr_index = 0;
  for (int i = 0; i < word_len; i++) {
    char to_find = dict[index][i];
    if (word[curr_index] != '(' && to_find != word[curr_index]) {
      return false;
    } else if (to_find == word[curr_index]) {
      curr_index++;
      continue;
    } else {
      curr_index++;
      while (word[curr_index] != ')') {
        if (word[curr_index] == to_find) break;
        curr_index++;
      }
      if (word[curr_index] == ')') return false;
      while (word[curr_index] != ')') curr_index++;
      curr_index++;
    }
  }
  if (word[curr_index] != '\0') {
    fprintf(stderr, "Warning, we didn't end at NULL! Saying not match.\n");
    return false;
  }
  return true;
}

int main(void) {
  int word_len, dict_size;
  int nC, cC;
  char word[15 * 28 + 1000];

  scanf("%d%d%d", &word_len, &dict_size, &nC);
  for (int i = 0; i < dict_size; i++)
    scanf("%s", dict[i]);
  for (cC = 0; cC < nC; cC++) {
    scanf("%s", word);
    int match = 0;
    for (int i = 0; i < dict_size; i++) {
      if (possible(word, i, word_len))
        match++;
    }
    printf("Case #%d: %d\n", cC + 1, match);
  }
  return 0;
}
