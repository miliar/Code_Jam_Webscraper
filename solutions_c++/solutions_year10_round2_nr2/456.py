/* 
 * SOUR:
 * ALGO:
 * DATE: 2010年 05月 23日 星期日 00:43:04 CST
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

int n,num;
int des,deadline;

struct  node{
	int loc,speed;
}cock[N];
bool operator < (node a,node b)
{
  if (a.loc != b.loc) {
	  return a.loc > b.loc;
  }
  return a.speed > b.speed;
}

int main()
{
  int i,j,k,testcase,testid = 1;
  scanf("%d",&testcase);
  while (testcase--) {
	  scanf("%d %d %d %d",&n,&num,&des,&deadline);
	  for (i = 0;i < n;i++) {
		  scanf("%d",&cock[i].loc);
	  }
	  for (i = 0;i < n;i++) {
		  scanf("%d",&cock[i].speed);
	  }
	  sort(cock,cock + n);
	  int ans = 0,cnt = 0,tmp = 0;
	  for (int i = 0;i < n;i++) {
		  int t = (des - cock[i].loc + cock[i].speed - 1 )/cock[i].speed;
		  //printf("t = %d\n",t);
		  if (t > deadline) {
			  tmp ++;
		  }else {
			  ans += tmp;
			  cnt ++;
		  }
		  if (cnt == num) {
			  break;
		  }
	  }
	  //printf("cnt = %d,ans = %d\n",cnt,ans);
	  if (cnt < num) {
		  printf("Case #%d: IMPOSSIBLE\n",testid++);
	  }else {
		  printf("Case #%d: %d\n",testid++,ans);
	  }
  }
  return 0;
}

