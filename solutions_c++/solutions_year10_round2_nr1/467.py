/* 
 * SOUR:
 * ALGO:
 * DATE: 2010年 05月 22日 星期六 23:49:42 CST
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
const int N = 128;
struct node 
{
  string name;
  int size;
  vector<int> next;
}*root,pool[N*N];
int top = 0;
int m,n;


void init()
{
  top = 0;
  for (int i = 0;i < N*N;i++) {
	  pool[i].size = 0;
	  pool[i].next.clear();
  }
  root = &pool[top++];
}

void ins(vector<string> name,int idx,node * root)
{
  if (idx == size(name)) {
	  return;
  }
  int i;
  for (i = 0;i < root->size;i++) {
	  if (name[idx] == pool[root->next[i]].name) {
		  ins(name,idx + 1,&pool[root->next[i]]);
		  return;
	  }
  }
  node * tmp = &pool[top++];
  tmp->name = name[idx];
  root->next.pb(top-1);
  root->size++;
  ins(name,idx+1,tmp);
}

int main()
{
  int i,j,k,testcase,testid = 1;
  scanf("%d",&testcase);
  while (testcase--) {
	  init();
	  scanf("%d %d\n",&m,&n);
	  while (m--) {
		  vector<string> name;
		  int t = getchar();
		  while (t == '/') {
			  string newname = "";
			  t = getchar();
			  while (t != '/' && t != '\n') { 
				  newname += t;
				  t = getchar();
			  }
			  name.pb(newname);
		  }
		  ins(name,0,root);
	  }
	  int ans1 = top;
	  while (n--) {
		  vector<string> name;
		  int t = getchar();
		  while (t == '/') {
			  string newname = "";
			  t = getchar();
			  while (t != '/' && t != '\n') { 
				  newname += t;
				  t = getchar();
			  }
			  name.pb(newname);
		  }
		  ins(name,0,root);
	  }
	  int ans2 = top;
	  printf("Case #%d: %d\n",testid++,ans2 - ans1);
  }
  root = &pool[top++];

  return 0;
}

