#include<cstdio>
#include<cassert>
#define infile "speaking.in"
#define outfile "speaking.out"
#define inExample "example.in"
#define outExample "example.out"
#define sigma 26
#define lgMax 10013

using namespace std;

char p[sigma];

bool valid(int x) {

  for(int i = 0; i < sigma; ++i) {
    if(p[i] == x + 'a')
      return false;
  }

  return true;
}

char getFree() {

  for(int i = 0; i < sigma; ++i) {
    if(valid(i))
      return i + 'a';
  }

  return 0;
}

void initialization() {

  p['y' - 'a'] = 'a';
  p['e' - 'a'] = 'o';
  p['q' - 'a'] = 'z';

  FILE *in = fopen(inExample, "r");
  FILE *out = fopen(outExample, "r");
  char a[lgMax], b[lgMax];
  int t;

  fscanf(in, "%d\n", &t);
  while(t--) {
    fgets(a, lgMax, in);
    fgets(b, lgMax, out);

    for(int i = 0; (a[i] >= 'a' && a[i] <= 'z') || a[i] == ' '; ++i) {
      if(a[i] >= 'a' && a[i] <= 'z')
        assert(p[a[i] - 'a'] == b[i] || p[a[i] - 'a'] == 0);
        p[a[i] - 'a'] = b[i];
    }
  }

  for(int i = 0; i < sigma; ++i) {
    if(p[i] == 0)
      p[i] = getFree();
  }
}

void solve(int test) {

  char str[lgMax];
  fgets(str, lgMax, stdin);

  for(int i = 0; (str[i] >= 'a' && str[i] <= 'z') || str[i] == ' '; ++i) {
    if(str[i] >= 'a' && str[i] <= 'z')
      str[i] = p[str[i] - 'a'];
  }

  printf("Case #%d: %s", test, str);
}

int main() {
  freopen(infile, "r", stdin);
  freopen(outfile, "w", stdout);

  initialization();

  int t;
  scanf("%d\n", &t);
  for(int test = 1; test <= t; ++test) {
    solve(test);
  }

  fclose(stdin);
  fclose(stdout);
  return 0;
}
