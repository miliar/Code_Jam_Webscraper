// TrainTimetable.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdlib.h"
#include <list>
#include <string>

enum TYPE
{
	_saida,
	_chegada
};


struct EVENT
{
	unsigned int time;
	TYPE type;

};


bool operator == (const EVENT& a, const EVENT& b)
{
	return ((a.time == b.time) && (a.type == b.type));
}

bool operator < (const EVENT& a, const EVENT& b)
{
	if(a.time != b.time)
		return (a.time < b.time);
	else
		return (a.type == _chegada);
}


unsigned int timeToMinutes(const char* time)
{
int hh, mm;

	sscanf(time, "%02d:%02d", &hh, &mm);

	return 60*hh+mm;
}


int main(int argc, _TCHAR* argv[])
{
FILE* fpIn;
FILE* fpOut;
char line[1024];
char hrSaida[128], hrChegada[128];
unsigned int N, T, NA, NB;
int disp, totalA, totalB;
std::list<EVENT> eventsA;
std::list<EVENT> eventsB;
unsigned int i, j;

	fpIn = fopen(argv[1], "rb");
	fpOut = fopen(argv[2], "wb");

	N = atoi(fgets(line, 1024, fpIn));

	for(i=0; i < N; i++)
	{
		eventsA.clear();
		eventsB.clear();

		T = atoi(fgets(line, 1024, fpIn));
		fgets(line, 1024, fpIn);
		sscanf(line, "%d %d", &NA, &NB);

		totalA = totalB = 0;

		for(j = 0; j < NA; j++)
		{
			EVENT e;
			fgets(line, 1024, fpIn);
			sscanf(line, "%s %s", hrSaida, hrChegada);
			e.time = timeToMinutes(hrSaida);
			e.type = _saida;
			eventsA.push_back(e);
			e.time = timeToMinutes(hrChegada) + T;
			e.type = _chegada;
			eventsB.push_back(e);
		}

		for(j = 0; j < NB; j++)
		{
			EVENT e;
			fgets(line, 1024, fpIn);
			sscanf(line, "%s %s", hrSaida, hrChegada);
			e.time = timeToMinutes(hrSaida);
			e.type = _saida;
			eventsB.push_back(e);
			e.time = timeToMinutes(hrChegada) + T;
			e.type = _chegada;
			eventsA.push_back(e);
		}

		eventsA.sort();
		eventsB.sort();

		std::list<EVENT>::iterator it;

		disp = 0;
		for(it = eventsA.begin(); it != eventsA.end(); it++)
		{
			EVENT e;
			e = *it;
			if(e.type == _chegada)
			{
				disp++;
			}
			if(e.type == _saida)
			{
				if(disp == 0)
				{
					totalA++;
				}
				else
				{
					disp--;
				}
			}
		}


		disp = 0;
		for(it = eventsB.begin(); it != eventsB.end(); it++)
		{
			EVENT e;
			e = *it;
			if(e.type == _chegada)
			{
				disp++;
			}
			if(e.type == _saida)
			{
				if(disp == 0)
				{
					totalB++;
				}
				else
				{
					disp--;
				}
			}
		}

		printf("%d=> %d %d\r\n", i+1, totalA, totalB);
		fprintf(fpOut, "Case #%d: %d %d\n", i+1, totalA, totalB);
	}


	fclose(fpIn);
	fclose(fpOut);

	return 0;
}

