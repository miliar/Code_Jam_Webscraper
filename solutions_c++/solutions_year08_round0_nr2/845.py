#include <iostream>
#include <list>
using namespace std;

struct trip
{
	unsigned int departure, arrival;
	bool done;
	bool operator<(const trip &t1) {return this->departure < t1.departure;}
};
void read(unsigned int &num, list<trip> &trains, unsigned int &T);
void goA(list<trip> &trainsA, list<trip> &trainsB, unsigned int arrival, unsigned int &completed);
void goB(list<trip> &trainsA, list<trip> &trainsB, unsigned int arrival, unsigned int &completed);

int main(void)
{
	unsigned int num_cases;

	cin >> num_cases;
	for(unsigned int c = 1; c <= num_cases; c++)
	{
		list<trip> trainsA, trainsB;
		list<trip>::iterator itA, itB, endA, endB;
		unsigned int T, NA, NB, TA = 0, TB = 0, completed = 0;

		cin >> T >> NA >> NB;
		read(NA, trainsA, T);
		read(NB, trainsB, T);
		trainsA.sort(); trainsB.sort();

		itA = trainsA.begin(), itB = trainsB.begin(), endA = trainsA.end(), endB = trainsB.end();
		while(completed < NA + NB)
		{
			while(itA != endA && itA->done) itA++;
			while(itB != endB && itB->done) itB++;

			if(itA == endA)
			{
				TB += NA + NB - completed;
				completed += TB;
			}
			else if(itB == endB)
			{
				TA += NA + NB - completed;
				completed += TA;
			}
			else if(*itA < *itB)
			{
				itA->done = true; TA++; completed++;
				goB(trainsA, trainsB, itA->arrival, completed);
			}
			else
			{
				itB->done = true; TB++; completed++;
				goA(trainsA, trainsB, itB->arrival, completed);
			}
		}

		cout << "Case #" << c << ": " << TA << " " << TB << endl;
	}
}

void read(unsigned int &num, list<trip> &trains, unsigned int &T)
{
	trip aux;
	unsigned int hour, minute;

	for(unsigned int i = 0; i < num; i++)
	{
		scanf("%u:%u", &hour, &minute);
		aux.departure = 60 * hour + minute;

		scanf("%u:%u", &hour, &minute);
		aux.arrival = 60 * hour + minute + T;

		aux.done = false;
		trains.push_back(aux);
	}
}
void goA(list<trip> &trainsA, list<trip> &trainsB, unsigned int arrival, unsigned int &completed)
{
	list<trip>::iterator it = trainsA.begin(), end = trainsA.end();

	while(it != end)
	{
		if(it->done == false && it->departure >= arrival)
		{
			it->done = true; completed++;
			goB(trainsA, trainsB, it->arrival, completed);
			break;
		}
		it++;
	}
}
void goB(list<trip> &trainsA, list<trip> &trainsB, unsigned int arrival, unsigned int &completed)
{
	list<trip>::iterator it = trainsB.begin(), end = trainsB.end();

	while(it != end)
	{
		if(it->done == false && it->departure >= arrival)
		{
			it->done = true; completed++;
			goA(trainsA, trainsB, it->arrival, completed);
			break;
		}
		it++;
	}
}
