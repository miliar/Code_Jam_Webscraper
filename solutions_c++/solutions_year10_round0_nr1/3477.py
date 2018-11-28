#include "stdafx.h"
#include <conio.h>
#include <iostream>
#include <algorithm>
#include <vector>

#define INPUTF "A-large.in"
#define OUTPUTF "A-large.out"

using namespace std;

__int64 power(__int64 t, __int64 k) 
{
	// возведение t в степень k
	int res = 1;
	while (k) 
	{
		if (k & 1) res *= t;
		t *= t;
		k >>= 1;
	}
	return res;
}


bool Check(__int64 NumberOfDevices, __int64 Times)
{
	__int64 Kb = 0;

	if(Times==0)
		return false;

	for (int i=0;i<NumberOfDevices;i++)
	{
		Kb+= power(2,i);
	}
	
	if(Times<Kb)
		return false;

//	__int64 K = Times/Kb;

	if(((Times+1)%(Kb+1))==0)
		return true;
	else 
		return false;
}



int _tmain(int argc, _TCHAR* argv[])
{
	__int64 T;
	
/*	cin>>N>>K;
	if(Check(N,K))
		cout<<"ON";
	else
		cout<<"OFF";
	*/

	FILE *Input,*Output,*Output2;
	Input = fopen(INPUTF, "r");
	Output = fopen(OUTPUTF, "w");
//	Output2 = fopen(OUTPUTF2, "w");

	string res, res2;

	fscanf(Input,"%lld",&T);
	for (int i=0;i<T;i++)
	{
		__int64 N = 1;
		__int64 K = 0;

		fscanf(Input,"%lld%lld",&N,&K);
		if(Check(N,K))
		{
			res = "ON";
		}
		else
		{
			res = "OFF";
		}
		

		if (i!=(T-1))
		{
			fprintf(Output,"Case #%d: %s\n",i+1,res.c_str());
//			fprintf(Output2,"Case #%d: %s\n",i+1,res2.c_str());
		}
		else
		{
			fprintf(Output,"Case #%d: %s",i+1,res.c_str());
//			fprintf(Output2,"Case #%d: %s",i+1,res2.c_str());
		}
	}

	fclose (Input);
	fclose (Output);
//	fclose (Output2);

//	getch();

	return 0;
}

