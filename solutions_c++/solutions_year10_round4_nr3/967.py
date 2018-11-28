/* 
 * SOUR:
 * ALGO:
 * DATE: 2010年 06月 05日 星期六 22:07:11 CST
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
const int N = 128;
int n,m;
int g[N][N];
int f[N][N];

void cp() 
{
  int i,j;
  for (i = 0;i < n;i++) {
  }
}

bool sim()
{
  int i,j;
  bool real = false;
  for (i = 1;i <= m;i++) {
	  for (j = 1;j <= n;j++) {
		  if (g[i][j] == 1) {
			  if (g[i-1][j] == 0 && g[i][j-1] == 0) {
				  f[i][j] = 0;
			  }else {
				  f[i][j] = g[i][j];
			  }
		  }else {
			  if (g[i-1][j] == 1 && g[i][j-1] == 1) {
				  f[i][j] = 1;
			  }else {
				  f[i][j] = g[i][j];
			  }
		  }
		  if (f[i][j]) {
			  real = true;
		  }
	  }
  }
  for (i = 1;i <= m;i++) {
	  for (j = 1;j <= n;j++) {
		  g[i][j] = f[i][j];
	  }
  }
  return real;
}

int main()
{
  int i,j,k , testcase,testid = 1;
  scanf("%d",&testcase);
  while (testcase--) {
	  int num;
	  scanf("%d",&num);
	  n = 0;
	  m = 0;
	  memset(g,0,sizeof(g));
	  while (num--) {
		  int x1,x2,y1,y2;
		  scanf("%d %d %d %d",&y1,&x1,&y2,&x2);
		  if (x1 > x2) { swap(x1,x2); }
		  if (y1 > y2) { swap(y1,y2); }
		  ckmax(m,x1), ckmax(m,x2);
		  ckmax(n,y1), ckmax(n,y2);
		  for (i = x1;i <= x2;i++) {
			  for (j = y1;j <= y2;j++) {
				  g[i][j] = 1;
			  }
		  }
	  }
	  int ans = 1;
	  while (sim()) {
		  ans++;
	  }
	  printf("Case #%d: %d\n",testid++,ans);

  }
  return 0;
}

