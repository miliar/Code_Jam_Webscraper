//MaximZh
//Qualification_B.cpp

#include <stdio.h> //Standard C++ library

//Information of an event
struct TRAINEVENT
{
	int time; //Time of the event in minutes (0 - 24*60)
	int station; //Station index: "0" - A, "1" - B
	int code; //Code of the event: "0" - departure, "1" - ready to depart
};

//Compare events by time
bool IsLater(TRAINEVENT &ev1, TRAINEVENT &ev2)
{
	if( ev1.time == ev2.time )
	{
		return (ev1.code < ev2.code);
	}
	else return (ev1.time > ev2.time);
}

int main()
{
	int N = 0; //Number of cases
	TRAINEVENT events[400];	

	FILE *pfin = fopen("data.in", "rt");
	FILE *pfout = fopen("data.out", "wt");
	fscanf(pfin, "%d\n", &N); //Input number of cases
	for( int i = 0; i < N; i++ )
	{
		int T = 0; //Turnaround time
		int NA = 0;
		int NB = 0;
		fscanf(pfin, "%d", &T);
		fscanf(pfin, "%d %d", &NA, &NB);
		//Input the timetable and fill in events' data
		int k = 0;
		for( int j = 0; j < NA; j++ )
		{
			int h1, m1, h2, m2;
			fscanf(pfin, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			events[k].time = h1*60+m1;
			events[k].station = 0;
			events[k].code = 0;
			k++;
			events[k].time = h2*60+m2+T;
			events[k].station = 1;
			events[k].code = 1;			
			k++;			
		}
		for( int j = 0; j < NB; j++ )
		{
			int h1, m1, h2, m2;
			fscanf(pfin, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			events[k].time = h1*60+m1;
			events[k].station = 1;
			events[k].code = 0;
			k++;
			events[k].time = h2*60+m2+T;
			events[k].station = 0;
			events[k].code = 1;
			k++;			
		}
		int N = (NA + NB)*2; //Number of events
		//Sort the events
		int M = N-1;
		bool flag;
		do{
			flag = false;
			for( int j = 0; j < M; j++ )
				if( IsLater(events[j], events[j+1]) )
				{
					TRAINEVENT etmp = events[j];
					events[j] = events[j+1];
					events[j+1] = etmp;
					flag = true;
				}
			M--;
		}while( flag );
		//Calculate number of trains
		int NtrA = 0; //Number of trains that must start at A
		int NtrB = 0; //Number of trains that must start at B
		int NtrAcurr = 0; //Number of trains at A ready to return
		int NtrBcurr = 0; //Number of trains at B ready to return
		for( int j = 0; j < N; j++ )
			if( events[j].station == 0 )
				if( events[j].code == 0 )
					if( NtrAcurr > 0 )
						NtrAcurr--;
					else
						NtrA++;
				else
					NtrAcurr++;
			else
				if( events[j].code == 0 )
					if( NtrBcurr > 0 )
						NtrBcurr--;
					else
						NtrB++;
				else
					NtrBcurr++;
		fprintf(pfout, "Case #%d: %d %d\n", i+1, NtrA, NtrB);
	}
	fclose(pfout);
	fclose(pfin);
	return 0;
}