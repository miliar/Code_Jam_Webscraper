
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

string words[10000];
string thingie;
int n, m;

int nletters[20];
int letters[20][10000];

unsigned int value[26][10000];
unsigned int depth[10000];

unsigned int mask;

string filter(string src) {
  string dst;
  for (size_t i = 0; i < src.size(); i++)
    if ((1 << (src[i] - 'a')) & mask)
      dst += src[i];
  return dst;
}

struct cmp {
  cmp(unsigned int _c) { c = _c; }

  bool operator()(const int& a, const int& b) {
    return value[c][a] < value[c][b];
  }

  unsigned int c;
};

const char* pick_letter(int* start, int* end, const char *str) {
  while (*str) {
    for (int *it = start; it != end; it++)
      if (value[str[0]-'a'][*it])
        return str;
    str++;
  }

  //cerr << "AAAAAAAAAAAAAAA" << endl;
  return NULL;
}

void my_sort(int* start, int *end, const char* str) {
  if (!*str) return;

  unsigned int c = *str -'a';
  //cerr << "derp1" << endl;
  sort(start, end, cmp(c));

  for (int* it = start; it != end; it++)
  {
    if (value[c][*it] == 0)
      depth[*it]++;
  }

  int *a = start;
  while (a != end) {
    int *b = a;
    while (b != end && value[c][*b] == value[c][*a])
      b++;

    //cerr << "from " << words[*a] << " (" << value[c][*a] << ") " << " to " << words[*b] << endl;
    if (b - a > 1)
      my_sort(a, b, pick_letter(a, b, str + 1));
      //my_sort(a, b, str+1);
    a = b;
  }

  //while (start < end) {
  //  cerr << "sorted by " << str[0] << ": " << words[*start++] << endl;
  //}
}

void solve(int CASE) {

  cin >> n >> m;
  memset(letters, 0, sizeof(letters));
  memset(nletters, 0, sizeof(nletters));
  memset(value, 0, sizeof(value));
  mask = 0;

  for (int i = 0; i < n; i++)
  {
    cin >> words[i];
    size_t w = words[i].size();
    letters[w][nletters[w]++] = i;

    for (size_t j = 0;  j < w; j++) {
      value[words[i][j] - 'a'][i] |=  (1 << j);
      mask |= 1 << (words[i][j] - 'a');
    }

    //for (int j = 0; j < 26; j++)
    //  cerr << "value " << j << " for " << words[i] << " is " << value[j][i] << endl;
  }

  printf("Case #%d:", CASE);
  for (int i = 0; i < m; i++)
  {
    cin >> thingie;
    memset(depth, 0, sizeof(depth));

    thingie = filter(thingie);
    //cerr << "thingie: " << thingie << endl;

    for (int j = 1; j <= 10; j++)
    {
      if (nletters[j] == 0) continue;
      if (nletters[j] == 1) { depth[letters[j][0]] = 0; continue; }

      my_sort(letters[j], letters[j] + nletters[j], thingie.c_str());
    }

    int maxe = 0;
    int maxv = depth[maxe];
    for (int i = 1; i < n; i++)
      if (depth[i] > maxv)
        maxv = depth[i], maxe = i;


    printf(" %s", words[maxe].c_str());
  }
  puts("");
}

int main()
{
  int n;
  cin >> n;
  for (int i = 1; i <= n; i++)
    solve(i);
  return 0;
}
