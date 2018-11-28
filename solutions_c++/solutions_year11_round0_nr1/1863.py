#include <stdio.h>
#include <math.h>
#include <queue>
using namespace std;

#define BLUE 0
#define ORANGE 1

queue<int> q; // the robots' turns

// parallel
queue<int> next_pos[2];
int current_pos[2];

char robot_code[4];

int main()
{
	int kase, serial=1,
		n, pos,
		robot, frd,
		move, frd_move,
		soln;

	scanf("%d", &kase);
//	printf("%d\n", kase);
	while (kase--) {
		// begin test case

		soln = 0;
		current_pos[BLUE] = 1;
		current_pos[ORANGE] = 1;

		scanf("%d", &n); // number of steps
		for (int i=0; i<n; ++i) {
			scanf("%s %d", robot_code, &pos);
			robot = ('B' == robot_code[0] ? BLUE : ORANGE);
			q.push(robot);
			next_pos[robot].push(pos);
		}

		while (! q.empty()) {
			robot = q.front(); // the one who need to push button next
			frd = !robot;
//			printf("Round %d, Robot = %d\n", i, robot);
//			printf("\t%d %d\n", current_pos[BLUE], current_pos[ORANGE]);
//			printf("\t%d %d\n",
//				next_pos[BLUE].empty() ? 999 : next_pos[BLUE].front(),
//				next_pos[ORANGE].empty() ? 999 : next_pos[ORANGE].front()
//			);

			if (current_pos[robot] == next_pos[robot].front()) { // I push button
//				printf("%d push button at %d\n", robot, next_pos[robot].front());

				++soln;
				next_pos[robot].pop();
				q.pop();

				if (! next_pos[frd].empty() && current_pos[frd] != next_pos[frd].front()) { // friend stays or moves
					current_pos[frd] += (current_pos[frd] < next_pos[frd].front() ? 1 : -1);
//					printf("%d move 1 step to reach %d\n", frd, current_pos[frd]);
				}
			}
			else {
				move = abs(next_pos[robot].front() - current_pos[robot]); // I move
				soln += move;
				current_pos[robot] < next_pos[robot].front() ?
					(current_pos[robot] += move) :
					(current_pos[robot] -= move);
//				printf("%d move %d steps to reach %d\n", robot, move, current_pos[robot]);

				if (! next_pos[frd].empty() && current_pos[frd] != next_pos[frd].front()) { // friend stays or moves
					frd_move = abs(next_pos[frd].front() - current_pos[frd]);
					move = min(move, frd_move);
					current_pos[frd] < next_pos[frd].front() ?
						(current_pos[frd] += move) :
						(current_pos[frd] -= move);
//					printf("%d move %d steps to reach %d\n", frd, move, current_pos[frd]);
				}
			}
//			printf("\t%d %d\n", current_pos[BLUE], current_pos[ORANGE]);
//			printf("\t%d %d\n",
//				next_pos[BLUE].empty() ? 999 : next_pos[BLUE].front(),
//				next_pos[ORANGE].empty() ? 999 : next_pos[ORANGE].front()
//			);
//			puts("");
		}

		printf("Case #%d: %d\n", serial++, soln);
		// end test case
	}
	return 0;
}
