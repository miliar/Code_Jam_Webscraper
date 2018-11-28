#include <fstream>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

struct Time {
	int hr;
	int min;
};

struct Trip {
	Time depart;
	Time arrive;
	char start;
};

struct Train {
	char dest;
	Time eta;
};

bool tripCompare(Trip a, Trip b) {
	return (a.depart.hr > b.depart.hr || (a.depart.hr == b.depart.hr && a.depart.min > b.depart.min));
}

int main()
{
	int N, NA, NB, T, aTrains, bTrains, aStartTrains, bStartTrains, i, j;
	vector<Trip> trips;
	list<Train> activeTrains;
	char line[256];
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	fin >> N;
	for (i = 0; i < N; ++i) {
		fin >> T >> NA >> NB;
		fin.ignore();
		trips.clear();
		for (j = 0; j < NA; ++j) {
			fin.getline(line, 256);
			Trip newTrip;
			sscanf(line, "%d:%d %d:%d", &newTrip.depart.hr, &newTrip.depart.min, &newTrip.arrive.hr, &newTrip.arrive.min);
			newTrip.start = 'A';
			trips.push_back(newTrip);
		}
		for (j = 0; j < NB; ++j) {
			fin.getline(line, 256);
			Trip newTrip;
			sscanf(line, "%d:%d %d:%d", &newTrip.depart.hr, &newTrip.depart.min, &newTrip.arrive.hr, &newTrip.arrive.min);
			newTrip.start = 'B';
			trips.push_back(newTrip);
		}
		sort(trips.begin(), trips.end(), tripCompare);
		activeTrains.clear();
		aTrains = aStartTrains = bTrains = bStartTrains = 0;
		for (j = 0; j < NA+NB; ++j) {
			Trip currentTrip = trips.back();
			trips.pop_back();

			list<Train>::iterator it = activeTrains.begin();
			while (it != activeTrains.end()) {
				if (it->eta.hr < currentTrip.depart.hr || (it->eta.hr == currentTrip.depart.hr && it->eta.min <= currentTrip.depart.min)) {
					if (it->dest == 'A')
						++aTrains;
					else
						++bTrains;
					it = activeTrains.erase(it);
				} else {
					++it;
				}
			}

			if (currentTrip.start == 'A') {
				if (aTrains == 0) {
					++aStartTrains;
					++aTrains;
				}
				Train newTrain;
				newTrain.dest = 'B';
				newTrain.eta = currentTrip.arrive;
				newTrain.eta.min += T;
				if (newTrain.eta.min > 59) {
					++newTrain.eta.hr;
					newTrain.eta.min -= 60;
				}
				activeTrains.push_back(newTrain);
				--aTrains;
			} else {
				if (bTrains == 0) {
					++bStartTrains;
					++bTrains;
				}
				Train newTrain;
				newTrain.dest = 'A';
				newTrain.eta = currentTrip.arrive;
				newTrain.eta.min += T;
				if (newTrain.eta.min > 59) {
					++newTrain.eta.hr;
					newTrain.eta.min -= 60;
				}
				activeTrains.push_back(newTrain);
				--bTrains;
			}
		}
		fout << "Case #" << i+1 << ": " << aStartTrains << ' ' << bStartTrains;
		if (i != N-1)
			fout << endl;
	}
	return 0;
}