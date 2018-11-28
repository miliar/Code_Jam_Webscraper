#include <iostream>
#include <stdio.h>
#define MAXLIST 1000
using namespace std;

int elementsList[MAXLIST], listLength; // Ordered list of elements
int elements[26];  // A count of current elements
int combineMat[26][26];   // Matrix of combinations
int opposeMat[26][26];    // Matrix of opposing characters
char curr, prev;

// Sets curr and prev to -1, emptys list
void clearList();
// Resets matrices and lists
void reset();
// Combines curr with prev if possible.  Returns 1 on combine.
int combine();
// Returns 1 if reduce occurred
int reduce();
// Prints list
void printList();
int main() {
  int T,C,D,N;
  cin >> T;
  for (int i = 0; i < T; i++) {
    reset();
    cin >> C;
    for (int j = 0; j < C; j++) {
      char b1, b2, prod;
      cin >> b1 >> b2 >> prod;
      b1 -= 'A';
      b2 -= 'A';
      prod -= 'A';
      combineMat[b1][b2] = prod;
      combineMat[b2][b1] = prod;
    }
    cin >> D;
    for (int j = 0; j < D; j++) {
      char b1, b2;
      cin >> b1 >> b2;
      b1 -= 'A';
      b2 -= 'A';
      opposeMat[b1][b2] = 1;
      opposeMat[b2][b1] = 1;
    }
    cin >> N;
    for (int j = 0; j < N; j++) {
      cin >> curr;
      curr -= 'A';
      elements[curr]++;
      elementsList[listLength++] = curr;
      while (combine())
	combine();
      reduce();
      prev = curr;
    }
    printf("Case #%d: ", i+1);
    printList();
  }
}

int combine() {
  if (prev == -1) return 0; // cannot combine
  int product = combineMat[prev][curr];
  if (product != -1) {
    // FREEREWARD FOR FIXING THESE BUGS
    elements[curr]--;
    elements[prev]--;
    elements[product]++;

    listLength--;
    elementsList[listLength-1] = product;
    curr = product;
    if (listLength > 1)
      prev = elementsList[listLength-2];
    else
      prev = -1;	
    return 1;
  }
  return 0;
}

int reduce() {
  if (prev == -1) return 0;
  for (int i = 0; i < 26; i++) {
    if (elements[i] && opposeMat[i][curr]) {
      clearList();
      return 1;
    }
  }
  return 0;
}

void clearList() {
  curr = prev = -1;
  listLength = 0;
  for (int i = 0; i < 26; i++)
    elements[i] = 0;
}
void reset() {
  clearList();
  for (int i = 0; i < 26; i++) {
    for (int j = 0; j < 26; j++) {
      opposeMat[i][j] = 0;
      combineMat[i][j] = -1;
    }
  }
}

void printList() {
  printf("[");
  for (int i = 0; i < listLength-1; i++)
    printf("%c, ", elementsList[i]+'A');
  if (listLength > 0)
    printf("%c", elementsList[listLength-1]+'A');
  printf("]\n");
}
