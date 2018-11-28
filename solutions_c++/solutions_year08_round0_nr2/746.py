
#include <stdio.h>
#include <string.h>
#include <list>

struct Event {
	int time;
	int event;
};

/* events */
#define READY_A 0
#define READY_B 1
#define LEAVE_A 2
#define LEAVE_B 3

class Simulator {

	int trainsAtA;
	int trainsAtB;
	int minTrainsAtA;
	int minTrainsAtB;
	std::list<Event>	eventList;

public:

	Simulator() : trainsAtA(0), trainsAtB(0), minTrainsAtA(0), minTrainsAtB(0) { }

	void addEvent(int time, int event) {

		/* add this event into list */
		Event anEvent;

		anEvent.time = time;
		anEvent.event = event;

		/* do insertion sort, make sure that trains becoming available happen before departing trains!!! */
		std::list<Event>::iterator iterator = eventList.begin();
		while (iterator != eventList.end()) {
			if (iterator->time > time) break;
			if (iterator->time == time) {
				if (iterator->event > event) break;
			}
			iterator++;
		}
		int temp = iterator->time;
		int temp2 = iterator->event;
		eventList.insert(iterator, anEvent);
	}

	void simulate() {

		/* go through sorted list, process each event, updating tran values as we go.
		 * if trainsAtX is ever less than minTrainsAtX, update minTrainsAtX.
		 * when done, -minTrainsAtX is how many you need to start
		 */
		while (eventList.size()) {
			Event event = eventList.front();
			switch (event.event) {
				case LEAVE_A: {
					trainsAtA--;
					if (trainsAtA < minTrainsAtA) minTrainsAtA = trainsAtA;
					break;
				}
				case READY_B: {
					trainsAtB++;
					break;
				}
				case LEAVE_B: {
					trainsAtB--;
					if (trainsAtB < minTrainsAtB) minTrainsAtB = trainsAtB;
					break;
				}
				case READY_A: {
					trainsAtA++;
					break;
				}
			}
			eventList.pop_front();
		}
	}

	int getMinTrainsAtA() { return -minTrainsAtA; }
	int getMinTrainsAtB() { return -minTrainsAtB; }
};

#define MAX_MINUTES (60*24)

int main(int argc, char** argv) {

	/* First argument is the file to open and process */
	FILE* inputFile;
	int numCases;

	inputFile = fopen("D:\\incoming\\B-large.in", "r");

	/* first token is number of test cases */
	fscanf(inputFile, "%d", &numCases);

	FILE* outputFile = fopen("C:\\output.txt", "w");
	for (int loop = 0; loop < numCases; loop++) {

		int turnAroundTime;
		int tripsFromA;
		int tripsFromB;
		int hourDepart;
		int minuteDepart;
		int hourArrive;
		int minuteArrive;
		int departMinute;
		int readyMinute;
		int loop2;
		Simulator simulator;

		fscanf(inputFile, "%d", &turnAroundTime);
		fscanf(inputFile, "%d %d", &tripsFromA, &tripsFromB);
		for (loop2 = 0; loop2 < tripsFromA; loop2++) {
			fscanf(inputFile, "%d:%d %d:%d", &hourDepart, &minuteDepart, &hourArrive, &minuteArrive);
			departMinute = minuteDepart + (60 * hourDepart);
			simulator.addEvent(departMinute, LEAVE_A);
			readyMinute = minuteArrive + (60 * hourArrive) + turnAroundTime;
			if (readyMinute < MAX_MINUTES) {
				simulator.addEvent(readyMinute, READY_B);
			}
		}
		for (loop2 = 0; loop2 < tripsFromB; loop2++) {
			fscanf(inputFile, "%d:%d %d:%d", &hourDepart, &minuteDepart, &hourArrive, &minuteArrive);
			departMinute = minuteDepart + (60 * hourDepart);
			simulator.addEvent(departMinute, LEAVE_B);
			readyMinute = minuteArrive + (60 * hourArrive) + turnAroundTime;
			if (readyMinute < MAX_MINUTES) {
				simulator.addEvent(readyMinute, READY_A);
			}
		}

		simulator.simulate();
		printf("Case #%d: %d %d\n", loop + 1, simulator.getMinTrainsAtA(), simulator.getMinTrainsAtB());
		fprintf(outputFile, "Case #%d: %d %d\n", loop + 1, simulator.getMinTrainsAtA(), simulator.getMinTrainsAtB());
	}
	fclose(outputFile);

	return 0;
}