#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cassert>
using namespace std;
#define max 500
#define sw 300
struct CM {
  long double i;
  long double j;
  long long w;
  CM(long double i = -1, long double j = -1, long long w = -1) : i(i), j(j), w(w) {}
  CM operator+(const CM other) const {
    CM ans;
    ans.w = w + other.w;
    ans.i = (w * i + other.w * other.i) / ans.w;
    ans.j = (w * j + other.w * other.j) / ans.w;
    return ans;
  }
};
const long double eps = 1e-16;

vector< vector< vector<CM> > > figures;
vector< vector< vector<CM> > > iLine;
vector< vector< vector<CM> > > jLine;
vector< vector<long long> > table;
int R, C, D;

CM ILine(int i, int j, int l) {
  if (i + l >= R || j >= C || l <= 0) {
    printf("oops\n");
    assert(0);
  }
  if (iLine[i][j][l].w == -1) {
    if (l == 1) {
      iLine[i][j][l] = CM(i, j, table[i][j]);
    }
    else {
      iLine[i][j][l] = ILine(i, j, l - 1) + ILine(i + l - 1, j, 1);
    }
  }
  return iLine[i][j][l];
}

CM JLine(int i, int j, int l) {
  if (j + l >= C || i >= R || l <= 0) {
    printf("oops\n");
    assert(0);
  }
  if (jLine[i][j][l].w == -1) {
    if (l == 1) {
      jLine[i][j][l] = CM(i, j, table[i][j]);
    }
    else {
      jLine[i][j][l] = JLine(i, j, l - 1) + JLine(i, j + l - 1, 1);
    }
  }
  return jLine[i][j][l];
}

CM figure(int i, int j, int size) {
  if (i + size > R || j + size > C || size < 2) {
    printf("oops\n");
    assert(0);
  }

  if (figures[i][j][size].w == -1) {
    if (size == 2) {
      figures[i][j][size] =  CM(i, j, 0);
    } else {
      figures[i][j][size] = figure(i, j, size - 1)  + JLine(i + size - 1, j + 1, size - 2) +  ILine(i + 1, j + size - 1, size - 2) +
	ILine(i + size - 2, j + size - 2, 1) + ILine(i + size - 2, j, 1) + ILine(i, j + size - 2, 1);
    }
  }
  return figures[i][j][size];
}

long double abs(long double x) {
  if (x > 0) {
    return x;
  }
  return -x;
}
int main() {
  int tN;
  scanf("%d", &tN);
  for (int testN = 1; testN <= tN; ++testN) {
    printf("Case #%d: ", testN);
    scanf("%d %d %d", &R, &C, &D);
    int size = min(C, R) + 3;
    figures = vector< vector< vector< CM > > >(R, vector< vector<CM> >(C, vector<CM>(size, CM())));
    iLine = vector< vector< vector< CM > > >(R, vector< vector<CM> >(C, vector<CM>(R, CM())));
    jLine = vector< vector< vector< CM > > >(R, vector< vector<CM> >(C, vector<CM>(C, CM())));
    table = vector< vector<long long> >(R, vector<long long>(C));

    char buf[1000];
    for (int i = 0; i < R; ++i) {
      scanf("%s", buf);
      string line(buf);
      for (int j = 0; j < C; ++j) {
	  table[i][j] = line[j] - '0' + D;
      }
    }
    int maxSize = 0;
    for (int s = 2; s < size; ++s) {
      for (int i = 0; i <= R - s; ++i) {
	for (int j = 0; j <= C - s; ++j) {	  
	  if (abs(figure(i,j,s).i - i - (s - 1.0) / 2) < eps && abs(figure(i,j,s).j - j - (s - 1.0) / 2) < eps) {
	    maxSize = s;
	  }
	}
      }
    }
    if (maxSize < 3) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", maxSize);
    }
  }
  return 0;
}
