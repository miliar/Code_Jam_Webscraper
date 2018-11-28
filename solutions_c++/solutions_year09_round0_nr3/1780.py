#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <sstream>
#include <set>
#define f(i, n) for(int i = 0; i < n; i++)
#define s(n) scanf("%d", &n)
#define sc(n) scanf("%s", &n)
#define fill(a, v) memset(a, v, sizeof a)
#define inf (int)1e9
using namespace std;

int mem[510][20], vis[510][20], id, l, pl;
string s, p = "welcome to code jam";

int dp(int tx, int px)
{
    //cout << tx << " " << px << endl;
    if(px == pl) return 1;
    if(tx >= l) return 0;
    int &m = mem[tx][px];
    if(vis[tx][px] == id) return m;
    vis[tx][px] = id;
    
    m = 0;
    m += dp(tx + 1, px);
    if(s[tx] == p[px]) m += dp(tx + 1, px + 1);
    
    return m;
}

main()
{
	int n;
	s(n); getline(cin, s);
	for(int zz = 1; zz <= n; zz++)
	{
          id++;
          getline(cin, s);
          l = s.length();
          pl = p.length();
          int ans = dp(0, 0) % 10000;
          printf("Case #%d: ", zz);
          if(ans / 10 == 0) printf("000%d\n", ans);
          else if(ans / 100 == 0) printf("00%d\n", ans);
          else if(ans / 1000 == 0) printf("0%d\n", ans);
          else printf("%d\n", ans);
    }
}
