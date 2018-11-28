// A.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <list>
#include <vector>
#include <cassert>
#include <cstdio>
#include <set>

using namespace std;

bool debug = false;

class Walkway
{
public:

	Walkway()
	{
	}

	Walkway(int b, int e, int s)
	{
		Begin = b;
		End = e;
		Speed = s;
		Length = e - b;
	}

	bool operator< (const Walkway& a) const
	{
		return (Speed < a.Speed);
	}

	int Begin;
	int End;
	int Speed;
	int Length;
};

int _tmain(int argc, _TCHAR* argv[])
{
	int T;

//	FILE *fp = fopen("C:\\Users\\Public\\Documents\\Codejam\\Source\\A-sample.txt", "r");
	FILE *fp = stdin;
	FILE *outFile = stdout;

	if (fp == 0)
	{
		printf("couldn't open input!");
		exit(1);
	}

	fscanf(fp, "%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int X, S, R, runTimeInt, N;
		double runTime;
		double time = 0.0;
		multiset<Walkway> w;
		int noX;

		fscanf(fp, "%d %d %d %d %d", &X, &S, &R, &runTimeInt, &N);
	    runTime = runTimeInt;
		noX = X;

		for (int n = 0; n < N; n++)
		{
			int b, e, s;

			fscanf(fp, "%d %d %d", &b, &e, &s);
			w.insert(Walkway(b, e, s));
			noX -= (e - b);
		}

		w.insert(Walkway(0, noX, 0));

		if (debug)
		{
			int sum = 0;
		for (multiset<Walkway>::iterator iter = w.begin(); iter != w.end(); iter++)
		{
			printf("%d %d %d %d\n", iter->Begin, iter->End, iter->Speed, iter->Length);
			sum += iter->Length;
		}
		printf("X %d noX %d\n", X, noX);
		assert(sum == X);
		}

		for (multiset<Walkway>::iterator iter = w.begin(); iter != w.end(); iter++)
		{
			double walkSpeed = S + iter->Speed;
			double runSpeed = R + iter->Speed;

			if (debug)
			{
				printf("Begin %d End %d Length %d Spd %d runTime %f time %f\n", iter->Begin, iter->End, iter->Length, iter->Speed, runTime, time);
			}


			if (runTime > 0)
			{
				double thisRunTime = iter->Length / runSpeed;

				if (runTime >= thisRunTime)
				{
					if (debug)
					{
						printf("run all: runTime %f thisRunTime %f\n", runTime, thisRunTime);
					}

					// run the whole thing
					time += thisRunTime;
					runTime -= thisRunTime;
				}
				else
				{
				    if (debug)
					{
						printf("run part:  runTime %f thisRunTime %f\n", runTime, thisRunTime);
					}

					time += runTime;
					double remDist = iter->Length - (runSpeed * runTime);
					runTime = 0;
					assert(remDist >= 0);

					if (debug)
					{
						printf("walk part: walkTime %f walkDist %f\n", remDist / walkSpeed, remDist);
					}

					time += remDist / walkSpeed;
				}
			}
			else
			{
				if (debug)
				{
				printf("walk all: dist %d time %f\n", iter->Length,  (iter->Length / walkSpeed));
				}
				time += iter->Length / walkSpeed;
			}
		}

		printf("Case #%d: %.9f\n", t, time);
	}

//	getchar();

	return 0;
}