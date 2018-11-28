#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
using namespace std;
#define N 50010
#define M 1000000007

char s[N];
int k, p[N];
int count_rle(char *s, int len, int p[], int k)
{
	char last = 0;
	int c = 0;
 	for(int i = 0; i < len / k; i++)
 		for(int j = 0; j < k; j++) {
 			if(s[i*k+p[j]] != last) {
 				++c;
 				last = s[i*k+p[j]];
 			}
		}
	return c;
}

int main()
{
  int t, index, i, r, rm, res;
  
  scanf("%d", &t);
  for(index = 1; index <= t; index++) {
    scanf("%d%s", &k, s);
    int len = strlen(s);
	for(i = 0; i < k; i++)
		p[i] = i;
	rm = count_rle(s, len, p, k);
	while(next_permutation(p, p+k)) {
		r = count_rle(s, len, p, k);
		if(r < rm)
			rm = r;
	}
    printf("Case #%d: %lld\n", index, rm);
  }
}
