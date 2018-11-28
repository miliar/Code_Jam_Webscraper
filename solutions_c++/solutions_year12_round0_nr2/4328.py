#include <iostream>
#include <fstream>

using namespace std;

int res[100];

int g[100], n, p, s;

int t;

int x;

int surpriseFound = 0;

int surpriseCount = 0;

void GetSurpriseAvailable(int rem, int j, int i)
{
	int val;

	if(rem == 0)
	{
		val = g[j] / 3;

		if(val >= p)
		{
			res[i] ++;
		}
		else if(val + 1 >= p && val != 0)
		{
			surpriseCount ++;			

			res[i] ++;
		}				
	}
	else if(rem == 1)
	{
		val = (g[j] - 1) / 3;

		if(val >= p)
		{
			res[i] ++;
		}
		else if(val + 1 >= p)
		{
			surpriseCount ++;

			res[i] += 2;
		}		
	}
	else if(rem == 2)
	{
		val = (g[j] - 2) / 3;

		if(val >= p || val + 1>= p)
		{
			res[i] ++;
		}
		else if(val + 2 >= p)
		{
			surpriseCount ++;

			res[i] ++;
		}
	}
}

void SubtractSurprises(int i)
{
	if(surpriseCount > s)
	{
		res[i] = res[i] - (surpriseCount - s);
	}
}

void Compute(int i)
{
	int rem = 0;
	for(int j = 0; j < n; j++)
	{
		rem = g[j] % 3;

		GetSurpriseAvailable(rem, j, i);		
	}

	SubtractSurprises(i);
}

void main()
{

	ifstream fileIn;
	ofstream fileOut;

	fileIn.open("input.in", ios::in|ios::_Nocreate);

	fileOut.open("ouput.out", ios::out);

	fileIn >> t;

	for(int i=0 ; i<t; i++)
	{
		fileIn>>n>>s>>p;

		for(int j = 0; j<n; j++)
		{
			fileIn>>g[j];
		}	

		Compute(i);

		surpriseFound = 0;

		surpriseCount = 0;
	}

	for(int i = 0; i<t; i++)
	{
		fileOut<<"Case #"<<i+1<<": "<<res[i]<<endl;
	}

	fileIn.close();
	fileOut.close();
}