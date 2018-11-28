#include <cstdio>
#include <cstring>

using namespace std;

int a[101*101], u[101*101], seen[101*101];

int parent(int v) {
  if (u[v] == v) return v;
  return u[v] = parent(u[v]);
}

void merge(int v, int w) {
  u[parent(v)] = parent(w);
}

int main() {
  int t; scanf("%d", &t);
  for(int i=1; i<=t; ++i) {
    int h, w; scanf("%d%d", &h, &w);
    for(int j=0; j<h; ++j) {
      for(int k=0; k<w; ++k) {
	scanf("%d", &a[w*j+k]);
	u[w*j+k] = w*j+k;
      }
    }
    for(int j=0; j<h; ++j) {
      for(int k=0; k<w; ++k) {
	int dx[] = {0,-1,1,0};
	int dy[] = {-1,0,0,1};
	int where = -1;
	for(int ii=0; ii<4; ++ii) {
	  int y = j+dy[ii], x = k+dx[ii];
	  if (y >= 0 && y < h && x >= 0 && x < w) {
	    if (a[w*y+x] < a[w*j+k]) {
	      if (where == -1 || a[where] > a[w*y+x]) {
		where = w*y+x;
	      }
	    }
	  }
	}
	if (where != -1) {
	  merge(w*j+k, where);
	}
      }
    }
    memset(seen, 0, sizeof(seen));
    printf("Case #%d:\n", i);
    for(int j=0, ii=0; j<h; ++j) {
      for(int k=0; k<w; ++k) {
	if (k) putchar(' ');
	int v = parent(w*j+k);
	if (!seen[v]) {
	  seen[v] = ++ii;
	}
	putchar('a'+seen[v]-1);
      }
      putchar('\n');
    }
  }
}
