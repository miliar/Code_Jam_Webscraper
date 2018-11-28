// A.cpp : Defines the entry point for the console application.
//

#include <math.h>
#include <stdio.h>
#include <memory.h>

struct taskvalue
{
	int sumtime;
	int pos;
};

struct task
{
	char name;
	int action;
	struct taskvalue *val;
};

#define TASK_MAX_NUM 100

int maxtime(struct task *tlist, int tasknum, struct taskvalue *tval)
{
	
	int atime = 0;
	int btime = 0;

	struct task *pcur = NULL;
	struct task *pnext = NULL;



	for (int i = 0, j = 1; i < tasknum; i ++, j ++){
		pcur = &tlist[i];
		pnext = &tlist[j];

		//name equal or i is last task
		if (pcur->name == pnext->name || j == tasknum){
			pcur->val->sumtime += abs(pcur->action - pcur->val->pos) + 1;
			pcur->val->pos = pcur->action;
			continue;
		}

		//name isn't equal


		atime = abs(pcur->action - pcur->val->pos) + 1 + pcur->val->sumtime;
		btime = abs(pnext->action - pnext->val->pos) + 1 + pnext->val->sumtime;

		if (btime <= atime){
			pnext->val->sumtime = atime;
			pnext->val->pos = pnext->action;
		}

		pcur->val->pos = pcur->action;
		pcur->val->sumtime = atime;
	}

	atime = (tval[0].sumtime > tval[1].sumtime) ? tval[0].sumtime:tval[1].sumtime;

	//printf("time:%d \n", atime);
	return atime;
}

int main(int argc, char* argv[])
{
    if (argc != 2) {
		printf("Usage: ./main input_file\n");
		return -1;
    }
    FILE *fp = fopen(argv[1], "r");
    if (!fp) {
		printf("Input File %s Open Error.\n", argv[1]);
		return 0;
    }

	struct task tlist[TASK_MAX_NUM];
	struct taskvalue tval[2];

	memset(&tlist, 0x00, sizeof (struct task) * 100);


    int T, N;
	unsigned char idx;

    fscanf(fp, "%d\n", &T);
    for (int i = 0; i < T; i++) {
		fscanf(fp, "%d", &N);
		memset(&tval, 0x00, sizeof (struct taskvalue) << 1);

		tval[0].pos = 1;
		tval[1].pos = 1;
		idx = 0;
		for (int j=0,k=0; j < N; k = j, j++){
			fscanf(fp, " %c %d", &tlist[j].name, &tlist[j].action);
			if (j != k && tlist[j].name != tlist[k].name){
				idx = 1 - idx;
			}
			tlist[j].val = &tval[idx];
		}
		printf("Case #%d: %d \n", i + 1, maxtime(tlist, N, tval));
	}
	fclose(fp);

/*	

	tlist[0].name = 'b';
	tlist[0].action = 6;
	tlist[0].val = &tval[0];

	tlist[1].name = 'b';
	tlist[1].action = 70;
	tlist[1].val = &tval[0];

	tlist[2].name = 'o';
	tlist[2].action = 2;
	tlist[2].val = &tval[1];

	tlist[3].name = 'o';
	tlist[3].action = 4;
	tlist[3].val = &tval[1];

	tlist[4].name = 'o';
	tlist[4].action = 7;
	tlist[4].val = &tval[1];
	
	tlist[5].name = 'b';
	tlist[5].action = 78;
	tlist[5].val = &tval[0];

	maxtime(tlist, 6, tval);*/
	return 0;
}

