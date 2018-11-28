#include <algorithm>
#include <vector>

#include <cstdio>

using namespace std;

const int INF = 1000000000;
const int MAX_N = 128;
const int MAX_P = 100;

int N;
vector< pair<int, int> > seq;

int min_time[MAX_N][MAX_P+1];

void read_input()
{
  scanf("%d", &N);
  seq.resize(N+1);

  seq[0] = make_pair(0, 1);
  for (int i = 1; i <= N; i++) {
    int ch;
    do {
      ch = getchar();
    } while (ch != 'O' && ch != 'B');

    int pos;
    scanf("%d", &pos);

    seq[i] = make_pair((ch == 'O' ? 0 : 1), pos);
  }
}

void unpack_location(int* pos, int current_step, int other_robot_pos)
{
  int cur_robot = seq[current_step].first;
  int other_robot = 1 ^ cur_robot;

  pos[cur_robot] = seq[current_step].second;
  pos[other_robot] = other_robot_pos;
}

int calc_time(int clicker, int* r_pos, int* n_pos)
{
	int time[2];
	for (int i = 0; i < 2; i++)
		time[i] = abs(n_pos[i] - r_pos[i]);
	time[clicker]++;

	return max(time[0], time[1]);
}

void update(int time, int step, int pos)
{
  int& mt = min_time[step][pos];
  mt = min(mt, time);
}

int solve()
{
	// Init
	for (int i = 0; i <= MAX_P; i++)
		min_time[0][i] = INF;
	min_time[0][1] = 0;

	// Solve
	for (int done = 0; done < N; done++) {
		for (int i = 0; i <= MAX_P; i++)
			min_time[done+1][i] = INF;

		int r_pos[2], n_pos[2];
		for (int other_pos = 1; other_pos <= MAX_P; other_pos++) {
			int cur_time = min_time[done][other_pos];
			if (cur_time >= INF)
				continue;

			unpack_location(r_pos, done, other_pos);
			for (int dst_pos = 1; dst_pos <= MAX_P; dst_pos++) {
				unpack_location(n_pos, done+1, dst_pos);
				int new_time = cur_time + calc_time(seq[done+1].first, r_pos, n_pos);
				update(new_time, done+1, dst_pos);
			}
		}
	}

	// Return answer
	return *min_element(min_time[N]+1, min_time[N]+MAX_P+1);
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "w", stdout);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 0; iTest < nTest; iTest++) {
		read_input();
		printf("Case #%d: %d\n", iTest+1, solve());
	}
	return 0;
}
