#include <iostream>
#include <fstream>

#include <math.h>

using namespace std;

int a, b;

int n, m;

int noOfDigits;

int res[50];

int noOfRotations = 0;

int digitPairs = 0;

int CalculateDigits(int x);

int CalculateRangeOf(int x)
{
	if(x > a && x<= b)
	{
		return 1;
	}
	return 0;
}

void CalculateNewValue()
{
	int temp = n;

	while(noOfRotations < noOfDigits - 1)
	{	
		m = temp%((int)pow(10.0, noOfDigits - 1)) * 10 + (temp / (int)pow(10.0, noOfDigits - 1));	
		
		if(m == n)
		{
			temp = m;

			noOfRotations++;
		}
		else if(m < n)
		{
			noOfRotations++;

			int newDigitLength = CalculateDigits(m);

			if(newDigitLength < noOfDigits)
			{
				newDigitLength = noOfDigits - newDigitLength;
			

				noOfRotations += newDigitLength;
		
				m = m * (int)pow(10.0, newDigitLength);		

				if(m > n && CalculateRangeOf(m))
				{
					digitPairs ++;					
				}
			}

			temp = m;
		}
		else
		{
			noOfRotations++;
			int ret = CalculateRangeOf(m);

			if(ret == 1)
			{	
				digitPairs ++;				
			}	

			temp = m;
		}
	}
}

int CalculateDigits(int x)
{
	int num = x, i;

	for(i = 0; num != 0; i ++)
	{
		num = num / 10;
	}

	return i;
}

void RecurssiveCalc(int i)
{
	n = a;

	while(n <= b)
	{
		CalculateNewValue();		

		noOfRotations = 0;

		n++;
	}

	res[i] = digitPairs;		

	digitPairs = 0;
}

void main()
{
	int t;	

	ifstream fileIn;
	ofstream fileOut;

	fileIn.open("input.in", ios::in|ios::_Nocreate);

	fileOut.open("ouput.out", ios::out);

	fileIn>>t;

	for(int i = 0; i < t; i++)
	{
		fileIn>>a>>b;

		noOfDigits = CalculateDigits(a);

		RecurssiveCalc(i);
	}

	for(int i = 0; i<t; i++)
	{
		fileOut<<"Case #"<<i + 1<<": "<<res[i]<<endl;
	}

	fileIn.close();
	fileOut.close();
}