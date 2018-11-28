#include <cstdio>
#include <vector>
#include <algorithm>

struct train {
  int time;
  char event;
  char place;
  train(int hour, int minute, char _event, char _place) : time(hour*60+minute),
							  event(_event),
							  place(_place) {}
  bool operator<(const struct train &t) const {
    if(time != t.time)
      return time < t.time;
    if(event != t.event)
      return event == '+';
    return false;
  }
};

int main()
{
  int N;
  scanf("%d", &N);
  for(int nc=1; nc<=N; ++nc) {
    std::vector<struct train> v;
    int T, NA, NB;
    scanf("%d%d%d", &T, &NA, &NB);
    int ta=0, tb=0, sa=0, sb=0;
    int h1, m1, h2, m2;
    for(int i=0; i<NA; ++i) {
      scanf("%d:%d%d:%d", &h1, &m1, &h2, &m2);
      v.push_back(train(h1, m1, '-', 'A'));
      v.push_back(train(h2, m2+T, '+', 'B'));
    }
    for(int i=0; i<NB; ++i) {
      scanf("%d:%d%d:%d", &h1, &m1, &h2, &m2);
      v.push_back(train(h1, m1, '-', 'B'));
      v.push_back(train(h2, m2+T, '+', 'A'));
    }
    std::sort(v.begin(), v.end());
    for(std::vector<struct train>::const_iterator it = v.begin();
	it != v.end(); ++it)
      if(it->place=='A') {
	if(it->event=='+')
	  ++ta;
	else if(ta)
	  --ta;
	else
	  ++sa;
      } else {
	if(it->event=='+')
	  ++tb;
	else if(tb)
	  --tb;
	else
	  ++sb;
      }
    printf("Case #%d: %d %d\n", nc, sa, sb);
  }
  return 0;
}
