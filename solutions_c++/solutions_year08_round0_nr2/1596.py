/*
	B. Train Timeable
	Google Code Jam '08 - Qualification Round
	- n@p [ 17-Jul-2008 ]
	Note: This code was written and debugged on Microsoft Visual Studio version 6.0
*/

#include<iostream.h>
#include<string.h>

#define MAX_TRIPS 100 //max values of nA & nB
#define MAX_MINS 1500 //total mins in a day=24*60=1440+max value of T (60)
					  //..used to define Timelines; each minute represents a discrete slice of time

struct TrainTrip
{
	int dep, arr; //times to be stored in minutes .. simplify life
};

void main()
{
	char dep_str[6], arr_str[6]; //will input times as character string, and then parse it
	char hh_str[3], mm_str[3];
	hh_str[2]=mm_str[2]='\0'; //set the end-of-string char to NULL, once and for all

	int dep_hh, dep_mm, arr_hh, arr_mm;

	struct TrainTrip tripAB[MAX_TRIPS], tripBA[MAX_TRIPS];
	int timelineA[MAX_MINS], timelineB[MAX_MINS]; //stores delta of no. of available trains at any point of time
	int stA, stB; //st=starting trains (number of trains initially needed at A & B)
	int lastEventA, lastEventB;

	int n, cases, T, nA, nB, i, last;
	cin>>cases; //scanf("%d",&cases);
	for(n=1;n<=cases;n++)
	{
		//init...
		memset((void *)timelineA, 0, sizeof(int)*MAX_MINS);
		memset((void *)timelineB, 0, sizeof(int)*MAX_MINS);
		stA=0;
		stB=0;
		lastEventA=-1;
		lastEventB=-1;
		
		//input turnaround time...
		cin>>T;
		
		//input nA & nB...
		cin>>nA>>nB;

		//input trains departing A...
		for(i=0;i<nA;i++)
		{
			cin>>dep_str>>arr_str;
			
			//parse dep_str...
			hh_str[0]=dep_str[0];
			hh_str[1]=dep_str[1];

			mm_str[0]=dep_str[3];
			mm_str[1]=dep_str[4];

			dep_hh=(hh_str[0]-'0')*10 + (hh_str[1]-'0'); //small atoi hack ;)
			dep_mm=(mm_str[0]-'0')*10 + (mm_str[1]-'0');

			//parse arr_str...
			hh_str[0]=arr_str[0];
			hh_str[1]=arr_str[1];

			mm_str[0]=arr_str[3];
			mm_str[1]=arr_str[4];

			arr_hh=(hh_str[0]-'0')*10 + (hh_str[1]-'0'); //small atoi hack ;)
			arr_mm=(mm_str[0]-'0')*10 + (mm_str[1]-'0');

			//store train data... [for trains departing A]
			tripAB[i].dep=dep_hh*60+dep_mm; //times converted to minutes
			tripAB[i].arr=arr_hh*60+arr_mm+T; //add turnaround time to arrivals .. again, simplify life
			if(lastEventA<tripAB[i].dep)
				lastEventA=tripAB[i].dep;
			if(lastEventB<tripAB[i].arr)
				lastEventB=tripAB[i].arr;

			//update delta timelines...for each trip from A to B, decrement A at dep & increment B at arr
			timelineA[tripAB[i].dep]--;
			timelineB[tripAB[i].arr]++;
		}

		//input trains departing B...
		for(i=0;i<nB;i++)
		{
			cin>>dep_str>>arr_str;
			
			//parse dep_str...
			hh_str[0]=dep_str[0];
			hh_str[1]=dep_str[1];

			mm_str[0]=dep_str[3];
			mm_str[1]=dep_str[4];

			dep_hh=(hh_str[0]-'0')*10 + (hh_str[1]-'0'); //small atoi hack ;)
			dep_mm=(mm_str[0]-'0')*10 + (mm_str[1]-'0');

			//parse arr_str...
			hh_str[0]=arr_str[0];
			hh_str[1]=arr_str[1];

			mm_str[0]=arr_str[3];
			mm_str[1]=arr_str[4];

			arr_hh=(hh_str[0]-'0')*10 + (hh_str[1]-'0'); //small atoi hack ;)
			arr_mm=(mm_str[0]-'0')*10 + (mm_str[1]-'0');

			//store train data... [for trains departing B]
			tripBA[i].dep=dep_hh*60+dep_mm; //times converted to minutes
			tripBA[i].arr=arr_hh*60+arr_mm+T; //add turnaround time to arrivals .. again, simplify life
			if(lastEventB<tripBA[i].dep)
				lastEventB=tripBA[i].dep;
			if(lastEventA<tripBA[i].arr)
				lastEventA=tripBA[i].arr;

			//update delta timelines...for each trip from B to A, decrement B at dep & increment A at arr
			timelineB[tripBA[i].dep]--;
			timelineA[tripBA[i].arr]++;
		}

		//need to sort train data...? nope!

		//de-delta-fy timelines and increment st counts... yup!
		last=0;
		for(i=0;i<=lastEventA;i++)
		{
			if(timelineA[i]==0)
				timelineA[i]=last;
			else
			{
				timelineA[i]+=last;
				if(timelineA[i]<0) //trains present at a station cant b negative
				{
					stA+= -(timelineA[i]); //number of more trains needed equals the amount of deficit
					timelineA[i]=0; //after fulfilling the deficit,assuming these trains were there initially
				}

				//while(timelineA[i]<0) //trains present at a station cant b negative
				//{
				//	timelineA[i]++; //need to increment till we reach zero
				//	stA++; //..as many trains more needed from beginning
				//}
				last=timelineA[i];
			}
		}

		last=0;
		for(i=0;i<=lastEventB;i++)
		{
			if(timelineB[i]==0)
				timelineB[i]=last;
			else
			{
				timelineB[i]+=last;
				if(timelineB[i]<0) //trains present at a station cant b negative
				{
					stB+= -(timelineB[i]); //number of more trains needed equals the amount of deficit
					timelineB[i]=0; //after fulfilling the deficit,assuming these trains were there initially
				}

				//while(timelineB[i]<0) //trains present at a station cant b negative
				//{
				//	timelineB[i]++; //need to increment till we reach zero
				//	stB++; //..as many trains more needed from beginning
				//}
				last=timelineB[i];
			}
		}

/* ...debug checks...* /
cout<<endl<<"timelineA[]="<<endl;
for(i=0;i<=lastEventA;i++)
	cout<<timelineA[i];
//..checked ok

cout<<endl<<"timelineB[]="<<endl;
for(i=0;i<=lastEventB;i++)
	cout<<timelineB[i]; //checked ok
//..checked ok

cout<<endl;
for(i=0;i<nA;i++)
	cout<<tripAB[i].dep/60<<":"<<tripAB[i].dep%60<<" "<<tripAB[i].arr/60<<":"<<tripAB[i].arr%60<<endl;
//..checked ok

for(i=0;i<nB;i++)
	cout<<tripBA[i].dep/60<<":"<<tripBA[i].dep%60<<" "<<tripBA[i].arr/60<<":"<<tripBA[i].arr%60<<endl;
//..checked ok
/ *................... */

	//DONE:
		cout<<"Case #"<<n<<": "<<stA<<" "<<stB<<endl;
	}

}