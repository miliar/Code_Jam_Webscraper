#include <algorithm>
#include <cstdio>
#include <vector>


using namespace std;

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  scanf("%d", &tn);

  for (int tt = 1; tt <= tn; tt++)
  {
    int cnt[2], t, na, nb;
    scanf("%d%d%d", &t, &na, &nb);
    
    vector < pair < pair <int, int>, int> > ev;
    for (int i = 0; i < na + nb; i++)
    {
      int a, b, c, d, t1, t2, pos;
      scanf("%d:%d %d:%d", &a, &b, &c, &d);
      t1 = a * 60 + b, t2 = c * 60 + d + t, pos = i >= na;
      ev.push_back(make_pair(make_pair(t1, pos), 1));      
      ev.push_back(make_pair(make_pair(t2, 1 - pos), -1));      
    }
    sort(ev.begin(), ev.end());
    int ncnt[2];
    memset(cnt, 0, sizeof(cnt));
    memset(ncnt, 0, sizeof(ncnt));
    for (int i = 0; i < ev.size(); i++)
    {
      if (ev[i].second == -1)
        ncnt[ev[i].first.second]++;
      else
      {
        if (!ncnt[ev[i].first.second])
          cnt[ev[i].first.second]++;
        else
          ncnt[ev[i].first.second]--;
      }
    }
    
    printf("Case #%d: %d %d\n", tt, cnt[0], cnt[1]);
  }

  return 0;
}