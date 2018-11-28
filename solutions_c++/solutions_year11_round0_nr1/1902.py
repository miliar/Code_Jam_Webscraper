#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX_N = 100;
const int ORANGE = 0;
const int BLUE = 1;

int N;
pair<bool, int> Seq[MAX_N];
vector<int> Targets[MAX_N];
int t_pos[2];

inline int
next_target(bool r)
{
  if (t_pos[r] >= Targets[r].size())
	 return -1;

  return Targets[r][t_pos[r]];
}

inline void
solve()
{
  Targets[ORANGE].clear();
  Targets[BLUE].clear();
  t_pos[ORANGE] = t_pos[BLUE] = 0;

  for (int i = 0; i < N; ++i)
	 Targets[Seq[i].first].push_back(Seq[i].second);

  int time = 0;
  int pos[2] = {1, 1};

  for (int i = 0; i < N; ++i) {
	 int delta_time = abs(pos[Seq[i].first] - Seq[i].second) + 1;
	 //	 printf("%c moving to %d\n", ((Seq[i].first == 0) ? 'O' : 'B'), Seq[i].second);
	 if (next_target(1 - Seq[i].first) != -1) {
		if (abs(next_target(1 - Seq[i].first) - pos[1 - Seq[i].first]) <=
			 delta_time)
		  pos[1 - Seq[i].first] = next_target(1 - Seq[i].first);
		else if (next_target(1 - Seq[i].first) < pos[1 - Seq[i].first])
		  pos[1 - Seq[i].first] -= delta_time;
		else
		  pos[1 - Seq[i].first] += delta_time;
	 }
	 pos[Seq[i].first] = Seq[i].second;
	 ++t_pos[Seq[i].first];
	 time += delta_time;
  }

  printf("%d\n", time);
}

int
main()
{
  int T;
  scanf("%d", &T);

  for (int i = 0; i < T; ++i) {
	 scanf("%d", &N);

	 for (int j = 0; j < N; ++j) {
		char color[4];
		int button;
		scanf("%s %d", color, &button);
		
		if ('O' == color[0]) 
		  Seq[j] = make_pair(ORANGE, button);
		else
		  Seq[j] = make_pair(BLUE, button);
	 }

	 printf("Case #%d: ", i + 1);
	 solve();
  }

  return (0);
}
