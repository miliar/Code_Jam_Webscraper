#ifndef TRAIN_COUNTER_H
#define TRAIN_COUNTER_H

#include <set>
#include "TrainEvent.h"
using namespace std;

class TrainCounter
{
private:
	int turnaroundTime;
	multiset<TrainEvent> timeTableA;
	multiset<TrainEvent> timeTableB;

	int getRequiredTrains(multiset<TrainEvent>& timeTable);
public:
	TrainCounter(const int turnaroundTime);

	void addTripFromAToB(const int departureTime, const int arrivalTime);
	void addTripFromBToA(const int departureTime, const int arrivalTime);

	void getNumOfRequiredTrains(int& requiredTrainsA, int& requiredTrainsB);
};

#endif