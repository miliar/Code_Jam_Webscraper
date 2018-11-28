#include <stdio.h>


const int MAXN = 1024;

int rides;
int size;
int n;
int group[MAXN];

int first[MAXN];
int rgap[MAXN];
long long sval[MAXN];
long long rval[MAXN];



int main() {

  int ncases;
  scanf("%d", &ncases);

  for(int ittr = 0; ittr < ncases; ++ittr) {
    scanf("%d %d %d", &rides, &size, &n);
    for(int j = 0; j < n; ++j) {
      scanf("%d", &group[j]);
    }

    for(int i = 0; i < n; ++i) {
      first[i] = -1;
      rgap[i] = -1;
    }

    long long v = 0;
    int p = 0;
    int i = 0;
    while(i < rides) {
      if(first[p] != -1 && rgap[p] == -1) {
	rgap[p] = i - first[p];
	rval[p] = v - sval[p];
      } else if(first[p] == -1) {
	first[p] = i;
	sval[p] = v;
      }
      if(rgap[p] != -1 && rides - i >= rgap[p]) {
	int q = (rides - i) / rgap[p];
	v += rval[p] * q;
	i += rgap[p] * q;
      } else {
	int c = 0;
	int in_car = 0;
	int p2 = p;
	while(in_car < n && c + group[p2] <= size) {
	  c += group[p2];
	  v += group[p2];
	  ++in_car;
	  p2 = (p2+1)%n;
	}
	p = p2;
	//printf("i = %d, c = %d, in_car = %d\n", i, c, in_car);
	++i;
      }
    }

    printf("Case #%d: %lld\n", ittr+1, v);
  }


  return(0);
}
