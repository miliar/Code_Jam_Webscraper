// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <list>
#include <string>
#include <stdlib.h>
using namespace std;

#define ORANGE 0
#define BLUE 1


inline int GetNextButton(int cur_move, int buttons, int color, int * moves, int * moves_order)
{
	cur_move++; //increment to get the next move
	while(cur_move < buttons)
	{
		if (moves_order[cur_move] == color)
			return moves[cur_move];
		else
			cur_move++;
	}
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char line[500], str_int[5];
	int cur_case = 0, cases, buttons, ptr, npos, time, cur_move, orange_pos, blue_pos, next, jump, other_jump;
	ofstream outfile;
	ifstream infile;

	outfile.open("answer.txt");
	if (!outfile.is_open()){
		cout<<"Error opening output file\n";
		goto end;
	}

	infile.open("in.txt");
	if (!infile.is_open()){
		cout<<"Error opening input file\n";
		goto end;
	}

	memset(str_int, 0, 5);
	infile.getline(str_int, 5);
	cases = atoi(str_int);
	while(cur_case < cases)
	{
		time = 0; //reset time for each case
		memset(str_int, 0, 5);
		memset(line, 0, 500);
		infile.getline(line, 500);
		ptr = 0;
		while(line[ptr] != ' ') ptr++;
		memcpy(str_int,line,ptr);
		buttons = atoi(str_int);
		ptr++;

		//read in each move in the line sequence and store it for processing
		int * moves = new int[buttons];
		int * moves_order = new int[buttons];
		cur_move = 0;
		while(1)
		{
			if (line[ptr] == 'O')
				moves_order[cur_move] = ORANGE;
			else
				moves_order[cur_move] = BLUE;

			ptr+=2;
			npos = ptr;
			while((line[npos] != ' ') & (line[npos] != 0)) npos++;
			memset(str_int, 0, 5);
			memcpy(str_int, line+ptr, npos - ptr);
			moves[cur_move] = atoi(str_int);

			if (line[npos])
			{
				ptr = npos+1;
				cur_move++;
			}
			else
				break;
		}

		//process the sequence of moves and output the result
		orange_pos = 1;
		blue_pos = 1;
		time = 0;
		int this_color;
		int other_color;
		int * cur_pos;
		int * other_pos;

		for (cur_move = 0; cur_move < buttons; cur_move++)
		{
			if (moves_order[cur_move] == ORANGE)
			{
				this_color = ORANGE;
				other_color = BLUE;
				cur_pos = &orange_pos;
				other_pos = &blue_pos;
			}
			else
			{
				this_color = BLUE;
				other_color = ORANGE;
				cur_pos = &blue_pos;
				other_pos = &orange_pos;
			}
			jump = abs(moves[cur_move] - *cur_pos) + 1;
			time += jump;
			*cur_pos = moves[cur_move];

			//while this current move has been made, find out what the other bot should be doing
			next = GetNextButton(cur_move,buttons,other_color,moves,moves_order);
			if (next == -1) continue;
			other_jump = abs(next - *other_pos);
			if (other_jump > jump)
			{
				if (next > *other_pos)
						*other_pos += jump;
				else
						*other_pos -= jump;
			}
			else
			{
					if (next > *other_pos)
						*other_pos += other_jump;
					else
						*other_pos -= other_jump;
			}
		}

		outfile<<"Case #"<<cur_case+1<<": "<<time<<endl;

		//clean up and reset for the next case
		delete [] moves_order;
		delete [] moves;
		cur_case++;
	}


end:
	infile.close();
	outfile.flush();
	outfile.close();
	getchar();
	return 0;
}

