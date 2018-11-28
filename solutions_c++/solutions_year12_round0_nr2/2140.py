#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
using namespace std;

int normal_max[31];
int surprising_max[31];

int fk(int i, int j, int k)
{
  int res = 0;
  if (abs(i-j) > res) {
	res = abs(i-j);
  }  
  if (abs(i-k) > res) {
	res = abs(i-k);
  }  
  if (abs(j-k) > res) {
	res = abs(j-k);
  }
  return res;
}

void calc(int n)
{
  for (int i = 0; i <= n && i <= 10; ++i) {
	for (int j = i-2>=0? i-2: 0;
		 i+j <= n && j <= 10 && j <= i+2;
		 ++j) {
	  int k = n-i-j;
	  int f = fk(i, j, k);
	  if (f == 0 || f == 1) {
		int m = max(max(i,j),k);
		if (m > normal_max[n]) normal_max[n] = m;
	  } else if (f == 2) {
		int m = max(max(i,j),k);
		if (m > surprising_max[n]) surprising_max[n] = m;
	  }
	}
  }
}

void init()
{
  memset(normal_max, 0x00, sizeof(normal_max));
  memset(surprising_max, 0x00, sizeof(surprising_max));

  for (int i = 1; i < 31; ++i) {
	calc(i);
	// printf("%d: %d, %d\n", i, normal_max[i], surprising_max[i]);
  }
}

int main(int argc, char *argv[])
{
  init();

  int T, c;
  scanf("%d", &T);
  for (c = 1; c <= T; ++c) {
	int N, S, p, t;
	scanf("%d%d%d", &N, &S, &p);
	int ans = 0, surprising = 0;
	
	for (int i = 0; i < N; ++i) {
	  scanf("%d", &t);
	  if (normal_max[t] >= p) {
		++ans;
	  } else if (surprising_max[t] >= p) {
		++surprising;
	  }
	}
	ans += min(surprising, S);
	printf("Case #%d: %d\n", c, ans);
  }
  return 0;
}
