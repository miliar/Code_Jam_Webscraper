#include <stdio.h>
#include <stdlib.h>

struct Row {
  char items[41];
  int count;
};

int dimen;
Row *matrix[40];

int main(void) {
  int cC, nC;

  scanf("%d", &nC);
  for (cC = 0; cC < nC; cC++) {
    scanf("%d", &dimen);
    for (int i = 0; i < dimen; i++)
      matrix[i] = new Row();
    
    for (int i = 0; i < dimen; i++) {
      scanf("%s", matrix[i]->items);
      matrix[i]->count = 0;
      for (int j = 0; j < dimen; j++) {
        if (matrix[i]->items[j] == '1') matrix[i]->count = j;
      }
    }

    int swaps = 0;
    for (int i = 0; i < dimen; i++) {
      if (matrix[i]->count > i) {
        // We need to find the next row that can live here.
        int row_num = -1;
        for (int j = i + 1; j < dimen; j++) {
          if (matrix[j]->count <= i) {
            row_num = j;
            break;
          }
        }
        swaps += (row_num - i);
        Row *temp = matrix[row_num];
        for (int j = row_num - 1; j >= i; j--)
          matrix[j + 1] = matrix[j];
        matrix[i] = temp;
      }
    }

    printf("Case #%d: %d\n", cC + 1, swaps);
  }
  return 0;
}
