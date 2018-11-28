// timetable.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/* HH::MM format to minutes in int*/
static stringTimeTominutes(string time)
{
	string hr;
	string min;
	int minutes;

	hr= time.substr(0, time.find(":"));
	min = time.substr(time.find(":")+1);
	minutes = atoi(hr.c_str()) * 60 + atoi(min.c_str());
	minutes = minutes%(24*60); 
	return minutes;

};

class CtrainSchedule
{
	
	vector<int> availableTimeList; /* in minutes*/
	vector<int> requiredTimesList;/* in minutes*/
	int ntrains;
	
public:
	int trainsRequired(void)
	{
		ntrains = 0;
		vector<int>::iterator avaItr;
		vector<int>::iterator reqItr;

		sort(availableTimeList.begin(), availableTimeList.end());
		sort(requiredTimesList.begin(), requiredTimesList.end());
		
		bool breakh= false;

		for (reqItr = requiredTimesList.begin(); reqItr!= requiredTimesList.end(); reqItr++)
		{
			breakh= false;
			for (avaItr = availableTimeList.begin(); avaItr!= availableTimeList.end(); avaItr++)
			{
				if(*reqItr >= *avaItr)
				{
					//printf("\n\n TODE DELETED IS = %d", *avaItr);					
					availableTimeList.erase(avaItr, avaItr+1);	
					breakh = true;
					break;
				}
	
			}
			if(!breakh)
			{
				ntrains++;				
			}
		}

		return ntrains;
	}
	void addAvailableTime(int time)
	{
		availableTimeList.push_back(time); 
	}
	void addRequiredTime(int time)
	{
		requiredTimesList.push_back(time); 
	}
	void clear(void)
	{
		availableTimeList.clear();
		requiredTimesList.clear(); 
		ntrains = 0;
	}
};


int main()
{
	char str [151];
	FILE * fp = NULL ;
	FILE * fpout = NULL;
	int NA, NB, T;
	int testcases;
	string tmpstring;
	string arrival;
	string departure;
	class CtrainSchedule scheduleA, scheduleB;

	string inputfilename="c:\\input.txt"; /* provide input file */
	string outputfilename="c:\\output.txt";

	if ((fp = fopen(inputfilename.c_str(), "r")) < 0)
	{
		fprintf(stderr, "cannot create  %s\n",
			inputfilename.c_str());
		return -1;
	}
	
	/* Read # of testcases */
	fgets(str, 151, fp);
	testcases = atoi(str);

	for(int count=0;count<testcases; count++)
	{
		string tmpstring;
		fgets(str, 151, fp);
		T =atoi(str);
		fgets(str, 151, fp);
		tmpstring = str;
		NA = atoi(tmpstring.substr(0,tmpstring.find(" ")).c_str());
		NB = atoi(tmpstring.substr(tmpstring.find(" ")+1).c_str());
		scheduleA.clear();
		scheduleB.clear(); 

		for(int i=0; i<NA; i++)
		{
			fgets(str, 151, fp);
			tmpstring = str;
			departure = tmpstring.substr(0,tmpstring.find(" "));
			arrival = tmpstring.substr(tmpstring.find(" ")+1);
			
			scheduleA.addRequiredTime(stringTimeTominutes(departure)); 
			scheduleB.addAvailableTime(stringTimeTominutes(arrival)+ T); 
		}
		for(int i=0; i<NB; i++)
		{
			fgets(str, 151, fp);
			tmpstring = str;
			departure = tmpstring.substr(0,tmpstring.find(" "));
			arrival = tmpstring.substr(tmpstring.find(" ")+1);

			scheduleB.addRequiredTime(stringTimeTominutes(departure)); 
			scheduleA.addAvailableTime(stringTimeTominutes(arrival)+ T);
		}

		if(!fpout)
		{
			if ((fpout = fopen(outputfilename.c_str(), "w+")) < 0)
			{
				fprintf(stderr, "cannot open output file %s\n",
					outputfilename.c_str());
				return -1 ;
			}
		}

		fprintf(fpout, "Case #%d: %d %d\n",  count+1, scheduleA.trainsRequired(),scheduleB.trainsRequired());
		//printf("Case #%d: %d %d\n", count+1, scheduleA.trainsRequired(),scheduleB.trainsRequired());
	}
	fclose(fpout);
	fclose(fp);
	return 0;
}

