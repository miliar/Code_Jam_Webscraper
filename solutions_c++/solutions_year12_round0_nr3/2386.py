// ProgramC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <Windows.h>

using namespace std;

#define fabc(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fa0c(a,b) fabc( a, 0, ( b ) )
#define for_i(a) fa0c( i, ( a ) )
#define for_j(a) fa0c( j, ( a ) )
#define for_k(a) fa0c( k, ( a ) )

//A <= n < m <= B
int RecycledPairs(int A, int B);
void Rotate(char* buffer, char* outBuffer, int Size);

int _tmain(int argc, _TCHAR* argv[])
{
	LARGE_INTEGER start, finish, freq;
	QueryPerformanceFrequency(&freq);



	int i,j,k;

	fstream f_input, f_output;
	f_input.open(argv[1],fstream::in);
	f_output.open("ProgramCOut.txt",fstream::out);


	//read test cases
	int T = 0;
	f_input >> T;
	for_i(T)
	{
		int A,B;
		f_input >> A;
		f_input >> B;
		QueryPerformanceCounter(&start);
		int numPairs = RecycledPairs(A,B);
		QueryPerformanceCounter(&finish);
		cout << "Case #" << i+1 <<": " << numPairs << " Time:" << ((finish.QuadPart - start.QuadPart) / (double)freq.QuadPart) << endl;
		f_output << "Case #" << i+1 <<": " << numPairs << endl;
	}
	

	f_input.close();
	f_output.close();
	return 0;
}

int RecycledPairs(int A, int B)
{
	int i;
	int RecycledPairs = 0;
	fabc(i, A, B)
	{
		char buffer[100];
		char buffer2[100];
		char i_buffer[100];
		memset(buffer,0,100);
		memset(buffer2,0,100);
		memset(i_buffer,0,100);
		_itoa(i,buffer,10);
		memcpy(i_buffer,buffer,100);

		Rotate(buffer,buffer2, strlen(buffer));
		int rotated = atoi(buffer2);
		do
		{
			if(rotated > i && rotated <= B)
				RecycledPairs++;

			memcpy(buffer,buffer2,100);
			memset(buffer2,0,100);
			Rotate(buffer,buffer2, strlen(buffer));
			rotated = atoi(buffer2);
		}while(strcmp(buffer2,i_buffer)!=0);
	}
	return RecycledPairs;
}

void Rotate(char* buffer, char* outBuffer, int Size)
{
	int i;
	for_i(Size)
	{
		outBuffer[(i+1)%(Size)] = buffer[i%(Size)];
	}
}
