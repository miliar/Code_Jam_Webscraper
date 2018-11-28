#include<iostream>
#include<string>
#include<fstream>
using namespace std;
ifstream fin;
ofstream fout;
struct Robot
{
	int Button;
	char Color;
	int Current;
};
int GetDifferentColor(int, Robot* , int );
void main()
{
	int No_Test_Cases = 0;
	
	fin.open("input.in", ios::in);
	fout.open("Output.txt", ios::out);

	fin>> No_Test_Cases;

	Robot** Robot_Obj = new Robot*[No_Test_Cases];
	int* Cases = new int[No_Test_Cases];
	int* Output = new int[No_Test_Cases];
	for(int i=0;i<No_Test_Cases;i++)
	{
		fin>> Cases[i];
		Output[i] = 0;
		Robot_Obj[i] = new Robot[Cases[i]];
		for(int j=0;j<Cases[i];j++)
		{
			fin>>Robot_Obj[i][j].Color;
			fin>>Robot_Obj[i][j].Button;
			Robot_Obj[i][j].Current = 1;
		}
	}

	int Counter = 0;
	int differentColor = 0;
	for(int C=0;C<No_Test_Cases;C++)
	{
		while(Counter < Cases[C])
		{
			differentColor = GetDifferentColor(Counter,Robot_Obj[C],Cases[C]);
			if(differentColor != -1)
			{
				//if(Robot_Obj[C][Counter].Button >)
				if(Robot_Obj[C][differentColor].Button != Robot_Obj[C][differentColor].Current) // It's probable to find it back not forward
				{
					if(Robot_Obj[C][differentColor].Button >Robot_Obj[C][differentColor].Current)
						Robot_Obj[C][differentColor].Current++;
					else
						Robot_Obj[C][differentColor].Current--;
				}
			}
				
					if(Robot_Obj[C][Counter].Button >Robot_Obj[C][Counter].Current)
					{
						Robot_Obj[C][Counter].Current++;
						Output[C]++;
						//Counter++;
					}
					else if(Robot_Obj[C][Counter].Button < Robot_Obj[C][Counter].Current)
					{
						Robot_Obj[C][Counter].Current--;
						Output[C]++;
						//Counter--;
					}
					else
					{
						Output[C]++;
						for(int k=Counter;k<Cases[C];k++)
						{
							if(Robot_Obj[C][Counter].Color == Robot_Obj[C][k].Color)
								Robot_Obj[C][k].Current = Robot_Obj[C][Counter].Current;
						}
						Counter++;
					}

				
				
			}
			Counter = 0;
			differentColor = -1;
		}

		for(int i=0;i<No_Test_Cases;i++)
		{
			fout<<"Case #"<<i+1<<":"<<" "<<Output[i]<<endl;
		}
		fout.close();
		fin.close();
	}



int GetDifferentColor(int Start, Robot* Array, int Array_Size)
{
	for(int i=Start;i< Array_Size;i++)
	{
		if(Array[i].Color != Array[Start].Color)
			return i;
	}
	return -1;
}