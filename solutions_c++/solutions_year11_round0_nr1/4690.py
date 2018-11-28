#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	FILE* pfi;
	FILE* pfo;

	fopen_s(&pfi, "A-large.in", "r");
	fopen_s(&pfo, "output.txt", "w");
///////////////////////////////////
	
	char buff[520];
	char* token;
	char* next_token;
	int cases = 0;

	memset(buff, 0, 520);
	fgets(buff, 520, pfi);
	sscanf_s(buff, "%d", &cases);

	int i, j = 0;
	char result[25];
	int len = 0;
	int nbbutt = 0;
	char robot; 
	int buttopress;
	int sec;
	int timetowait;
	int timetomove;
	int pos;
	int pos_O = 1;
	int pos_B = 1;
	int sec_O = 0;
	int sec_B = 0;
	for (i = 0; i < cases; i++)
	{
		/////////////////////////////////////////
		nbbutt = 0;
		memset(buff, 0, 520);	
		fgets(buff, 520, pfi);
		token = strtok_s(buff, " ", &next_token);
		nbbutt = atoi(token);
		//c++ s*** if you align the variable like int x,x,x, here
		//you get a fabulous random of the result
		//maybe i messed up with the pointer, but well ...
		robot = 0; 
		buttopress = 0;
		sec = 0;
		timetowait = 0;
		timetomove = 0;
		
		pos = 0;
		pos_O = 1;
		pos_B = 1;
		sec_O = 0;
		sec_B = 0;
		for (j = 0; j < nbbutt; j++)
		{
			token = strtok_s(NULL, " ", &next_token);
			robot = *token;
			token = strtok_s(NULL, " ", &next_token);
			buttopress = atoi(token);

			(robot == 'O') ? sec = sec_O : sec = sec_B;
			(robot == 'O') ? pos = pos_O : pos = pos_B;
			(robot == 'O') ? timetowait = sec_B : timetowait = sec_O;

			timetomove = pos - buttopress; //nb sec to move to the button 1m/s
			if (timetomove < 0)
				timetomove = timetomove * -1;
			sec += timetomove;
			if (sec < timetowait)
				sec = timetowait;
			sec = sec + 1; //push the button

			(robot == 'O') ? sec_O = sec : sec_B = sec;
			(robot == 'O') ? pos_O = buttopress : pos_B = buttopress;
		}

		/////////////////////////////////////////
		memset(result, 0, 25);
		len = sprintf_s(result, "Case #%d: %d\n", i+1, (sec_O > sec_B ?  sec_O : sec_B));
		fwrite(result, 1, len, pfo);
	}

//////////////////////////////////////
	fclose(pfi);
	fclose(pfi);
	return 0;
}



