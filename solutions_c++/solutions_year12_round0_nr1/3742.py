#include <iostream>
#include <cassert>

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  char * p[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

  char * q[] = {"our language is impossible to understand",
                "there are twenty six factorial possibilities",
                "so it is okay if you want to just give up"};

  char map[128];
  for(size_t i = 0; i < sizeof(map) / sizeof(map[0]); ++i)
    map[i] = i;

  for(size_t i = 0; i < 3; ++i)
    for(size_t j = 0, n = ::strlen(p[i]); j < n; ++j)
      map[p[i][j]] = q[i][j];

  map['z'] = 'q';
  map['q'] = 'z';

  for(size_t i = 'a'; i <= 'z'; ++i)
    assert(map[i] != i);

  assert(map['y'] == 'a');
  assert(map['e'] == 'o');
  assert(map['q'] == 'z');

  int tests = 0;
  std::cin >> tests;
  char sz[1024];
  std::cin.getline(sz, sizeof(sz) / sizeof(sz[0]));
  for(int test = 1; test <= tests; ++test)
  {
    std::cin.getline(sz, sizeof(sz) / sizeof(sz[0]));

    for(size_t i = 0, n = ::strlen(sz); i < n; ++i)
      sz[i] = map[sz[i]];

    std::cout << "Case #" << test << ": " << sz << std::endl;
  }

  return 0;
}