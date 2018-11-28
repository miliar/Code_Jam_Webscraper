/* 
 * SOUR:
 * ALGO:
 * DATE: 2010年 05月 23日 星期日 01:13:22 CST
 * COMM:
 * */
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define size(x) ((int)x.size())
#define X first
#define Y second 
typedef vector < int >vi;
typedef pair < int, int >pii;
typedef long long LL;
template <class T> void ckmin(T &a,T b) { if (a > b) { a = b; } }
template <class T> void ckmax(T &a,T b) { if (a < b) { a = b; } }
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }

const int maxint = 0x7fffffff;
const long long max64 = 0x7fffffffffffffffll;
const int Debug = 1;
const int N = 512;
int ans = 0,n;

int num[N],top;
int a[N];
void init()
{
  ans = 0;
}

bool judge()
{
  int t = top - 1;

  for (int i = top - 2;i >= 1;i--) {
	  if (t == a[i]) {
		  t = i;
	  }
  }
  return t == 1;
}

int main()
{
  int i,j,testcase,testid = 1;
  scanf("%d",&testcase);
  while (testcase--) {
	  scanf("%d",&n);
	  for (i = 0;i <= n -2;i++) {
		  num[i] = i + 2;
	  }
	  n--;
	  int full = (1 << n) - 1;
	  ans = 0;
	  for (i = 1;i <= full;i++) {
		  if (i & (1 << (n-1))) {
			  top = 1;
			  for (j = 0;j < n;j++) {
				  if (i & (1 << j)) {
					  a[top++] = num[j];
				  }
			  }
			  if (judge()) {
				  ans ++;
			  }
		  }
	  }
	  printf("Case #%d: %d\n",testid++,ans % 100003);
  }
  return 0;
}

