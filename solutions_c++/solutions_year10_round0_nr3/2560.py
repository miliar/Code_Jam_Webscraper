#include <iostream>
#include <fstream>
#include <string.h>
#include <conio.h>

using namespace std;

enum BOOL {FALSE, TRUE};

int T, R, k, N, queue[1000], AccumQueue[1000], head;
long Total;
ifstream ifile;
ofstream ofile;

void Input();
void Calculate();


void main()
{
	int i;

	ifile.open("C-small-attempt0.in");
	ofile.open("C-small-attempt0.out");

	ifile >> T;


	for ( i = 0; i < T; i++)
	{
		head = 0;
		Total = 0;
		Input();
		Calculate();
		ofile << "Case #" << i+1 << ": ";
		ofile << Total << endl;
	}

	ifile.close();
	ofile.close();
}

void Input()
{
	int i;

	ifile >> R >> k >> N;

	ifile >> queue[0];
	AccumQueue[0] = queue[0];
	for(i = 1; i < N; i++)
	{
		ifile >> queue[i];
		AccumQueue[i] = AccumQueue[i-1] + queue[i];
	}
}

void Calculate()
{
	int i, remain= 0, o;

	for(i = 0; i < R; i++)
	{
		if(k > AccumQueue[N - 1])
		{
			Total += AccumQueue[N - 1];
			continue;
		}

		remain = k;
		if(head != 0 && remain >= AccumQueue[N - 1] - AccumQueue[head - 1])
		{
			Total += (AccumQueue[N - 1] - AccumQueue[head - 1]);
			remain -= (AccumQueue[N - 1] - AccumQueue[head - 1]);
			head = 0;
		}

		while(head < N)
		{
			if(remain < queue[head])
				break;
			Total += queue[head];
			remain -= queue[head++];
		}
	}
}