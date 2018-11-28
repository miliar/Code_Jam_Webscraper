#include <cstdio>
#include <cstdlib>
#include <vector>

int main()
{
  char const pattern[] = "welcome to code jam";
  int const lp = strlen(pattern);
  int N;
  scanf("%d", &N);
  char str[10000];
  fgets(str, 10000, stdin);
  for(int i=1; i<=N; ++i) {
    fgets(str, 10000, stdin);
    int const ls = strlen(str);
    std::vector<int> first, second;
    first.resize(ls);
    if(pattern[0] == str[0])
      first[0] = 1;
    for(int j=1; j<ls; ++j)
      first[j] = first[j-1] + (pattern[0] == str[j]);
    for(int k=1; k<lp; ++k) {
      second.resize(ls);
      for(int j=1; j<ls; ++j) {
	second[j] = second[j-1];
	if(pattern[k] == str[j])
	  second[j] += first[j-1];
	second[j] %= 10000;
      }
      first = second;
      second.clear();
    }
    printf("Case #%d: %04d\n", i, first.back());
  }
  return 0;
}
