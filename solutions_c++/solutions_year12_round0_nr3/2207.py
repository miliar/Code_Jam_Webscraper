#include <cstdio>
#include <cstring>
using namespace std;
const int MAXL = 7;
const int MAXN = 2000000;
const int MAXH = 1000000;

char znam[MAXL+1];
int L10[8] = {1, 1, 10, 100, 1000, 10000, 100000, 1000000};

int bio[MAXN+1];

int main()
{
  int T; scanf("%d\n", &T);
  for( int t_case = 0; t_case < T; ++t_case ) {
    int A, B; scanf("%d%d", &A, &B);

    int sol = 0;

    memset(bio, 0, sizeof(bio));
    for(int i = A; i <= B; ++i) {
      int x = i, l = 0; 
      for( ; x > 0; x = x / 10, ++l)
	znam[l] = x % 10;

      // okrecem da mi bude lakse razmisljati
      for(int j = 0; 2 * j < l; ++j) {
	int tmp = znam[j];
	znam[j] = znam[l-j-1];
	znam[l-j-1] = tmp;
      }

      // mogu izbaciti MOD
      for(int j = 1; j < l; ++j) {
	int novi = 0;
	for(int k = 0; k < l; ++k)
	  novi = novi * 10 + znam[(j+k)%l];
	
	if (A <= novi && novi < i && L10[l] <= novi && bio[novi] != i) {
	  ++sol;
	  bio[novi] = i;
	}
      }
    }

    printf( "Case #%d: %d\n", t_case + 1, sol);
  }
  return 0;
}
