// Google Dancing Googlers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int highest(int a, int b, int c)
{
	int High = a;
	if (b > High) 
	{
		High = b;
	}
	if (c > High)
	{
		High = c;
	}
	return High;
}

int lowest(int a, int b, int c)
{
	int High = a;
	if (b < High) 
	{
		High = b;
	}
	if (c < High)
	{
		High = c;
	}
	return High;
}

vector<int> StrListToIntVector(string Input, char LeftSeperator, char RightSeperator)
{
	vector<int> IntList;
	string Sector;
	for ( int Active = 0 ; Active < Input.length() ; Active = ( Input.find( RightSeperator, Active+1  ) ) ) 
	{
		Sector = Input.substr( Active , Input.find(' ', Active+1 ) );
		//cout<<  "( "<<Active << " " << Sector << " ), "<< endl;
		IntList.push_back( atoi(Sector.c_str()) );
	}
	/*
	for ( int i = 0; i < IntList.size(); i++)
	{
		cout<<IntList[i]<<endl;
	}
	*/
	return IntList;
}


int gettotal(vector<int> Input)
{
	vector<int> NotNormal = Input;
	int p = Input[2];
	int Normal = 0;
	bool Found = false;
	for ( int g = 3; g < Input.size(); g++ ) 
	{
		int Total = Input[g];
		
		for (int a = 0; a <= 10 && !Found ; a++ )
		{
			for (int b = 0; b <= 10 && !Found; b++)
			{
				for (int c = 0; c <= 10 && !Found; c++)
				{
					if( (a + b + c) == Total && !Found )
					{
						if ( highest(a, b, c) - lowest(a, b, c) < 2 && (a >= p || b >= p || c >= p) && !Found )
						{
							Normal++;
							Found = true;
							NotNormal[g] = 0;
						}
					}
				}
			}
		
		}
		Found = false;
	}
	//-----------------------
	Found = false;
	int OnlyStrange = 0;
	for ( int g = 3; g < NotNormal.size(); g++ ) 
	{
		int Total = NotNormal[g];
		
		for (int a = 0; a <= 10 && !Found ; a++ )
		{
			for (int b = 0; b <= 10 && !Found; b++)
			{
				for (int c = 0; c <= 10 && !Found; c++)
				{
					if( (a + b + c) == Total && !Found )
					{
						if ( highest(a, b, c) - lowest(a, b, c) == 2 && (a >= p || b >= p || c >= p) && !Found )
						{
							OnlyStrange++;
							Found = true;
						}
					}
				}
			}
		
		}
		Found = false;
	}
	if (OnlyStrange >= Input[1])
	{
		return Normal + Input[1];
	}
	else
	{
		return Normal + OnlyStrange;
	}
}
int main()
{


	ifstream InputFile;
	InputFile.open("B-large.in");
	if (!InputFile.is_open())
	{
		cout<< "fail.";
		cin.get();
		return 1;
	}
	string Max;
	vector<int> Totals;
	vector<int> Numbers;
	getline(InputFile, Max);
	int Cases = atoi(Max.c_str());
	for ( int i = 0; i < Cases; i++)
	{
		getline(InputFile, Max);
		cout<<Max<<endl;
		Numbers = StrListToIntVector(Max, ' ', ' ' );
		Totals.push_back(gettotal(Numbers));
		Numbers.clear();
	}
	ofstream OutputFile;
	OutputFile.open("Output.txt");
	for ( int i = 0; i < Totals.size(); i++)
	{
		OutputFile<<"Case #"<<i+1<<": "<<Totals[i]<<endl;
	}



	cin.get();








	/*
	int Total = 0;
	int p = 8;
	cin>>Total;
	bool Strange = false;
	bool Normal = false;
	for (int a = 0; a <= 10; a++)
	{
		for (int b = 0; b <= 10; b++)
		{
			for (int c = 0; c <= 10; c++)
			{
				if( (a + b + c) == Total )
				{
					if ( highest(a, b, c) - lowest(a, b, c) < 2 && (a >= p || b >= p || c >= p) )
					{
						Normal = true;
					}

				}
			}
		}
	}
	cout<<Normal;
	 
	cin.get();
	cin.get();
	*/
}




