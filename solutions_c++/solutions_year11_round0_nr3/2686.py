// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <list>
#include <stdlib.h>
using namespace std;

#define ORANGE 0
#define BLUE 1
#define LINE_SIZE 10000
#define STR_INT_SIZE 10


inline int PatricksSum(list<int> * candy_bag)
{
	list<int>::iterator it;
	int sum = 0;

	for (it = candy_bag->begin(); it != candy_bag->end(); it++)
		sum = sum ^ *it;

	return sum;
}

int _tmain(int argc, _TCHAR* argv[])
{
	char line[LINE_SIZE], str_int[STR_INT_SIZE];
	int cur_case = 0, cases, total_candies, ptr, nptr, tmp, patricks_score, seans_score, equal;

	ofstream outfile;
	ifstream infile;

	list<int> seans_bag;

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

	memset(str_int, 0, STR_INT_SIZE);
	infile.getline(str_int, STR_INT_SIZE);
	cases = atoi(str_int);
	while(cur_case < cases)
	{
		//cout<<"CUR CASE IS: "<<cur_case<<endl;
		//reset variables for each case
		patricks_score = 0;
		seans_score = 0;
		seans_bag.clear();

		//read in the total amount of candies
		memset(str_int, 0, STR_INT_SIZE);
		infile.getline(str_int, STR_INT_SIZE);
		total_candies = atoi(str_int);

		//read in the next string line
		memset(line, 0, LINE_SIZE);
		infile.getline(line, LINE_SIZE);
		ptr = 0;
		tmp = 0;


		//read in each integer in the line
		while(tmp < total_candies)
		{
			nptr = ptr;
			while((line[nptr] != ' ') & (line[nptr] != 0)) nptr++;
			memset(str_int, 0, STR_INT_SIZE);
			memcpy(str_int, line+ptr, nptr - ptr);
			int i = atoi(str_int);
			seans_bag.push_back(i);
			seans_score += i;

			if (line[nptr])
			{
				ptr = nptr+1;
				tmp++;
			}
			else
				break;
		}

		//now do the actual processing
		seans_bag.sort();
		patricks_score = seans_bag.front();
		seans_score -= seans_bag.front();
		seans_bag.pop_front();
		equal = PatricksSum(&seans_bag) ^ patricks_score;

		while((equal != 0)&&(!seans_bag.empty()))
		{
			patricks_score ^= seans_bag.front(); //^ instead of + since Patrick cant add properly
			seans_score -= seans_bag.front();
			seans_bag.pop_front();
			equal = PatricksSum(&seans_bag) ^ patricks_score;
		}

		if ((equal == 0)&&(!seans_bag.empty()))
			outfile<<"Case #"<<cur_case+1<<": "<<seans_score<<endl;
		else
			outfile<<"Case #"<<cur_case+1<<": NO\n";


		cur_case++;
	}


end:
	infile.close();
	outfile.flush();
	outfile.close();
	getchar();
	return 0;
}

