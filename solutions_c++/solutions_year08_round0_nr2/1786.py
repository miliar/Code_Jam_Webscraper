// googleCodeContest.cpp : Defines the entry point for the console application.
//
// Stephan Carpenter (TsuQ)
//
// This code is certainly inefficient, but should be fast enough for the purpose of the contest.

#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <stdio.h>
using namespace std;

#include <fstream>
using namespace std;

#include <string>
using namespace std;

int main()
{
	const int MINS_IN_DAY=60*24;
	ifstream f("B-small.in");
	ofstream of("B-small-out.txt");
	int cases;
	int turnAround;
	int N1out;
	int N2out;
	int N1;
	int N2;
	char discard;
	int trainsNeededA[MINS_IN_DAY];
	int trainsNeededB[MINS_IN_DAY];
	int hours;
	int minutes;
	int currentMinute;
	int w, x, y, z;

	for(x=0; x<MINS_IN_DAY; x++)
	{
		trainsNeededA[x]=0;
		trainsNeededB[x]=0;
	}

	f >> cases;
	for(x=0; x<cases; x++)
	{
		for(z=0; z<MINS_IN_DAY; z++)
		{
			trainsNeededA[z]=0;
			trainsNeededB[z]=0;
		}
		f >> turnAround;
		f >> N1;
		f >> N2;

		for(w=0; w<N1; w++)
		{
			f >> hours;
			f >> discard;
			f >> minutes;
			currentMinute=hours*60+minutes;
			for(y=currentMinute; y<MINS_IN_DAY; y++)
			{
				trainsNeededA[y]++;
			}

			f >> hours;
			f >> discard;
			f >> minutes;
			currentMinute=hours*60+minutes;
			currentMinute+=turnAround;
			for(y=currentMinute; y<MINS_IN_DAY; y++)
			{
				trainsNeededB[y]--;
			}

		}

		for(w=0; w<N2; w++)
		{
			f >> hours;
			f >> discard;
			f >> minutes;
			currentMinute=hours*60+minutes;
			for(y=currentMinute; y<MINS_IN_DAY; y++)
			{
				trainsNeededB[y]++;
			}

			f >> hours;
			f >> discard;
			f >> minutes;
			currentMinute=hours*60+minutes;
			currentMinute+=turnAround;
			for(y=currentMinute; y<MINS_IN_DAY; y++)
			{
				trainsNeededA[y]--;
			}

		}


		N1out=0;
		N2out=0;

		for(w=0; w<MINS_IN_DAY; w++)
		{
			if(trainsNeededA[w]>N1out)
			{
				N1out=trainsNeededA[w];
			}

			if(trainsNeededB[w]>N2out)
			{
				N2out=trainsNeededB[w];
			}
		}
		of << "Case #" << (x+1) << ": " << N1out << " " << N2out << endl;
	}
	f.close();
	of.close();


	cout << "Done." << endl;

    char a;
	cin >> a;
	return 0;
}
