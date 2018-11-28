#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>

#define MAXY 16
#define MAXX 16

using namespace std;

int nrow, ncol;
char walls[MAXY][MAXX];
vector <pair <int, int> > endstate;
vector <pair <int, int> > startstate;
map <vector <pair <int, int> >, int> mindist;

int isadj(pair <int, int> box1, pair <int, int> box2)
{
	return (abs(box1.first-box2.first) + abs(box1.second-box2.second)) == 1;
}

int connected(vector <pair <int, int> >& state)
{
	if (state.size() == 1)
		return 1;
	if (state.size() == 2)
		return isadj(state[0], state[1]);

	vector <int> reach(state.size(), 0);
	queue <int> q;

	reach[0] = 1;
	q.push(0);

	while (!q.empty()) {
		int x = q.front(); q.pop();

		for (int i = 0; i < state.size(); i++)
			if (reach[i] == 0 && isadj(state[i], state[x])) {
				reach[i] = 1;
				q.push(i);
			}
	}

	return find(reach.begin(), reach.end(), 0) == reach.end();
}

int isfree(vector <pair <int, int> >& state, pair <int, int> place)
{
	return find(state.begin(), state.end(), place) == state.end();
}

int can_horizontal(vector <pair <int, int> >& state, int i)
{
	pair <int, int> box = state[i];

	if (!(box.second-1 >= 0 && box.second+1 < ncol))
		return 0;
	if (walls[box.first][box.second-1] || walls[box.first][box.second+1])
		return 0;

	return isfree(state, make_pair(box.first, box.second-1)) && isfree(state, make_pair(box.first, box.second+1));
}

int can_vertical(vector <pair <int, int> >& state, int i)
{
	pair <int, int> box = state[i];

	if (!(box.first-1 >= 0 && box.first+1 < nrow))
		return 0;

	if (walls[box.first-1][box.second] || walls[box.first+1][box.second])
		return 0;

	return isfree(state, make_pair(box.first-1, box.second)) && isfree(state, make_pair(box.first+1, box.second));
}

void print_state(vector <pair <int, int> > state)
{
	for (int i = 0; i < state.size(); i++)
		printf("(%d, %d) ", state[i].first, state[i].second);
}

void bfs()
{
	queue <vector <pair <int, int> > > q;

	mindist[startstate] = 0;
	q.push(startstate);

	while (!q.empty()) {
		vector <pair <int, int> > state = q.front(); q.pop();
		int d = mindist[state];

/*		printf("State = ");
		print_state(state);
		printf("\n");*/

		for (int i = 0; i < state.size(); i++) {
			if (can_horizontal(state, i)) {
				for (int offx = -1; offx <= 1; offx += 2) {
					vector <pair <int, int> > state2 = state;
					
					state2[i].second += offx;

					if (!connected(state) && !connected(state2))
						continue;

					map <vector <pair <int, int> >, int>::iterator it = mindist.find(state2);
					
					if (it == mindist.end()) {
						mindist[state2] = d+1;
						q.push(state2);
					}
				}
			}
			if (can_vertical(state, i)) {
				for (int offy = -1; offy <= 1; offy += 2) {
					vector <pair <int, int> > state2 = state;
					
					state2[i].first += offy;

					if (!connected(state) && !connected(state2))
						continue;

					map <vector <pair <int, int> >, int>::iterator it = mindist.find(state2);
					
					if (it == mindist.end()) {
						mindist[state2] = d+1;
						q.push(state2);
					}
				}				
			}
		}
	}
}

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		scanf("%d %d", &nrow, &ncol);

		startstate.clear();
		endstate.clear();
		mindist.clear();

		for (int y = 0; y < nrow; y++)
			for (int x = 0; x < ncol; x++) {
				char c;

				scanf(" %c", &c);
				
				walls[y][x] = (c == '#');
				
				if (c == 'o' || c == 'w')
					startstate.push_back(make_pair(y, x));
				if (c == 'x' || c == 'w')
					endstate.push_back(make_pair(y, x));
			}

		bfs();

		printf("Case #%d: ", t+1);
		fprintf(stderr, "%d\n", t+1);

		int bestans = -1;

		sort(endstate.begin(), endstate.end());
		do {
			if (mindist.find(endstate) != mindist.end()) {
				int bla = mindist[endstate];

				if (bestans == -1)
					bestans = bla;
				else
					bestans = min(bestans, bla);
			}
		} while (next_permutation(endstate.begin(), endstate.end()));

		printf("%d\n", bestans);
	}

	return 0;
}
