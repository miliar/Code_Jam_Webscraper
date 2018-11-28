#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

const int MAXN = 1005;
typedef long long ll;

int tc, R, K, N;
int gsize[MAXN], next[MAXN];
vector<int> list;
bool seen[MAXN];

void init() {
  list.clear();
  memset(next, 0, sizeof next);
  memset(seen, 0, sizeof seen);
}  

int main() {
  scanf("%d", &tc);
  for(int z = 1; z <= tc; z++) {
    init();
    
    int i, prev, start, sent;
    ll size, ans = 0;
    
    scanf("%d%d%d", &R, &K, &N);
    for(i = 1; i <= N; i++)
      scanf("%d", &gsize[i]);
    
    i = N;
    do {
      seen[prev = i] = true; // Last group admitted
      for(i = i%N + 1, size = 0, sent = 0; ; i = i%N + 1) {
        if(sent == N || size + gsize[i] > K)
          break;
        size += gsize[i]; // Try to take as many groups as possible
        sent++;
      }
      list.push_back(size); // Add this size to the list
      if(!--i) i = N;
      next[prev] = i; // From the first waiting group, thorugh --i waiting group can be batched this time
    } while(!seen[i]); // If it has already been seen, we're in a cycle hereon
    start = i;

    if(R <= list.size())
      for(i = 0; i < R; i++)
        ans += list[i];
    else {
      for(i = N; i != start; R--, i = next[i]) {
        ans += *list.begin();
        list.erase(list.begin());
      }
      ll comp = R / list.size();
      ll def = R % list.size();
      ll sum = 0;
      for(vector<int>::iterator it = list.begin(); it != list.end(); it++)
        sum += *it;
      ans += sum * comp;
      for(int i = 0; i < def; i++)
        ans += list[i];
    }
    printf("Case #%d: %lld\n", z, ans);
  }
  return 0;
}
