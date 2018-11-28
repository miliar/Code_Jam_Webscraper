// Train_Timetable.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "stdio.h"
#include <iostream> 
#include <fstream> 
#include <vector> 
#include <list> 
#include <algorithm> 
using namespace std; 

struct TimeTable
{
	int Tdepar;
	int Tarriv; 
	bool bMark; 
	
}; 


bool operator<(const TimeTable& a, const TimeTable&b)
{
	return (a.Tdepar) < (b.Tdepar); 
}

bool
sortVector(const TimeTable &a, const TimeTable  &b) {
	return (a.Tdepar) < (b.Tdepar);
}


int _tmain(int argc, _TCHAR* argv[])
{
	
	
	fstream file_op("arq.txt",ios::in);
	fstream file_Out("arqOut.txt",ios::out); 

	int nCases, T, NA, NB; 
	char ch[255]; 
	
	




	TimeTable lineA;
	TimeTable lineB; 

	vector<TimeTable> vA;
	vector<TimeTable> vB; 

	file_op >> nCases; 
	int nPos = 1; 

	//while(!file_op.eof())
	for(int k = 0 ; k < nCases ; k++)
	{
		
		vA.erase(vA.begin(),vA.end());
		vB.erase(vB.begin(),vB.end()); 
		file_op >> T; 
		file_op >> NA;
		file_op >> NB; 


		string str,subStr; 
		int minutes;
		for(int i =0 ; i < NA; i++)
		{
			file_op >> ch; 
			str = ch; 
			subStr = str.substr(0,2);
			minutes = atoi(subStr.c_str())*60;
			subStr = str.substr(3,4);
			minutes+= atoi(subStr.c_str());
			lineA.Tdepar  = minutes; 
			
			file_op >> ch; 
			str = ch; 
			subStr = str.substr(0,2);
			minutes = atoi(subStr.c_str())*60;
			subStr = str.substr(3,4);
			minutes+= atoi(subStr.c_str());
			lineA.Tarriv = minutes; 
			lineA.bMark = false; 

			vA.push_back(lineA); 
			
		}
		
		for(int i = 0 ; i < NB; i++)
		{
			file_op >> ch; 
			str = ch; 
			subStr = str.substr(0,2);
			minutes = atoi(subStr.c_str())*60;
			subStr = str.substr(3,4);
			minutes+= atoi(subStr.c_str());
			lineB.Tdepar  = minutes; 
			 
			file_op >> ch; 
			str = ch; 
			subStr = str.substr(0,2);
			minutes = atoi(subStr.c_str())*60;
			subStr = str.substr(3,4);
			minutes+= atoi(subStr.c_str());
			lineB.Tarriv = minutes; 
			lineB.bMark = false; 

			vB.push_back(lineB); 

		}
		std::sort(vA.begin(),vA.end(),sortVector); 
		std::sort(vB.begin(),vB.end(),sortVector); 


		int MaxTrainA = NA; 
		int MaxTrainB = NB; 

		for(int i=0; i < vA.size(); i++)
		{
			int min = vA[i].Tarriv;
			for(int j =0 ; j < vB.size() ; j++)
			{
				if(min <=(vB[j].Tdepar-T) && !vB[j].bMark)
				{
					MaxTrainB--;
					vB[j].bMark = true; 
					break;
				} 
			}
		}

		for(int i=0; i < vB.size(); i++)
		{
			int min = vB[i].Tarriv;
			for(int j =0 ; j < vA.size() ; j++)
			{
				if(min <=(vA[j].Tdepar-T) && !vA[j].bMark)
				{
					MaxTrainA--;
					vA[j].bMark = true; 
					break; 
				} 
			}
		}
		
		cout << "Case #" << k+1 << ": " << MaxTrainA << " " << MaxTrainB << endl; 
		file_Out << "Case #" << k+1 << ": " << MaxTrainA << " " << MaxTrainB << endl; 

		nPos++; 
	}

	
		
	return 0;
}


 