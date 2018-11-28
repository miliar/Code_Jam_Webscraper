#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>
using namespace std;

int TimeInMin(string Time);
void TimeSort(string **TimeArray, int Size);

int main()
{
	int Cases = 0;
	int UpCounter = 1;
	int TurnAoundTime = 0;
	int NA = 0;
	int NB = 0;
	string** TimeA;
	string** TimeB;
	int NeededTrainsA = 0;
	int NeededTrainsB = 0;
	bool* CheckA;
	bool* CheckB;
	string Temp_String;

	ifstream Input;
	ofstream Output;

	Input.open("B.in");
	Output.open("Out.txt");

	getline(Input,Temp_String);
	Cases = atoi(Temp_String.c_str());

	while(Cases)
	{

		getline(Input,Temp_String);
		TurnAoundTime = atoi(Temp_String.c_str());

		getline(Input,Temp_String);
		NA = atoi(Temp_String.substr(0,Temp_String.find(" ")).c_str());
		NB = atoi(Temp_String.substr(Temp_String.find(" ")+1,Temp_String.size()-Temp_String.find(" ")).c_str());

		CheckA = new bool[NA];
		for (int i = 0 ; i < NA ; i++)
			CheckA[i] = true;
		TimeA = new string*[NA];
		for (int i = 0 ; i < NA ; i++)
			TimeA[i] = new string[2];

		CheckB = new bool[NB];
		for (int i = 0 ; i < NB ; i++)
			CheckB[i] = true;
		TimeB = new string*[NB];
		for (int i = 0 ; i < NB ; i++)
			TimeB[i] = new string[2];

		NeededTrainsA = NA;
		NeededTrainsB = NB;

		for (int i = 0 ;  i < NA ; i++)
		{
			getline(Input,Temp_String);
			TimeA[i][0] = Temp_String.substr(0,Temp_String.find(" "));
			TimeA[i][1] = Temp_String.substr(Temp_String.find(" ")+1,Temp_String.size()-Temp_String.find(" "));
		}
		
		for (int i = 0 ;  i < NB ; i++)
		{
			getline(Input,Temp_String);
			TimeB[i][0] = Temp_String.substr(0,Temp_String.find(" "));
			TimeB[i][1] = Temp_String.substr(Temp_String.find(" ")+1,Temp_String.size()-Temp_String.find(" "));
		}
		TimeSort(TimeB,NB);
		TimeSort(TimeA,NA);

		for (int i = 0 ;  i < NA ; i++)
		{
			for (int j = 0 ; j < NB ; j++)
				if (((TimeInMin(TimeA[i][1])+TurnAoundTime) <= TimeInMin(TimeB[j][0])) && CheckB[j])
				{
					NeededTrainsB--;
					CheckB[j] =  false;
					break;
				}
		}

		for (int i = 0 ;  i < NB ; i++)
		{
			for (int j = 0 ; j < NA ; j++)
				if (((TimeInMin(TimeB[i][1])+TurnAoundTime) <= TimeInMin(TimeA[j][0])) && CheckA[j])
				{
					NeededTrainsA--;
					CheckA[j] =  false;
					break;
				}
		}

		
		if (Cases == 1)
			Output<<"Case #"<<UpCounter<<": "<<NeededTrainsA<<" "<<NeededTrainsB;
		else
			Output<<"Case #"<<UpCounter<<": "<<NeededTrainsA<<" "<<NeededTrainsB<<endl;
		UpCounter++;
		Cases--;
	}
	return 0;
}

int TimeInMin(string Time)
{
	return (atoi(Time.substr(0,2).c_str())*60)+(atoi(Time.substr(3,2).c_str()));
}

void TimeSort(string** TimeArray, int Size)
{
	int MinLoc = 0;
	for (int i = 0 ; i < Size ; i++)
	{
		MinLoc = i;
		for (int j = i+1 ; j < Size ; j++)
			if (TimeInMin(TimeArray[j][0]) < TimeInMin(TimeArray[MinLoc][0]))
				MinLoc = j;
		swap(TimeArray[i][0],TimeArray[MinLoc][0]);
		swap(TimeArray[i][1],TimeArray[MinLoc][1]);
	}
}