#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <utility>
#include <functional>
using namespace std;

typedef pair<int, int> PII;

#define ENGINE second

map<string, int> mp;

int sq[1008];
int cl[108], ch[108];
int ud[108][1008];
char bf[1008];

int main() {
  int t, T, i, k, E, Q, A, e;
  scanf("%d", &T);
  for (t=1; t<=T; t++) {
    mp.clear();
    scanf("%d\n", &E);
    for (i=0; i<E; i++) {
      gets(bf);
      mp[bf]=i;
    }
    scanf("%d\n", &Q);
    memset(cl, 0, sizeof cl);
    memset(ch, 0, sizeof ch);
    for (i=0; i<Q; i++) {
      k=mp[gets(bf)];
      sq[i]=k;
      ud[k][ch[k]++]=i; 
    }
    for (i=0; i<E; i++)
      ud[i][ch[i]++]=1000000;
    priority_queue<PII> pq;
    for (i=0; i<E; i++)
      pq.push(PII(ud[i][cl[i]++], i));
    A=0;
    e=sq[0];
    for (i=0; i<Q; i++) {
      k=sq[i];
      if (e==k) {
	A++;
	e=pq.top().ENGINE;
      }
      pq.push(PII(ud[k][cl[k]++], k));
    }
    printf("Case #%d: %d\n", t, A==0 ? 0 : A-1);
  }
  return 0;
}
