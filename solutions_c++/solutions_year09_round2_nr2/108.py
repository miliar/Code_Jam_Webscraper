#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;

typedef long long int huge;
const int inf=0x3f2f1f0f;
const huge hinf=0x3fff2fff1fff0fffll;

#define foreach(i...) _foreach(i)
#define all(v) v.begin(), v.end()
#define _foreach(i, b, e) for(__typeof(b) i=b; i!=e; i++)

int main()
{
  int test;
  vector<int> v;
  char num[256];
  scanf(" %d", &test);
  for(int z=1; z<=test; ++z)
    {
      v.clear();
      v.push_back(0);
      scanf(" %s", num);
      for(int i=0; num[i]; ++i)
	v.push_back(num[i]-'0');
      next_permutation(all(v));
      printf("Case #%d: ", z);
      if (v[0])
	printf("%d", v[0]);
      for(int i=1; i<v.size(); ++i)
	printf("%d", v[i]);
      printf("\n");
    }
  return 0;
}
