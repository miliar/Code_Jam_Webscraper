/******************************************************************************
 * main.cpp
 *
 * Created on: May 6, 2011
 * Copyright Martin Wojtczyk <martin.wojtczyk@gmail.com>
 *
 * Description
 ******************************************************************************/

#include "Problem.h"
#include <iostream>
#include "config.h"

using namespace std;

int main(int argc, char** argv)
{
	if (argc == 2)
	{
		Problem* problem = new Problem();

		problem->process(argv[1]);

		delete problem;
	}
	else
	{
		cout << "Please provide an input file name." << endl;
	};

	return 0;
};
