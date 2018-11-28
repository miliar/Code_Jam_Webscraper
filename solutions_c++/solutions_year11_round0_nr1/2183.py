#include <stdio.h>
#include <stdlib.h>

int t, tc, n, nc, in, sec, btn_ctr;
// false => orange's turn and true => blue's turn
bool *turns, press;
int *btns;
char c;

struct robo {
	int dest_ctr;
	int pos;
	bool name;
};

void updateDest(robo *robot) {
	int temp;
	for(temp = robot->dest_ctr+1; temp < n; temp++) {
		if(turns[temp] == robot->name) {
			robot->dest_ctr = temp;
			break;
		}
	}
	if(temp == n)
		robot->pos = robot->dest_ctr;
}

void act(robo *robot) {
	if(robot->pos < btns[robot->dest_ctr]) {
		robot->pos++;
		return;
	}
	else
		if(robot->pos > btns[robot->dest_ctr]) {
			robot->pos--;
			return;
		}

	if((turns[btn_ctr] == robot->name) && !press) {
		press = true;
		btn_ctr++;
		updateDest(robot);
	}
}

int main() {
	robo orange, blue;
	orange.name = false;
	blue.name = true;

	FILE *ifile, *ofile;
	ifile = fopen("input", "r");
	ofile = fopen("output", "w");

	fscanf(ifile, "%d\n", &t);
	for(tc = 0; tc < t; tc++) {
		
		fscanf(ifile, "%d ", &n);
		turns = new bool[n];
		btns = new int[n];
		
		for(nc = 0; nc < n; nc++) {
			fscanf(ifile, "%c ", &c);
			
			if(c == 'O')
				turns[nc] = false;
			else
				turns[nc] = true;

			fscanf(ifile, "%d ", &in);
			btns[nc] = in;
		}
		
		sec = 0;
		btn_ctr = 0;
		orange.dest_ctr = -1;
		blue.dest_ctr = -1;
		orange.pos = 1;
		blue.pos = 1;

		updateDest(&orange);
		updateDest(&blue);
//		printf("%d %d\n", orange.dest_ctr, blue.dest_ctr);
		while(btn_ctr != n) {
			press = false;
			sec++;
			act(&orange);
			act(&blue);
		}

		delete [] turns;
		delete [] btns;
		turns = NULL;
		btns = NULL;
		fprintf(ofile,"Case #%d: %d\n",tc+1,sec);
	}

	return 0;
}
