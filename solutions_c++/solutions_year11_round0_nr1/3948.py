
#include "stdafx.h"
#include <algorithm>
#include <list>
#include <map>
#include <set>

#define max(a,b) ((a<b)?(b):(a))

int _tmain(int argc, _TCHAR* argv[])
{
    FILE * fIn = fopen("test.in", "r");
    FILE * fOut = fopen("test.out", "w");

    int nTests = 0;
    fscanf(fIn, "%d", &nTests);
    printf("%d tests\n", nTests);

    for (int iTest = 1; iTest <= nTests; iTest++)
    {
		printf ("\nTest %d:", iTest);
		
		// Clear data structures
		struct Objective {
			char colour;
			int dest;
		};

		std::list<Objective> objectives;

		// Read input
		int n;
		fscanf(fIn, "%d ", &n);
		//printf("%d", n);
		for (int i = 0; i < n; ++i)
		{
			Objective obj;
			fscanf(fIn, "%c %d ", &obj.colour, &obj.dest);
			//printf("%c %d", obj.colour, obj.dest);
			objectives.push_back(obj);
		}
		
		struct Robot
		{
			Robot() { pos = 1; idlesince = 0; }
			int pos;
			int idlesince;
		} robots[2];

		//printf("\n"); 

		int time = 0;
		for (std::list<Objective>::const_iterator iterobj = objectives.begin();
			iterobj != objectives.end();
			iterobj++)
		{
			const int robot = iterobj->colour == 'O' ? 0 : 1;

			int tomove = abs(iterobj->dest - robots[robot].pos);
			int timetomove = max(0, tomove - (time - robots[robot].idlesince));
			int timecompleted = time + timetomove + 1;
			
			//printf("Time %d: Robot %c completed button %d in time %d, new time %d\n", 
			//	time, iterobj->colour, iterobj->dest, timetomove, timecompleted);
			robots[robot].idlesince = timecompleted;
			robots[robot].pos = iterobj->dest;

			time = timecompleted;
		}
		
		fprintf(fOut, "Case #%d: %d\n", iTest, time);
	}

	return 0;
}

