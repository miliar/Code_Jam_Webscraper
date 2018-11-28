#include<iostream>
#include<string>
#include<fstream>

using namespace std;
#define MAX_TRIP 100
#define MAX_TIME 1440
struct TRIP {
	int departure;
	int arrival;
	bool scheduled;
};
int timeToInt(string time)
{
	return 60*atoi((time.substr(0,2)).c_str())+atoi((time.substr(3,2)).c_str());
}
int globalearliest(TRIP A[], int NA, TRIP B[], int NB)
{ //we give back the position of the earliest not sheduled train
  // the B positions starts from NA
	int earliest=MAX_TIME; //(24:00)
	int position=-1;
	for(int i=0;i<NA;i++)
		if(!A[i].scheduled && A[i].departure<earliest)
		{
			earliest=A[i].departure;
			position=i;
		}
	for(int i=0;i<NB;i++)
		if(!B[i].scheduled && B[i].departure<earliest)
		{
			earliest=B[i].departure;
			position=NA+i;
		}
	return position;
}
int findNext(int time, TRIP T[], int NT)
{
	int position=-1;
	int earliest=MAX_TIME;
	for(int i=0;i<NT;i++)
		if(!T[i].scheduled && T[i].departure>=time && T[i].departure<earliest)
		{
			earliest=T[i].departure;
			position=i;
		}
	return position;
}
void main (void)
{
	ifstream myinput;
	ofstream myoutput;
	int N;
	int T;
	int NA;
	int NB;
	int TA;
	int TB;
	string arrival="";
	string departure="";
	TRIP TNA[MAX_TRIP];
	TRIP TNB[MAX_TRIP];
	myinput.open("input.txt");
	myoutput.open("output.txt");
	myinput>>N;
	for(int i=0;i<N;i++)
	{
		myinput>>T>>NA>>NB;
		for(int j=0;j<NA;j++)
		{
			departure="";arrival="";
			myinput>>departure>>arrival;
			TNA[j].arrival=timeToInt(arrival);
			TNA[j].departure=timeToInt(departure);
			TNA[j].scheduled=false;
		}
		for(int j=0;j<NB;j++)
		{
			string departure,arrival;
			departure="";arrival="";
			myinput>>departure>>arrival;
			TNB[j].arrival=timeToInt(arrival);
			TNB[j].departure=timeToInt(departure);
			TNB[j].scheduled=false;
		}
		TA=0;
		TB=0;
		//we read the problem, now solve it :)
		//we should found the earliest departure
		//we should start with that city
		int position;
		bool inA;
		do
		{
			position=globalearliest(TNA,NA,TNB,NB);
			int time;
			if(0<=position && position<NA)
			{ //starting from city A
				TA++;
				inA=true;
				time=TNA[position].arrival+T;
				TNA[position].scheduled=true;
			}
			else if(NA<=position && position<NA+NB)
			{ //starting from city B
				position-=NA;
				TB++;
				inA=false;
				time=TNB[position].arrival+T;
				TNB[position].scheduled=true;
			}
			int nextposition;
			bool isnext=true;
			while(isnext)
			{
				if(inA)
				{
					nextposition=findNext(time,TNB, NB);
					inA=false;
				}
				else
				{
					nextposition=findNext(time,TNA, NA);
					inA=true;
				}

				if(nextposition==-1)
					isnext=false;
				else
				{
					if(inA)
					{
						TNA[nextposition].scheduled=true;
						time=TNA[nextposition].arrival+T;
					}
					else
					{
						TNB[nextposition].scheduled=true;
						time=TNB[nextposition].arrival+T;
					}
				}
			}

		}
		while(position>-1);

		//now we should print out the results
		myoutput<<"Case #"<<i+1<<": "<<TA<<" "<<TB<<endl;
	}
}