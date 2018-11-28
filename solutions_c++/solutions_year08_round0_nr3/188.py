// Code jam 3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iosfwd>
#include <string>
#include <list>
#include <math.h>
#include <stdio.h>]

const float pi = 3.14159265358979;

int _tmain(int argc, _TCHAR* argv[])
{
	using namespace std;
	ifstream in;
	in.open("C:\\C-large.in");

	string empt;

	int n_tests, tests;
	in>>n_tests;
	getline(in, empt);

	double f, R, t, r, g, R_otn;

	FILE* out = fopen("C:\\C-large.out","w+");

	int i, j;
	double ver;
	double x1,y1,x2,y2;
	double x_over1,y_over1,x_over2,y_over2;
	double square_for_fly;
	double currentSquare;
	double currentSector;

	double angle;

	int quant;
	for (tests=0; tests<n_tests; ++tests)
	{
		square_for_fly = 0;
		in>>f;
		in>>R;
		in>>t;
		in>>r;
		in>>g;
		getline(in, empt);
		t = t + f;
		r = r + f;
		g = g - 2*f;
		R_otn = R - t;
		if (g <= 0)
		{
			ver = 1.00000;
		}
		else
		{
			quant = floor(R_otn/(g+2*r))+1;
			for (i=0; i<quant; ++i)
			{
				y1 = r + i*(g+2*r);
				y2 = y1 + g;
				for (j=0; j<quant; ++j)
				{
					x1 = r + j*(g + 2*r);
					x2 = x1 + g;
					if (sqrt(x1*x1+y1*y1) >= R_otn)
					{
						break;
					}
					if (sqrt(x2*x2+y2*y2) > R_otn)
					{
						if (sqrt(x2*x2+y1*y1) >= R_otn)
						{
							if (sqrt(x1*x1+y2*y2) >= R_otn)
							{
								x_over2 = x1;
								y_over1 = y1;
								x_over1 = sqrt(R_otn*R_otn - y_over1*y_over1);
								y_over2 = sqrt(R_otn*R_otn - x_over2*x_over2);

								currentSquare = (x_over1-x1)*(y_over2-y1)/2;
							}
							else
							{
								y_over1 = y1;
								y_over2 = y2;
								x_over1 = sqrt(R_otn*R_otn - y_over1*y_over1);
								x_over2 = sqrt(R_otn*R_otn - y_over2*y_over2);

								currentSquare = g*((x_over1-x1) + (x_over2-x1))/2;
							}
						}
						else
						{
							if (sqrt(x1*x1+y2*y2) >= R_otn)
							{
								x_over1 = x2;
								x_over2 = x1;
								y_over1 = sqrt(R_otn*R_otn - x_over1*x_over1);
								y_over2 = sqrt(R_otn*R_otn - x_over2*x_over2);

								currentSquare = g*((y_over1-y1) + (y_over2-y1))/2;
							}
							else
							{
								x_over1 = x2;
								y_over2 = y2;
								y_over1 = sqrt(R_otn*R_otn - x_over1*x_over1);
								x_over2 = sqrt(R_otn*R_otn - y_over2*y_over2);

								currentSquare = g*g - (x2-x_over2)*(y2-y_over1)/2;
							}
						}
						square_for_fly += currentSquare;
					

						angle = atan(y_over2/x_over2) - atan(y_over1/x_over1);
						currentSector = R_otn*R_otn*angle/2 - R_otn*R_otn*sin(angle)/2;
						square_for_fly += currentSector;
				}
					else
					{
						currentSquare = g*g;
						square_for_fly += currentSquare;
					}
				}
			}
			ver = 1 - (4*square_for_fly/(pi*R*R));
		}
		fprintf(out, "%s%d%s%f\n", "Case #", tests+1, ": ", ver);

	}



	in.close();
	fclose(out);
	return 0;
}
