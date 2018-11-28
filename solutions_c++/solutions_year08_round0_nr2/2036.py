
//#include <typeinfo>
//#include <stdio.h>
//#include <stdlib.h>      /* for malloc, free */
//#include <ctype.h>       /* for isupper, islower, tolower */


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <stdlib.h>
using namespace std;




int main(int argc, char * argv[])
{  
	char* InFileName = "B-large.in";
	char* OutFileName = "B-large.out";
	ifstream fileIn;
	ofstream fileOut; 

	fileIn.open(InFileName);
	fileOut.open(OutFileName);
	if(!fileIn)
		cout<<"Input file Open ERROR"<<endl;
	if(!fileOut)
		cout<<"Output file Open ERROR"<<endl;

	int totalCaseNum;
	fileIn>>totalCaseNum;
	cout<<"CaseNum: "<<totalCaseNum<<endl;

	for(int i = 0; i < totalCaseNum; i++)
	{
		int turnTime;
		int A_tripnum,B_tripnum;
		char ch;
		fileIn>>turnTime;
		fileIn>>A_tripnum>>B_tripnum;
		//fileIn;
		//cout<<"A: "<<A_tripnum<<"   B: "<<B_tripnum<<endl;

		list<int>A2B_leave;
		list<int>B2A_leave;
		list<int>A2B_arrive;
		list<int>B2A_arrive;

		for (int j = 0; j< A_tripnum; j ++) //A to B
		{
			int hour,min;
			fileIn>>hour>>ch>>min;
			//cout<<hour<<":"<<min<<endl;
			int time_in_min = hour * 60 + min;
			A2B_leave.push_back(time_in_min);

			fileIn>>hour>>ch>>min;
			//cout<<hour<<":"<<min<<endl;
			time_in_min = hour * 60 + min;
			A2B_arrive.push_back(time_in_min);			
		}
		for (int j = 0; j< B_tripnum; j ++)//B to A
		{
			int hour,min;
			fileIn>>hour>>ch>>min;
			//cout<<hour<<":"<<min<<endl;
			int time_in_min = hour * 60 + min;
			B2A_leave.push_back(time_in_min);

			fileIn>>hour>>ch>>min;
			//cout<<hour<<":"<<min<<endl;
			time_in_min = hour * 60 + min;
			B2A_arrive.push_back(time_in_min);			
		}

		A2B_leave.sort();
		B2A_leave.sort();
		A2B_arrive.sort();
		B2A_arrive.sort();

		unsigned int A_have, A_must,B_have,B_must;
		A_have = A_must = B_have = B_must = 0;
		
		for (int curtime = 0; curtime <= 60*24; curtime++)
		{
			//A station arrive
			while(1)
			{
				if (B2A_arrive.size() > 0)
				{
					int arriveA = *B2A_arrive.begin();
					if (curtime >= arriveA + turnTime)
					{
						B2A_arrive.pop_front();
						A_have ++;
					}
					else
						break;
				}
				else
					break;
			}
			
			//B station arrive
			while(1)
			{
				if(A2B_arrive.size() > 0)
				{
					int arriveB = *A2B_arrive.begin();
					if (curtime >= arriveB + turnTime)
					{
						A2B_arrive.pop_front();
						B_have ++;
					}
					else
						break;
				}
				else
					break;
			}

			//A station leave
			while(1)
			{
				if(A2B_leave.size() > 0)
				{			
					int A_leave = *A2B_leave.begin();			
					if(curtime >= A_leave)
					{
						A2B_leave.pop_front();
						if(A_have > 0)
							A_have --;
						else
							A_must ++;
					}
					else
						break;
				}
				else
					break;
			}
			//B station leave
			while(1)
			{
				if (B2A_leave.size() > 0)
				{
					int B_leave = *B2A_leave.begin();			
					if(curtime >= B_leave)
					{
						B2A_leave.pop_front();
						if(B_have > 0)
							B_have --;
						else
							B_must ++;
					}
					else
						break;
				}
				else
					break;
			}
			

			if(A2B_leave.empty() && B2A_leave.empty() && A2B_arrive.empty() && B2A_arrive.empty() )
				break;
		}//end for( curtime...
		cout<<"Case #"<<i+1<<": "<<A_must<<" "<<B_must<<endl;
		fileOut<<"Case #"<<i+1<<": "<<A_must<<" "<<B_must<<endl;

	}
		
	fileIn.close();
	fileOut.close();

	char ch;
	scanf("%d",&ch);
}
