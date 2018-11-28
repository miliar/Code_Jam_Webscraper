#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

struct Node {
   char name[128];
   char exist;
   Node() : exist(0) {name[0]=0;}
   bool operator <(const Node& right) const {
      int res = strcmp(name, right.name);
      if (res) return res < 0;
      else
         return exist > right.exist;
   }
};

Node nlist[200];

int doit(Node* already, Node* test) {
   if (test->exist) return 0;

   const char* already_path = already ? already->name : "/";
   char* test_path = test->name;
   int start = 0;
   while(already_path[start]) {
      if (already_path[start] != test_path[start])
         break;
      ++start;
   }
   
   if (test_path[start] == 0) return 0;

   int res = 0;
   while(test_path[start] != '/')
      --start;
   ++start;
   while(test_path[start]) {
      if (test_path[start-1] == '/' && test_path[start] != '/')
         ++res;
      ++start;
   }
   return res;
}

int main() {
	freopen("problem.in", "r", stdin);
	freopen("problem.out", "w", stdout);
	int T;
   int N, M;
	scanf("%d", &T);
	for (int tid=1; tid<=T; ++tid) {
      scanf("%d %d", &N, &M);
      int cnt = 0;

      for (int i=0; i<N; ++i) {
         scanf("%s", nlist[cnt].name);
         nlist[cnt].exist = 1;
         ++cnt;
      }
      for (int i=0; i<M; ++i) {
         scanf("%s", nlist[cnt].name);
         nlist[cnt].exist = 0;
         ++cnt;
      }
      sort(nlist, nlist+cnt);
      int res = 0;
      res += doit(NULL, nlist+0);
      for (int i=1; i<cnt; ++i) {
         res += doit(nlist+i-1, nlist+i);
      }

		printf("Case #%d: %d\n", tid, res);
	}
	return 0;
}


