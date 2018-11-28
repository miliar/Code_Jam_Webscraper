//============================================================================
// Name        : third.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
const int MAXM = 512;
const int MAXN = 512;


int chess[MAXM][MAXM];


int f(char ch);
int min(int,int);
int legal(int chess[MAXM][MAXM], int, int, int);


int main() {

	int T, t;
	int M, N, m, n;
	char ch;
	int count[MAXM];
	cin >> T;
	for ( t = 0; t < T; t++)
    {
		//input
		cin >> M;
		cin >> N;

		for (m = 0; m < MAXM; m++)
			count[m] = 0;

		for (m = 0; m < M; m++)
		{
			for (n = 0; n < N/4; n++)
			{
				cin >> ch;
				int value = f(ch);
				chess[m][n*4]  = value/8;
				chess[m][n*4+1]= (value%8)/4;
				chess[m][n*4+2]=  (value%4)/2;
				chess[m][n*4+3]=  value%2;
			}

		}

	    int curM, curN, curSize;
	    curM = 0;
	    curN = 0;
	    curSize = 0;
	    int size = 0;
	    while(1)
	    {
	       for (m = 0; m < M; m++)
		        for (n = 0; n < N; n++)
		        {
		        	 int lg = -1;
			         for (size = min(M-m, N-n); size >0; size--)
				      {
			        	  lg = legal(chess, m, n, size);
				          if (lg == 1)
			              {
			    	         if (size > curSize)
			    	         {
			    		      curM = m;
			    		      curN = n;
			    		      curSize = size;

			    	           continue;
			                  }
			             }
				      }

		        }


	       if (curSize == 0)
	    	   break;
	        count[curSize]++;
	        for (m = curM; m < curM + curSize; m++)
	    	   for (n = curN; n < curN + curSize; n++)
	    		   chess[m][n] = -1;
  	   }

	   cout << "Case #" << t+1 << ": ";
       int num = 0;
	   for (m = MAXM -1; m >= 1; m--)
		  if (count[m] != 0)
			  num++;


       cout << num << endl;

       for (m = MAXM -1; m >= 1; m--)
    	  if (count[m] != 0)
    		  cout << m <<"  " << count[m] << endl;

    }
	return 0;
}

int legal(int chess[MAXN][MAXN], int startRow, int startColumn, int size)
{

	int i, j;

	for (i = 0; i < size; i++)
			for (j = 0; j < size; j++)
				if (chess[startRow+i][startColumn+j] == -1)
					return 0;

	for (i = 0; i < size; i++)
		for (j = 0; j < size-1; j++)
			if (chess[startRow+i][startColumn+j] == chess[startRow+i][startColumn+j+1])
				return 0;
	for (j = 0; j < size; j++)
		for (i = 0; i < size-1; i++)
			if ( chess[startRow+i][startColumn+j] == chess[startRow+i+1][startColumn+j])
				return 0;
	return 1;
}

int min(int a, int b)
{
	if (a > b)
		return b;
	else
		return a;
}
int f(char ch)
{
  if ((ch >= '0') && (ch <= '9'))
		  return ch-'0';
  return ch-'A' + 10;
}
