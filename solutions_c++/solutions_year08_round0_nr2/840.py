/*
   Code Jam Problem B: Train Timetable.
   7/16/08  10:49 p.m.
   by John Alway
*/
#include "stdio.h"
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

//Structure to hold start or end time, and start position
struct STimes {
	long minutes; //time of start or end
	bool Start; //true of an end time, false if a start time
	bool A; //True if starting from A, false if from B
};

//////////////////////////////////////////////////////////////////////
//Compare function for sorting train times in order
//////////////////////////////////////////////////////////////////////
bool cmpr(STimes &a,STimes &b)
{
	if(a.minutes < b.minutes) return true;	 
	else return false; 
}

//Sort items so that Start=false come before
//items with Start = true;
bool cmpr2(STimes &a,STimes &b)
{
	if(a.Start == true && b.Start == false) return false;
	return true;	 
}
void SortEndStart(vector<STimes> &trips,int begin,int end)
{
	STimes temp;
	int len;
 
	len = end - begin;
	for(int i=0; i<len ;i++)
	{
		int cnt=0;
		for(int j=begin; j<end; j++){
			if(trips[j].Start == true && trips[j+1].Start == false)
			{
				temp = trips[j];
				trips[j] = trips[j+1];
				trips[j+1] = temp;
				cnt++;
			}
		}
		if(cnt == 0) break;
	}
}


//Tack the five minutes onto the end.
//Passed back the number of trains that start from A in FromA, and from B in FromB.
void CalculateNumberOfTrainsAndLocation(vector<STimes> &trips,long TurnAroundTime,long &FromA,long &FromB)
{
	long minute=0L;
	vector<STimes>::iterator p;
	long v;
	int m, n;
	int vsize=trips.size();
	long cntA=0, cntB=0;  //count the trains that start from A and B respectively.
	long atA=0, atB=0;   //keep track of the number of trains at A and B currently.
 
	//Tack on turnaround time to ending times
	for(int i=0; i < vsize; i++) {
		if(trips[i].Start == false)
			trips[i].minutes += TurnAroundTime;		 
	}

	//Sort times in order from earliest to latest
	sort(trips.begin(),trips.end(),cmpr);
 
	//Sort the elements with the same time
	//so that the end times come before the
	//start times
	for(int i=0;i<(vsize-1);i++){
		v = trips[i].minutes;
		m = n = i;
		while(v==trips[i+1].minutes){
			i++;
			n++;
			if(i >= (vsize-1)) break;
		}
		if(n > m){
			SortEndStart(trips,m,n);	 
			i = n;
		} 
	}

	for(int i=0; i < vsize; i++) {

		//Is time a start time?
		if(trips[i].Start){ //Start Time, is a train available or must one be added?
			if(trips[i].A){ //must start from A
				if(atA == 0){
					cntA++;
				}else{
					atA--;
				}
			}else{  //must start from B				
				if(atB == 0){
					cntB++;
				}else{
					atB--;
				}
			}
		}
		else{  //End Time, makes a train available
			if(trips[i].A) { // Must end at B
				atB++;				
			}else{  //Must end at A
				atA++;
			}
		}
	}
	FromA = cntA;
	FromB = cntB;
}

//Extract Hour and Minute from xy:ab time formate
//and return total in minutes;
long parseTime(char *pTime)
{

	char *p;
	char hour[5], minute[5];
	long hr, mn;
	int i=0;

	p = pTime;
 
	while(*p != ':'){	 
		hour[i++] = *(p++);
	}
	p++;
	hour[i] = '\0';	 
	sscanf(hour,"%ld",&hr);		
 
	i=0;
	while(*p != '\0'){
		minute[i++] = *(p++);
	}
	minute[i] = '\0';
	sscanf(minute,"%ld",&mn);

	mn += hr*60L;

	return mn;
}

int main()
{
	vector<STimes> tripsData;
	int idx=1;
	int cnt=0;
	long TurnAroundTime, FromA, FromB, Tm;
	char begtime[30], endtime[30];
	int NA, NB;
	char str[350], buf[20]; 	 
	char *p;
	string dataOut;
	STimes Trip;	 
	int infile=0;
  
	//ifstream in("B-small-attempt1.in");
	ifstream in("B-large.in");
	//ifstream in("TestTrain2.in");

	if(!in){
		cout << "Cannot Open file.\n" << endl;
		return 1;
	}

	//ofstream out("BSmallout.txt");
	ofstream out("Blargeout.txt");
	//ofstream out("TestTrainOut.txt");

	if(!out){
		cout << "Cannot Open Output File.\n" << endl;
		return 1;
	}

	in.getline(str,349);
	sscanf(str,"%d",&cnt);

	

	while(in){
		TurnAroundTime=FromA=FromB=0L;

		in.getline(str, 349);
		sscanf(str,"%ld",&TurnAroundTime);

		
		in.getline(str, 349);
		sscanf(str,"%d%d",&NA,&NB);

		for(int i=0;i<NA;i++){
			in.getline(str, 349);
			sscanf(str,"%s%s",begtime,endtime);			 

			//Start Time
			Tm = parseTime(begtime);			
			Trip.A = true;
			Trip.Start = true;
			Trip.minutes = Tm;
			tripsData.push_back(Trip);

			//End Time			 	 
			Tm = parseTime(endtime);
			Trip.A = true;
			Trip.Start = false;
			Trip.minutes = Tm;
			tripsData.push_back(Trip);
		}

		for(int i=0;i<NB;i++){
			in.getline(str, 349);
			sscanf(str,"%s%s",begtime,endtime);
		 
			//Start Time
			Tm = parseTime(begtime);
			Trip.A = false;
			Trip.Start = true;
			Trip.minutes = Tm;
			tripsData.push_back(Trip);

			//End Time			 
			Tm = parseTime(endtime);
			Trip.A = false;
			Trip.Start = false;
			Trip.minutes = Tm;
			tripsData.push_back(Trip);
		}
	 


		CalculateNumberOfTrainsAndLocation(tripsData,TurnAroundTime,FromA,FromB);

				 
		sprintf(buf,"Case #%d: ",idx++);
		dataOut = buf;
		sprintf(buf,"%ld %ld",FromA,FromB);
		dataOut += buf;

		cout << dataOut << endl;
	    
		dataOut += "\r";

		out.write(dataOut.c_str(),dataOut.length());
		tripsData.clear();
		if(idx > cnt) break;
	}

	out.close();
	in.close();

	return 0;
}