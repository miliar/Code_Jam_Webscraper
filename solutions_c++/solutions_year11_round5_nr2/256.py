/*
ID: azhai1
LANG: C++
TASK: dire_straights
*/

#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

void init();

FILE *in  = fopen ("dire_straights.in", "r");
FILE *out = fopen ("dire_straights.out", "w");

const int NUM_MAX = 10032;
int N;
int cards[NUM_MAX];
int extendable[NUM_MAX];

bool can_achieve(int size) {  
  printf("trying size %d\n", size);

  int cards_copy[NUM_MAX];
  //  memcpy(cards_copy, cards, sizeof(cards));

  for (int i = 0; i < NUM_MAX; i++) {
    cards_copy[i] = cards[i];
    extendable[i] = 0;
  }

  for (int cursor = 0; cursor < NUM_MAX; cursor++) {
    if (!cards_copy[cursor])
      continue;

    //    printf("scanning %d\n", cursor);

    if (cards_copy[cursor] < extendable[cursor])
      extendable[cursor] = cards_copy[cursor];
    extendable[cursor + 1] += extendable[cursor];
    cards_copy[cursor] -= extendable[cursor];
    int num_needed = cards_copy[cursor];
    for (int i = cursor; i < cursor + size; i++) {
      if (cards_copy[i] < num_needed)
	return false;
      cards_copy[i] -= num_needed;
    }
    extendable[cursor + size] += num_needed;
  }
  return true;
}

int binary_search(int lower, int upper) {
  if (lower == upper)
    return lower;

  int mid = (upper + lower + 1) / 2;

  if (can_achieve(mid)) {
    //    printf("can achieve %d\n", mid);
    return binary_search(mid, upper);
  }

  //  printf("can't achieve %d\n", mid);
  return binary_search(lower, mid - 1);
}

int main() {
  int T;
  fscanf(in, "%d\n", &T);



  for (int t = 0; t < T; t++) {
    printf("Working on case %d\n", t + 1);

    init();

    if (N == 0) {
      fprintf(out, "Case #%d: 0\n", t + 1);
      continue;
    }

    int answer = binary_search(1, N);
    fprintf(out, "Case #%d: %d\n", t + 1, answer);
  }

  return 0;
}

void init() {
  fscanf(in, "%d ", &N);

  for (int i = 0; i < NUM_MAX; i++) {
    cards[i] = 0;
  }

  for (int i = 0; i < N; i++) {
    int card;
    fscanf(in, "%d ", &card);
    cards[card]++;
  }

  fscanf(in, "\n");
}

