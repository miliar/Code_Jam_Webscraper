#include <cstdio>
#include <set>

int count_digits(int x)
{
  int digits = 0;
  while(x) {
    ++digits;
    x /= 10;
  }
  return digits;
}

int log[] = { 0,
	      1,
	      10,
	      100,
	      1000,
	      10000,
	      100000,
	      1000000,
	      10000000,
	      100000000,
	      1000000000 };
int main()
{
  int T;
  scanf("%d", &T);
  for(int cs=1; cs<=T; ++cs) {
    int A, B;
    scanf("%d%d", &A, &B);
    std::set<std::pair<int, int> > s;
    for(int x=A; x<=B; ++x) {
      int digits = count_digits(x);
      int y = x;
      for(int i=1; i<digits; ++i) {
	int d = y%10;
	y /= 10;
	y += d * log[digits];
	if(d && y >= A && y <= B && x != y)
	  s.insert(std::make_pair(std::min(x, y), std::max(x, y)));
      }
    }
    printf("Case #%d: %lu\n", cs, s.size());
  }
  return 0;
}
