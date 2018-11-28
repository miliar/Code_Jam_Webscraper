/* 
 * SOUR:
 * ALGO:
 * DATE: 2010年 05月 08日 星期六 15:27:24 CST
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
const int Debug = 0;
const int N = 1024;
int a[N],R,capacity,n;
int hash[N],idx;
int startRound[N],endRound;
int startCost[N];
int endCost;

int main()
{
  int i,j,testcase,testid = 1;
  scanf("%d",&testcase);
  while (testcase--) {
	 scanf("%d %d %d",&R, &capacity,&n);
	 queue<pii> que;
	 for (i = 0;i < n;i++) {
		 scanf("%d",a + i);
		 que.push(pii(i,a[i]));
	 }
	 memset(startRound,-1,sizeof(startRound));
	 memset(startCost,-1,sizeof(startCost));

	 int round = 1;
	 LL cost = 0,ans = 0;
	 while (1) {
		 if (startRound[que.front().X] >= 0) {
			 idx = que.front().X;
			 endCost = cost;
			 endRound = round;
			 break;
		 }
		 int tmp = capacity;
		 startRound[que.front().X] = round++;
		 startCost[que.front().X] = cost;

		 memset(hash,0,sizeof(hash));
		 while (tmp - que.front().Y >= 0 && hash[que.front().X] == 0) {
			 tmp -= que.front().Y;
			 cost += que.front().Y;
			 hash[que.front().X] = 1;
			 que.push(que.front()),que.pop();
		 }
	 }
	 while (!que.empty()) { que.pop(); }
	 for (i = 0;i < n;i++) { que.push(pii(i,a[i])); }

	 cost = endCost - startCost[idx];
	 round = endRound - startRound[idx];
	 if (Debug) {
		 printf("idx = %d,round = %d,startRound[idx] = %d,endRound = %d\n" ,
				idx,round,startRound[idx],endRound); 
		 printf("cost = %lld\n",cost);
	 }
	 if (R < endRound) {
		 while (R--) {
			 memset(hash,0,sizeof(hash));
			 int tmp = capacity;
			 while (tmp - que.front().Y >= 0 && hash[que.front().X] == 0) {
				 tmp -= que.front().Y;
				 ans += que.front().Y;
				 hash[que.front().X] = 1;
				 que.push(que.front()),que.pop();
			 }
		 }
	 }else {
		 int t = startRound[idx];
		 R -= startRound[idx];
		 while (t--) {
			 memset(hash,0,sizeof(hash));
			 int tmp = capacity;
			 while (tmp - que.front().Y >= 0 && hash[que.front().X] == 0) {
				 tmp -= que.front().Y;
				 ans += que.front().Y;
				 hash[que.front().X] = 1;
				 que.push(que.front()),que.pop();
			 }
		 }
		 ans += (R / round) * cost;
		 R %= round;
		 while (R--) {
			 memset(hash,0,sizeof(hash));
			 int tmp = capacity;
			 while (tmp - que.front().Y >= 0 && hash[que.front().X] == 0) {
				 tmp -= que.front().Y;
				 ans += que.front().Y;
				 hash[que.front().X] = 1;
				 que.push(que.front()),que.pop();
			 }
		 }
	 }
	 printf("Case #%d: %lld\n",testid++,ans);

  }
  return 0;
}

