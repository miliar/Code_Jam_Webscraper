#include <cstdio>
#include <vector>
#include <string>

#define len(x) ((int)x.size())

using namespace std;

vector<string> names;

string getname(FILE *fin)
{
  char name[128];

  fgets(name, 120, fin);
  if (strlen(name) && name[strlen(name) - 1] == '\n') {
    name[strlen(name) - 1] = 0;
  }
  if (strlen(name) && name[strlen(name) - 1] == '\r') {
    name[strlen(name) - 1] = 0;
  }
  if (strlen(name) && name[strlen(name) - 1] == '\n') {
    name[strlen(name) - 1] = 0;
  }
  if (strlen(name) && name[strlen(name) - 1] == '\r') {
    name[strlen(name) - 1] = 0;
  }
  return string(name);
}

int findname(string name)
{
  for (int i = 0; i < len(names); ++i) {
    if (names[i] == name) {
      return i;
    }
  }
  return -1;
}

int n, s;
int v[1024];

int sol[1024][128];

const int infinity = 99999;

int solve()
{
  int answer = infinity;
  int minc[128];
  int mind[128];

  for (int i = 0; i < s; ++i) {
    if (v[0] == i) {
      sol[0][i] = infinity;
    } else {
      sol[0][i] = 0;
    }
  }
  for (int i = 1; i < n; ++i) {
    minc[0] = infinity;
    for (int j = 1; j < s; ++j) {
      minc[j] = min(minc[j - 1], sol[i - 1][j - 1]);
    }
    mind[s - 1] = infinity;
    for (int j = s - 2; j >= 0; --j) {
      mind[j] = min(mind[j + 1], sol[i - 1][j + 1]);
    }
    for (int j = 0; j < s; ++j) {
      sol[i][j] = min(minc[j], mind[j]) + 1;
      if (v[i] != j) {
	sol[i][j] = min(sol[i][j], sol[i - 1][j]);
      }
    }
  }
  if (n > 0) {
    for (int i = 0; i < s; ++i) {
      answer = min(answer, sol[n - 1][i]);
    }
  } else {
    answer = 0;
  }
  return answer;
}

int main()
{
  FILE *fin = fopen("test.in", "r");
  FILE *fout = fopen("test.out", "w");
  int tests;

  fscanf(fin, "%d\n", &tests);
  for (int test = 0; test < tests; ++test) {
    names.clear();
    fscanf(fin, "%d\n", &s);
    for (int i = 0; i < s; ++i) {
      string temp = getname(fin);
      names.push_back(temp);
    }
    fscanf(fin, "%d\n", &n);
    for (int i = 0; i < n; ++i) {
      string temp = getname(fin);
      v[i] = findname(temp);
    }
    fprintf(fout, "Case #%d: %d\n", test + 1, solve());
  }
  fclose(fin);
  fclose(fout);
}
