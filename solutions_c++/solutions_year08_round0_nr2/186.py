// code jam 2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iosfwd>
#include <string>
#include <list>

int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;
	ifstream in;
	ofstream out;
	in.open("C:\\B-large.in");
	out.open("C:\\B-large.out");

	string empt;

	int n_tests, tests;
	in>>n_tests;
	getline(in, empt);

	int turnaround;
	int trains_A, trains_B;
	char A[60*24], B[60*24];
	int i;
	int hour, minute;
	char c;
	int time;
	int needTrains_A, needTrains_B;
	int currentTrains_A, currentTrains_B;

	for (tests=0; tests<n_tests; ++tests)
	{
		trains_A = 0;
		trains_B = 0;
		needTrains_A = 0;
		needTrains_B = 0;
		currentTrains_A = 0;
		currentTrains_B = 0;
		for (i=0; i<60*24; ++i)
		{
			A[i] = 0;
			B[i] = 0;
		}

		in>>turnaround;
		getline(in, empt);

		in>>trains_A;
		in>>trains_B;
		getline(in, empt);


		for (i=0; i<trains_A; ++i)
		{
			in>>hour;
			in>>c;
			in>>minute;
			time = hour*60 + minute;
			A[time] -= 1;

			in>>hour;
			in>>c;
			in>>minute;
			time = hour*60 + minute + turnaround;
			if (time > (60*24-1))
			{
				time = 60*24-1;
			}
			B[time] += 1;
			getline(in, empt);
		}

		for (i=0; i<trains_B; ++i)
		{
			in>>hour;
			in>>c;
			in>>minute;
			time = hour*60 + minute;
			B[time] -= 1;

			in>>hour;
			in>>c;
			in>>minute;
			time = hour*60 + minute + turnaround;
			if (time > (60*24-1))
			{
				time = 60*24-1;
			}
			A[time] += 1;
			getline(in, empt);
		}


		for (i=0;i<60*24;++i)
		{
			if (A[i] != 0)
			{
				currentTrains_A += A[i];
				if (currentTrains_A < 0)
				{
					needTrains_A += abs(currentTrains_A);
					currentTrains_A = 0;
				}
			}

			if (B[i] != 0)
			{
				currentTrains_B += B[i];
				if (currentTrains_B < 0)
				{
					needTrains_B += abs(currentTrains_B);
					currentTrains_B = 0;
				}
			}
		}

		out<<"Case #"<<tests+1<<": "<<needTrains_A<<' '<<needTrains_B<<endl;

	}



	in.close();
	out.close();
	return 0;
}
