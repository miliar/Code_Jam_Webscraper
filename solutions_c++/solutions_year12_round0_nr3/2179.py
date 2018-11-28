#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <algorithm>
using namespace std;

#define MAX 2000000
#define MAX_ANS 8000000

struct pair
{
  int n, r;
  bool operator<(const pair &o) const {
	if (n != o.n) return n < o.n;
	return r < o.r;
  }
  bool operator==(const pair &o) const {
	return n == o.n && r == o.r;
  }
} P[MAX_ANS];
int ans_num = 0;

int count(int n)
{
  if (n >= 1000000) return 7;
  if (n >= 100000) return 6;
  if (n >= 10000) return 5;
  if (n >= 1000) return 4;
  if (n >= 100) return 3;
  if (n >= 10) return 2;
  return 1;
}

void update(int n, int r)
{
  P[ans_num].n = n;
  P[ans_num].r = r;
  ++ans_num;
}

void init()
{
  int p[] = {1,10,100,1000,10000,100000,1000000};
  for (int n = 0; n <= MAX; ++n) {
	int nc = count(n);
	for (int i = 1; i < nc; ++i) {
	  int r = n/p[i] + (n%p[i])*p[nc-i];
	  if (r > n) {
		update(n,r);
	  }
	}
  }
  sort(P, P+ans_num);
  ans_num = unique(P, P+ans_num) - P;
}

int calc(int A, int B)
{
  int res = 0;
  for (int i = 0; i < ans_num; ++i) {
	if (P[i].n >= A) {
	  if (P[i].r <= B) {
		++res;
	  }
	  if (P[i].n > B) {
		break;
	  }
	}
  }
  return res;
}

int main(int argc, char *argv[])
{
  init();
  int T, c, A, B;
  scanf("%d", &T);
  for (c = 1; c <= T; ++c) {
	scanf("%d%d", &A, &B);
	printf("Case #%d: %d\n", c, calc(A, B));
  }
  
  return 0;
}
