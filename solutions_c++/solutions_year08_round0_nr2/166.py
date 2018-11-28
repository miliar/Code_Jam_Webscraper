#include <stdio.h>
#include <string.h>
#include "general.h"

#define STATUS_EN_ROUTE_TO_A 1
#define STATUS_A 2
#define STATUS_B 3
#define STATUS_EN_ROUTE_TO_B 4

#define EVENT_A_DEPARTURE 1
#define EVENT_A_ARRIVAL 2
#define EVENT_B_DEPARTURE 3
#define EVENT_B_ARRIVAL 4


class Time
{
public:
	int hour_;
	int minute_;

	Time() {}

	Time(int hour, int minute)
	{
		hour_ = hour;
		minute_ = minute;
	}

	Time(Time& time)
	{
		hour_ = time.hour_;
		minute_ = time.minute_;
	}

	int operator==(Time& time2)
	{
		return hour_ == time2.hour_ && minute_ == time2.minute_;
	}

	Time operator+(int minute)
	{
		int h = hour_, m = minute_;

		m += minute;
		while(m >= 60)
		{
			m -= 60;
			h ++;
		}
		return Time(h, m);
	}

	int operator>= (Time& time2)
	{
		if(hour_ > time2.hour_)
			return 1;
		else if(hour_ < time2.hour_)
			return 0;
		else
		{
			if(minute_ >= time2.minute_)
				return 1;
		}
		return 0;
	}

	int operator> (Time& time2)
	{
		if(hour_ > time2.hour_)
			return 1;
		else if(hour_ < time2.hour_)
			return 0;
		else
		{
			if(minute_ > time2.minute_)
				return 1;
		}
		return 0;
	}

	int operator<= (Time& time2)
	{
		if(hour_ < time2.hour_)
			return 1;
		else if(hour_ > time2.hour_)
			return 0;
		else
		{
			if(minute_ <= time2.minute_)
				return 1;
		}
		return 0;
	}

	int operator< (Time& time2)
	{
		if(hour_ < time2.hour_)
			return 1;
		else if(hour_ > time2.hour_)
			return 0;
		else
		{
			if(minute_ < time2.minute_)
				return 1;
		}
		return 0;
	}

};

class Train
{
public:
	int status_;

	Train() {}

	Train(int status) : status_(status) {}
};


class EventStruct
{
public:
	int id_event_;
	Time time_;
	
	EventStruct() {}

	EventStruct(int id_event, Time& time) : id_event_(id_event), time_(time) {}
};

void InsertEvent(Queue< EventStruct >& qevent, EventStruct * es)
{
	int i = 0;

	while(1)
	{
		if(i >= qevent.GetSize())
			break;

		if(es->id_event_ == EVENT_A_DEPARTURE || es->id_event_ == EVENT_B_DEPARTURE)
		{
			if(es->time_ < qevent[i].time_)
			{
				qevent.InsertAs(es, i);
				break;
			}
		}
		else
		{
			if(es->time_ <= qevent[i].time_)
			{
				qevent.InsertAs(es, i);
					break;
			}
		}
		i++;
	}
	if(i >= qevent.GetSize())
	{
			qevent.InsertAs(es, qevent.GetSize());
	}
}

int SeekTrain(Queue< Train >& qtrain, int status)
{
	for(int i = 0; i < qtrain.GetSize(); i++)
	{
		if(qtrain[i].status_ == status)
			return i;
	}
	return -1;
}


void SetStatus(Queue< Train >& qtrain, int status, int index)
{
	qtrain[index].status_ = status;
}

void Run(Queue< EventStruct >& qevent, int & n1, int & n2)
{
	Queue< Train > qtrain;
	EventStruct * es;
	int index;

	n1 = 0;
	n2 = 0;

	while(!qevent.IsEmpty())
	{
		es = qevent.DeQueue();
		switch(es->id_event_)
		{
		case EVENT_A_DEPARTURE:
			index = SeekTrain(qtrain, STATUS_A);
			if(index >= 0)
			{
				SetStatus(qtrain, STATUS_EN_ROUTE_TO_B, index);
			}
			else
			{
				qtrain.EnQueue(new Train(STATUS_EN_ROUTE_TO_B));
				n1 ++;
			}
			break;
			
		case EVENT_B_DEPARTURE:
			index = SeekTrain(qtrain, STATUS_B);
			if(index >= 0)
			{
				SetStatus(qtrain, STATUS_EN_ROUTE_TO_A, index);
			}
			else
			{
				qtrain.EnQueue(new Train(STATUS_EN_ROUTE_TO_A));
				n2 ++;
			}
			break;

		case EVENT_A_ARRIVAL:
			index = SeekTrain(qtrain, STATUS_EN_ROUTE_TO_A);
			SetStatus(qtrain, STATUS_A, index);
			break;

		case EVENT_B_ARRIVAL:
			index = SeekTrain(qtrain, STATUS_EN_ROUTE_TO_B);
			SetStatus(qtrain, STATUS_B, index);
			break;
		}
		delete es;
	}
}

int main(int argc, char ** argv)
{
	int ncases;
	int extra_minute;
	int nab, nba;
	int n1, n2;
	int h1, m1, h2, m2;
	FILE * fpin, * fpout;

	Queue< EventStruct >* qevent1, * qevent;

	if(argc < 3)
	{
		printf("Requires in and out filename!\n");
		return 0;
	}

	fpin = fopen(argv[1], "r");
	fpout = fopen(argv[2], "w");

	fscanf(fpin, "%d", &ncases);
	for(int k = 0; k < ncases; k++)
	{
		fscanf(fpin, "%d", &extra_minute);
		fscanf(fpin, "%d", &nab);
		fscanf(fpin, "%d", &nba);
		qevent = new Queue< EventStruct >;
		qevent1 = new Queue< EventStruct >;

		for(int i = 0; i < nab; i++)
		{
			fscanf(fpin, "%d:%d%d:%d", &h1, &m1, &h2, &m2);
			qevent1->EnQueue(new EventStruct(EVENT_A_DEPARTURE, Time(h1, m1)));
			qevent1->EnQueue(new EventStruct(EVENT_B_ARRIVAL, Time(h2, m2) + extra_minute));

		}
		for(int i = 0; i < nba; i++)
		{
			fscanf(fpin, "%d:%d%d:%d", &h1, &m1, &h2, &m2);
			qevent1->EnQueue(new EventStruct(EVENT_B_DEPARTURE, Time(h1, m1)));
			qevent1->EnQueue(new EventStruct(EVENT_A_ARRIVAL, Time(h2, m2) + extra_minute));
		}

		while(!qevent1->IsEmpty())
		{
			InsertEvent(*qevent, qevent1->DeQueue());
		}

		Run(*qevent, n1, n2);

		fprintf(fpout, "Case #%d: %d %d\n", k + 1, n1, n2);

		delete qevent;
		delete qevent1;
	}

	fclose(fpin);
	fclose(fpout);


	return 0;
}










		
