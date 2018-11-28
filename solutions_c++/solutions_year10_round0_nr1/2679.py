/* 
 * SOUR:
 * ALGO:
 * DATE: 2010年 05月 08日 星期六 10:52:40 CST
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
#include<cmath>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
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
#define bin(x) (1 << (x))

int n,k;
bool judge()
{
  int i;
  for (i = 0;i < n;i++) {
	  if (!(bin(i) & k)) {
		  return false;
	  }
  }
  return true;
}

int main()
{
  int testcase,testid = 1;
  scanf("%d",&testcase);
  while (testcase--) {
	  scanf("%d%d",&n,&k); 
	  if (judge()) {
		  printf("Case #%d: ON\n",testid++); 
	  }else {
		  printf("Case #%d: OFF\n",testid++); 
	  }
  }
  
  return 0;
}

