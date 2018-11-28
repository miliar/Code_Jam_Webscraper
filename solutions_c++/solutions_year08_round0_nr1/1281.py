#include <iostream>
#include <fstream>
#include <string>
#include <conio.h>
using namespace std;

int main()
{
	int Cases = 0;
	int CurrentCase = 1;
	int NumOfEngines = 0;
	int NumOfQueries = 0;

	int ChangePoint = 0;
	int Temp_ChangePoint = 0;
	int Current_ChangePoint = 0;

	int Count = -1;
	int UpCounter = 1;

	string Temp_String;
	ifstream Input;
	ofstream Output;

	Input.open("A.in");
	Output.open("Out.txt");

	getline(Input,Temp_String);
	Cases = atoi(Temp_String.c_str());

	while(Cases)
	{
		NumOfEngines = 0;

		getline(Input,Temp_String);
		NumOfEngines = atoi(Temp_String.c_str());

		string* Engines = new string[NumOfEngines];

		for(int i = 0 ; i < NumOfEngines ; i++)
			getline(Input,Engines[i]);
	
		NumOfQueries = 0;

		getline(Input,Temp_String);
		NumOfQueries = atoi(Temp_String.c_str());

		string* Queries = new string[NumOfQueries];

		for (int i = 0 ; i < NumOfQueries ; i++)
			getline(Input,Queries[i]);

		ChangePoint = 0;
		while (ChangePoint != NumOfQueries)
		{
			Temp_ChangePoint = 0;
			for (int i = 0 ; i < NumOfEngines ; i++)
			{	
				Current_ChangePoint = 0;

				for (int j = ChangePoint ; j < NumOfQueries ; j++)
					if (Engines[i] != Queries[j])
						Current_ChangePoint++;
					else
						break;

				if (Current_ChangePoint > Temp_ChangePoint)
					Temp_ChangePoint = Current_ChangePoint;	
			}
			Count++;
			ChangePoint += Temp_ChangePoint;
		}

		Output<<"Case #"<<UpCounter<<": "<<Count<<endl;
		UpCounter++;
		Cases--;
	}
	return 0;
}