#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std;

char* IntegerToChar(int Number,int r_Base = 10);
void main()
{
	ifstream fin("C-small-attempt1.in"); //namenum.in , namenum.txt
	ofstream fout("C-small-attempt1.out"); // namenum.out , namenumout.txt
	int testCases = 0;
	int**numbers = NULL;

	fin>>testCases;
	numbers = new int*[testCases];
	int* Counters = new int[testCases];

	for(int i=0;i<testCases;i++)
	{
		Counters[i] = 0;
		numbers[i] = new int[2];
		for(int j=0;j<2;j++)
			fin>>numbers[i][j];
	}

	for(int i=0;i<testCases;i++)
	{
		int n = numbers[i][0];
		int m = numbers[i][1];
		if(n<10 && m < 10)
		{
			Counters[i] = 0;
			continue;
		}
		for(int j=n;j<m;j++)
		{
			char* match = IntegerToChar(j);
			for(int k= j+1;k<=m;k++)
			{
				char* match2 = IntegerToChar(k);
				if(strcmp(match, match2) == 0)
					Counters[i]++;
				else
				for(int l=1;l<(int)strlen(match);l++)
				{
					char* match3 = new char[strlen(match) + 1];
					int u;
					for(int r=l,u=0;r<(int)strlen(match);r++,u++)
						match3[u] = match[r];
					match3[(int)strlen(match)] = '\0';
					int e;
					for(int s=0,e=(int)strlen(match)-l;s<l;s++,e++)
						match3[e] = match[s];
					if(strcmp(match3, match2) == 0)
					{
						Counters[i]++;
						delete[]match3;
						break;
					}
				}
				delete[]match2;
			}
			delete[]match;
		}
	}
	for(int i=0;i<testCases;i++)
		fout<<"Case #"<<i+1<<": "<<Counters[i]<<endl;
	fout.close();
	fin.close();
}

char* IntegerToChar(int Number,int r_Base)
{
	char s_Array[20];
	int Counter = 0;
	//char* Number_C = NULL;
	int Temp = Number;
	int Reminder = Number;
	while(true)
	{
		Reminder %= r_Base;
		Temp /= r_Base;
		if(Reminder == 0)
			s_Array[Counter++] = '0';
		else if(Reminder == 1)
			s_Array[Counter++] = '1';
		else if(Reminder == 2)
			s_Array[Counter++] = '2';
		else if(Reminder == 3)
			s_Array[Counter++] = '3';
		else if(Reminder == 4)
			s_Array[Counter++] = '4';
		else if(Reminder == 5)
			s_Array[Counter++] = '5';
		else if(Reminder == 6)
			s_Array[Counter++] = '6';
		else if(Reminder == 7)
			s_Array[Counter++] = '7';
		else if(Reminder == 8)
			s_Array[Counter++] = '8';
		else if(Reminder == 9)
			s_Array[Counter++] = '9';
		if(Temp == 0)
			break;
		Reminder = Temp;
	}
	
	char* Array = NULL;
	Array = new char[Counter+1];
	int S = 0;
	for(int i=Counter-1;i>=0;i--)
	{
		Array[S++] = s_Array[i];
	}
	Array[Counter] = '\0';
	return Array;
}