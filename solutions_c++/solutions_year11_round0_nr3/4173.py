// CandySpilit.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#include <vector>
#include "time.h"


int XORAdd(int x, int y)
{
	int iSum = 0;

	int iPos = 0;
	int ijegop = 1;

	while(1)
	{
		int iBit = x%2  ^ y%2;


		iSum = iSum + iBit * ijegop;// (pow(2.0, iPos));

		ijegop = ijegop * 2;

		iPos++;

		x = x/2;
		y = y/2;

		if(( x == 0) && ( y == 0))
		{
			break;
		}
	}

	return iSum;
}
 
 


FILE *in = fopen( "input.txt" , "r" );
FILE *out = fopen( "output.txt" , "w" );

int inputArray[1000];
int MaxSean;

  
 
int _tmain(int argc, _TCHAR* argv[])
{
	time_t start, end;
	start = clock();

 

	int TestCase;
	fscanf(in, "%d", &TestCase); 

	for(int T = 0; T < TestCase; T++)
	{ 
		int N; 
		int XorTotal = 0;
		int total = 0;

		 



		fscanf(in, "%d", &N); 



		for(int i = 0; i < N ; i++)
		{
			int element;
			fscanf(in, "%d", &element); 
			//input.push_back(element);
			inputArray[i] = element;

			XorTotal = XORAdd(XorTotal, element);
			total = total + element;

		}


		if(XorTotal != 0)
		{
			fprintf(out, "Case #%d: NO\r\n", T+1);
			continue;
		}

 
 
		

		MaxSean = 0;
		for(int j =0 ; j < N ; j++)
		{
			int XORSubTotal = 0;
			int NormalTotal = 0;
			for(int k = 0; k < N; k++)
			{

				if(j != k)
				{
					XORSubTotal = XORAdd(XORSubTotal, inputArray[k]);
					NormalTotal = NormalTotal + inputArray[k];
				}


			}
			if(XORSubTotal == inputArray[j])
			{
				if(NormalTotal > MaxSean)
				{
					MaxSean = NormalTotal;
				} 

			}

		}




		int Answer = MaxSean;
		if(Answer == 0)
			fprintf(out, "Case #%d: NO\r\n", T+1);
		else
			fprintf(out, "Case #%d: %d\r\n", T+1, Answer);

	}



	end = clock();
	double pst = (double)(end-start)/CLK_TCK;
	//fprintf(out, "Time : %f \r\n", pst);

	fclose(in);
	fclose(out);
	return 0;
}

