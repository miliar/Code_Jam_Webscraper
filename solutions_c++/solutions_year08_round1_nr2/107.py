#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

#define FOR(i, N) for(int i = 0, _n = N ; i < _n ; ++i )

#define MAX 2002

int C[MAX][MAX];

int main()
{
  int CC;
  scanf("%d", &CC);

  FOR(c, CC) {
    printf("Case #%d: ", c+1);
    
    int N, M;
    vector <int> malt;
    vector <int> cnt;
    vector <bool> malted;
    bool impossible = false;
    queue <int> q;
    FOR(i, MAX) FOR(j, MAX) C[i][j] = 0;

    scanf("%d %d", &N, &M);
    malt.resize(M);
    cnt.resize(M);
    malted.resize(N+1);
    
    FOR(i, M) {
      int T;
      scanf("%d", &T);
      FOR(j, T) {
	int x, y;
	scanf("%d %d", &x, &y);
	if(y==1) malt[i] = x;
	else { C[i][x] = 1; cnt[i]++; }
      }
    }
    FOR(i, M)
      if(cnt[i] == 0) {
	if(malt[i] == 0) { impossible = true; break; }
	q.push(malt[i]);
	malted[malt[i]] = true;
      }
    
    while(not q.empty() and not impossible) {
      int cur = q.front();
      q.pop();
      
      FOR(i, M)
	if(C[i][cur] == 1) {
	  C[i][cur] = 0;
	  cnt[i] --;
	  if(cnt[i] == 0) {
	    if(malt[i] == 0) { impossible = true; break; }
	    if(malted[malt[i]] == true) continue;
	    q.push(malt[i]);
	    malted[malt[i]] = true;
	  }
	}
    }
    
    if( impossible )
      printf("IMPOSSIBLE\n");
    else
      FOR(i, N)
	printf("%d%c", int(malted[i+1]), (i==(N-1)?'\n':' '));
  }
}
