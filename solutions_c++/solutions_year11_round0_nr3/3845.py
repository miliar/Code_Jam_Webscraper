#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

using namespace std;

long c[1000];
unsigned long max_value = 0;

void combine(int n)
{
  for (int s = 1; s < (1 << (n - 1)); ++s) {
    int a = 0, b = 0;
    int x = 0, y = 0;
    for (int i = 0, k = s; i < n; ++i, k >>= 1) {
      if ((k & 1) != 0) {
        a += c[i];
        x ^= c[i];
      }
      else {
        b += c[i];
        y ^= c[i];
      }
    }
    if (x == y && max(a, b) > max_value)
      max_value = max(a, b);
  }
}

void solve(int N)
{
  max_value = 0;
  //perm(0, N-1);
  combine(N);
  if(max_value == 0)
    cout<<"NO";
  else
    cout<<max_value;
}

int main(int argc,char **args)
{
	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
	int testcase;
  cin>>testcase;
	for (int caseId=1;caseId<=testcase; caseId++)
	{
		printf("Case #%d: ",caseId);
    int N = 0;
    cin>>N;
    for(int i=0; i<N; ++i)
      cin>>c[i];
    
    solve(N);
    printf("\n");
		fflush(stdout);
	}
	return 0;
}