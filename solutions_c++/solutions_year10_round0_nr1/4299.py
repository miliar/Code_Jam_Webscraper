#include <Windows.h>
#include <iostream>
#include <fstream>

#define IN_FILE "A-small-attempt0.in"
#define OUT_FILE "A-small-attempt0.out"

using namespace std;

void SnapFingers(int *states, int *powers, int N)
{
	for (int i=0;i<N;i++)
	{
		if (powers[i] == 1)
		{
			if (states[i] == 1)
			{
				states[i] = 0;
			}else{
				states[i] = 1;
			}
		}
		else
		{
			break;
		}
	}
	
	powers[0] = 1;
	if (N>1)
	{
		int cut = 1;
		for (int j=1;j<N;j++)
		{
			if (states[j - 1] ==1 && cut == 1)
			{
				powers[j] = 1;
			}else{
				powers[j] = 0;
				cut = 0;
			}
		}
	}
}

bool AllOn(int * states,int N)
{
	for (int i=0;i<N;i++)
	{
		if (states[i] != 1)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int caseNum;
	int N,K;
    ifstream in(IN_FILE);
	ofstream out(OUT_FILE);
    in >> caseNum;
	for (int n=0;n<caseNum;n++)
	{
		in >>N;
		in >>K;
		if (K == 0 || (K % 2) != 1)
		{
			out << "Case #" << n+1 << ":"<< ' '<<"OFF" <<"\n";
		}else{
			int * states = new int [N];
			int * powers = new int [N];
			memset(states,0,N);
			memset(powers,0,N);
			powers[0] = 1;
			//SnapFingers(states,powers,N);
			int times = 0;
			do 
			{
				SnapFingers(states,powers,N);
				times++;
			} while (times < K && !AllOn(states,N));
			if (AllOn(states,N) && ((K+1) % (times +1) )== 0)
			{
				out << "Case #" << n+1 << ":"<< ' '<<"ON" <<"\n";
			}else{
				out << "Case #" << n+1 << ":"<< ' '<<"OFF"<<"\n" ;
			}
		}
	}
	return 0;
}
