#include<stdio.h>
#include<conio.h>
#include<math.h>
#include<string.h>

#define INPUTFILE "A-large.in"
#define OUTPUTFILE "A-large.out"

#define BLUE 	0
#define ORANGE 	1
#define OTHER(x) (x ^ 0x1)
#define PREV 	0
#define CURR	1

int t=0;
int n;
FILE *in;
FILE *out;


typedef struct coords
{
	int position;
	int time;
} t_coords;

void main(void)
{
	clrscr();

	in = fopen(INPUTFILE,"r");
	out = fopen(OUTPUTFILE,"w");

	fscanf(in, "%d", &t);
	for(int ti=0; ti<t; ++ti)
	{
		t_coords rInfo[2][2];		// [color][time]
		int runningTime = 0;
		int lastUpdate = 0;

		memset(rInfo, 0, sizeof(t_coords) * 4);
		rInfo[BLUE][PREV].position = 1;
		rInfo[ORANGE][PREV].position = 1;
		fscanf(in, "%d", &n);
		for(int ni=0; ni<n; ni++)
		{
			int color;
			int button;
			int deltaT;
			int noWait;

			fscanf(in, " %s %d", &color, &button);

			color = (color == 'B') ? 0 : 1;
			rInfo[color][CURR].position = button;
			noWait = abs(rInfo[color][PREV].position - button);

			if(lastUpdate == rInfo[color][PREV].time && lastUpdate != 0)
			{
				runningTime += noWait+1;
			}
			else
			{
				deltaT = lastUpdate - rInfo[color][PREV].time;
				if(deltaT > noWait)
					runningTime = lastUpdate + 1;
				else
					runningTime = rInfo[color][PREV].time + noWait + 1;
			}
			rInfo[color][PREV].position = button;
			rInfo[color][PREV].time = runningTime;

			lastUpdate = runningTime;
		}
		fprintf(out, "Case #%d: %d\n", ti+1, runningTime);
	}
	fclose(in);
	fclose(out);
	printf("Done.");
	getch();
}