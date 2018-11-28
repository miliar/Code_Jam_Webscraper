#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>

#define STAY 0
#define MOVE 1
#define PUSH 2
#define IDLE 3
#define FINISHED 4

struct task_s {
	int who;
	int where;
	int what;
	int next;
};

struct task_s tasks[100];
struct task_s state[2];

int sign(int n)
{
	return n < 0 ? -1 : 1;
}

int main(int argc, char**argv)
{
	if (argc != 2) exit(1);
	FILE *in = fopen(argv[1], "rt");
	if (!in) {
		ferror(in);
	}
	FILE *out = fopen("output.txt", "wt");
	int T=0;
	fscanf(in,"%d",&T);
	int i,j,k;
	for (i = 0; i < T; i++) {
		int N=0;
		fscanf(in,"%d",&N);
		for (j = 0; j < N; j++) {
			char who;
			fscanf(in,"%c%c",&who,&who);
			fscanf(in,"%d",&(tasks[j].where));
			tasks[j].who = who == 'B';
		}
		int current, time = 0;
		state[0].where = state[1].where = 1;
		state[0].what = state[1].what = IDLE;
		for (current = 0; current < N; current++) {
			struct task_s *task = &tasks[current];
			int timeconsumed = abs(task->where - state[task->who].where) + 1;
			state[task->who].where = task->where;
			time += timeconsumed;
			struct task_s *other = &state[1 - task->who];
			if (other->what != FINISHED) {
				other->what = FINISHED;
				for (k = current + 1; k < N; k++) {
					if (tasks[k].who == 1 - task->who) {
						if (tasks[k].where == other->where) {
							other->what = STAY;
							break;
						}
						int stepsneeded = tasks[k].where - other->where;
						if (abs(stepsneeded) > timeconsumed) {
							other->where += sign(stepsneeded) * timeconsumed;
							other->what = MOVE;
						} else {
							other->where = tasks[k].where;
							other->what = STAY;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", i + 1, time);
		fprintf(out, "Case #%d: %d\n", i + 1, time);
	}
	fclose(in);
	fclose(out);
}
