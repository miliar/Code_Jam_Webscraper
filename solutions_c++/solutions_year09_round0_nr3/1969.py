#include<cstdio>
#include<cassert>
#include<cstring>

using namespace std;

const int P = 19;
const char pattern[] = "welcome to code jam";
const int MAX_R = 500;
const int MOD = 1000;

char text[MAX_R + 2];

int memo[P][MAX_R];

int go(int p, int r)
{
  if(text[r] == '\n')
    return 0;
  int &res = memo[p][r];
  if(res != -1)
    return res;
  res = go(p, r+1);
  if(pattern[p] == text[r])
    res = (res + go((p+1)%P, r+1) + (p == P-1)) % MOD;
  return res;
}

int main()
{
  int T;
  assert(scanf("%d\n", &T));
  for(int t = 1; t <= T; t++)
    {
      memset(memo, -1, sizeof(memo));
      assert(fgets(text, MAX_R+2, stdin));
      printf("Case #%d: %04d\n", t, go(0, 0));
    }
}
