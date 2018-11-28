#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
A train timetable specifies departure and arrival time of all trips between A and B. 
The train company needs to know how many trains have to start the day at A and B in order to make the timetable work: 
whenever a train is supposed to leave A or B, there must actually be one there ready to go. 
There are passing sections on the track, so trains don't necessarily arrive in the same order that they leave.

sort and search, type
sort by out-time, sort by in-time

	vector<train*> listIn;
	temp = new train();
	temp->inTime = "09:00";
	temp->outTime = "12:00";
	temp->type = 0;
	listIn.push_back(temp);

	temp = new train();
	temp->inTime = "10:00";
	temp->outTime = "13:00";
	temp->type = 0;
	listIn.push_back(temp);

	temp = new train();
	temp->inTime = "11:00";
	temp->outTime = "12:30";
	temp->type = 0;
	listIn.push_back(temp);

	vector<train *> listOut;

	temp = new train();
	temp->inTime = "12:02";
	temp->outTime = "15:00";
	temp->type = 0;
	listOut.push_back(temp);

	temp = new train();
	temp->inTime = "09:00";
	temp->outTime = "10:30";
	temp->type = 0;
	listOut.push_back(temp);
*/

#if 1


struct trainType
{
	string inTime;
	string outTime;
	int type;
};
typedef struct trainType train; 

bool less_than(const trainType * m1, const trainType * m2) {
	 if(m1->outTime.compare(m2->outTime) < 0)
		 return true;
	 else
		 return false;
}

bool less_than_in(const trainType * m1, const trainType * m2) {
	 if(m1->inTime.compare(m2->inTime) < 0)
		 return true;
	 else
		 return false;
}

int compareTime(string m1, string m2, int time)
{

	int val1 = ((m1[0]-48) * 10 + (m1[1] - 48))*60 + ((m1[3]-48) * 10 + (m1[4] - 48));
	int val2 = ((m2[0]-48) * 10 + (m2[1] - 48))*60 + ((m2[3]-48) * 10 + (m2[4] - 48));
	if(val2 - val1 >= time)
		return 1;
	else
		return 0;
}

int main()
{
	cout << "this is timetable program!" <<endl;

	int num, total, ANum,BNum;
	int resultA,resultB;
	int returnTime;
	string inTime, outTime;

	vector<string> AInTime, AOutTime;
	vector<string> BInTime, BOutTime;
	train* temp;
	
	vector<train*> listIn;	
	vector<train*> listOut;

	ifstream fin("B-large.in");
	ofstream fout("B-large.in.out");

	//num = 1;
	fin >> num;

	//total = 5;
	//ANum = 3;
	//BNum = 2;
	//returnTime = 5;


	int i,j;
	for(int count = 0; count<num;count++)
	{
		fin >> returnTime;
		fin >> ANum;
		fin >> BNum;
		
	resultA = ANum;
	resultB = BNum;

		for(i=0; i<ANum; i++)
		{
			temp = new train();
			fin >> inTime;
			fin >> outTime;
			temp->inTime = inTime;
			temp->outTime = outTime;
			temp->type = 0;
			listIn.push_back(temp);
		}

		for(i=0; i<BNum; i++)
		{
			temp = new train();
			fin >> inTime;
			fin >> outTime;
			temp->inTime = inTime;
			temp->outTime = outTime;
			temp->type = 0;
			listOut.push_back(temp);
		}


		if(ANum<=0 || BNum<=0)
		{
			fout << "Case #"<< count+1 <<": " << ANum <<" "<<BNum <<endl;
			return 0;
		}

		sort(listIn.begin(),listIn.end(),less_than);
	    sort(listOut.begin(),listOut.end(),less_than_in);
		for(i=0; i<ANum; i++)
		{
			for(j=0; j<BNum; j++)
			{
				if(compareTime(listIn[i]->outTime, listOut[j]->inTime,returnTime) == 1 && listIn[i]->type == 0 && listOut[j]->type == 0)
				{
					resultB--;
					listIn[i]->type = 1;
					listOut[j]->type = 1;
				}
			}
		}
		
		for(int m=0; m<ANum; m++)
		{
			listIn[m]->type = 0;
		}
		for(int n=0; n<BNum; n++)
		{
			listOut[n]->type = 0;
		}
		sort(listIn.begin(),listIn.end(),less_than_in);
	    sort(listOut.begin(),listOut.end(),less_than);

		for( i=0; i<BNum; i++)
		{
			for( j=0; j<ANum; j++)
			{
				if(compareTime(listOut[i]->outTime, listIn[j]->inTime,returnTime) == 1 && listIn[j]->type == 0 && listOut[i]->type == 0)
				{
					resultA--;
					listIn[j]->type = 1;
					listOut[i]->type = 1;
				}
			}
		}

		fout << "Case #"<< count+1 <<": " << resultA <<" "<<resultB <<endl;
		listOut.clear();
		listIn.clear();
	}

	fin.close();
	fout.close();

	return 0;
}

#endif