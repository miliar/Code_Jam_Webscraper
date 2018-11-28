/************************/
/*	GCJ 2008		     */
/*	Matthew D Sandy       */
/************************/

#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <list>
#include <time.h>

using namespace std;

int getTimeStamp(string timeString);

int main(int argc, char **argv)
{
	ifstream inFile;
	inFile.open(argv[1]);
	if(inFile.is_open()) cout<<"Opened \""<<argv[1]<<"\" for read...\n";
	else {cout<<"Error opening \""<<argv[1]<<"\" for read...\n"; return 1;}
	ofstream outFile;
	outFile.open(argv[2]);
	if(inFile.is_open()) cout<<"Opened \""<<argv[2]<<"\" for write...\n";
	else {cout<<"Error opening \""<<argv[2]<<"\" for write...\n"; return 1;}
	
	//////////////////////BEGIN CODE//////////////////////
	/*Train Timetable
	Begin needing no trains at all.
	Read in the timetable and for each line, add one event timestamp to each of two vectors; needed_X, and ready_X (where X is A or B)
	insert these in order of increasing time.
	Once the vectors are populated, look at the least unprocessed timestamp out of all vectors
	process all events in the ready vectors at this timestamp, and remove them from the list once processed.
	when a train is ready at X, increment the trainsatX value
	process all events in the needed vectors at this timestamp, and remove them from the list once processed.
	when a train is needed at X, if there is none available, increment the startX value, otherwise decrement the trainsatX value
	once all events at this timestamp are processed, look for the next timestamp and repeat the loop.
	loop until all vectors are empty
	*/
	
	int numCases;
	inFile >> numCases;
	
	for(int i=1;i<=numCases;i++)
	{	//for each test case...
		cout<<"Now processing case #"<<i<<"\n";
		int turnaround;
		inFile >> turnaround;	//turnaround tme
		int NA, NB;
		inFile >> NA;	//number of A=>B schedules
		inFile >> NB;	//number of B=>A schedules
		string timeString;
		list<int> needed_A,needed_B,ready_A,ready_B;
		list<int>::iterator it;
		cout<<"Now reading "<<NA<<" A-to-B paths\n";
		for(int j=0;j<NA;j++)
		{
			inFile >> timeString;
			needed_A.push_back(getTimeStamp(timeString));
			inFile >> timeString;
			ready_B.push_back(getTimeStamp(timeString) + turnaround);
		}
		cout<<"Now reading "<<NB<<" B-to-A paths\n";
		for(int j=0;j<NB;j++)
		{
			inFile >> timeString;
			needed_B.push_back(getTimeStamp(timeString));
			inFile >> timeString;
			ready_A.push_back(getTimeStamp(timeString) + turnaround);
		}
		
		needed_A.sort();
		needed_B.sort();
		ready_A.sort();
		ready_B.sort();
		
		cout<<"Trains will be needed at A at:\n";
		for(it=needed_A.begin();it!=needed_A.end();it++)
		{
			cout<<"\t"<<*it<<endl;
		}
		cout<<"Trains will be needed at B at:\n";
		for(it=needed_B.begin();it!=needed_B.end();it++)
		{
			cout<<"\t"<<*it<<endl;
		}
		cout<<"Trains will be ready at A at:\n";
		for(it=ready_A.begin();it!=ready_A.end();it++)
		{
			cout<<"\t"<<*it<<endl;
		}
		cout<<"Trains will be ready at B at:\n";
		for(it=ready_B.begin();it!=ready_B.end();it++)
		{
			cout<<"\t"<<*it<<endl;
		}

		//values loaded in, begin processing
		
		int startA = 0;
		int startB = 0;
		int trainsatA = 0;
		int trainsatB = 0;
		while(!(needed_A.empty() && needed_B.empty() && ready_A.empty() && ready_B.empty()))
		{	int timeStamp = 144000;
			if(!needed_A.empty() && timeStamp > needed_A.front()) timeStamp = needed_A.front();
			if(!needed_B.empty() && timeStamp > needed_B.front()) timeStamp = needed_B.front();
			if(!ready_A.empty() && timeStamp > ready_A.front()) timeStamp = ready_A.front();
			if(!ready_B.empty() && timeStamp > ready_B.front()) timeStamp = ready_B.front();
			cout<<"Looking for Ready A events at "<<timeStamp<<endl;
			while(!ready_A.empty() && int(ready_A.front()) == timeStamp)
			{
				trainsatA++;	//increment trains at A
				ready_A.pop_front();	//pop this event off
			}
			cout<<"Looking for Ready B events at "<<timeStamp<<endl;
			while(!ready_B.empty() && int(ready_B.front()) == timeStamp)
			{
				trainsatB++;	//increment trains at A
				ready_B.pop_front();	//pop this event off
			}
			cout<<"Looking for Needed A events at "<<timeStamp<<endl;
			while(!needed_A.empty() && int(needed_A.front()) == timeStamp)
			{
				if(trainsatA)	//if there are trains at A
					trainsatA--;	//decrease by 1
				else			//otherwise
					startA++;	//increase required starting A trains by 1
				needed_A.pop_front();	//pop this event off
			}
			cout<<"Looking for Needed B events at "<<timeStamp<<endl;
			while(!needed_B.empty() && int(needed_B.front()) == timeStamp)
			{
				if(trainsatB)	//if there are trains at B
					trainsatB--;	//decrease by 1
				else			//otherwise
					startB++;	//increase required starting B trains by 1
				needed_B.pop_front();	//pop this event off
			}
		}
		
		//once we're done, write the output
		outFile<<"Case #"<<i<<": "<<startA<<" "<<startB<<"\n";
	}
	
	//////////////////////END CODE//////////////////////
	
	inFile.close();
	outFile.close();
}

int engineID(string* engines, string query)
{	//returns the engine ID for a given query string
	int i=0;
	while(1)
	{
		if(engines[i]==query) return i;
		i++;
	}
}

int getTimeStamp(string timeString)
{
	//returns the number of minutes since 00:00
	struct tm timeStruct;
	strptime(timeString.c_str(),"%H:%M",&timeStruct);
	return timeStruct.tm_hour * 60 + timeStruct.tm_min;
}
