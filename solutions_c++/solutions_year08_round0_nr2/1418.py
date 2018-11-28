#include <iostream>
#include <vector>
using namespace std;

struct Trip {
    Trip(int d, int a, bool s) : depart(d), arrive(a), stationA(s) {}
    int depart;
    int arrive;
    bool stationA;
};

bool operator < (const Trip &lhs, const Trip &rhs) { return lhs.depart < rhs.depart; }

int main(int argc, char *argv[])
{
    int num_cases;
    cin >> num_cases;

    for (int i = 0 ; i < num_cases ; ++i) {
	int turnaround;
	cin >> turnaround;

	int NA, NB;
	cin >> NA;
        cin >> NB;

	vector<Trip> trips;

	for (int n = 0 ; n < NA ; ++n) {
	    int h, m;
	    char c;

	    cin >> h >> c >> m;
	    int t1 = h * 60 + m;

	    cin >> h >> c >> m;
	    int t2 = h * 60 + m;
	    trips.push_back(Trip(t1, t2, true));
	}

	for (int n = 0 ; n < NB ; ++n) {
	    int h, m;
	    char c;

	    cin >> h >> c >> m;
	    int t1 = h * 60 + m;

	    cin >> h >> c >> m;
	    int t2 = h * 60 + m;
	    trips.push_back(Trip(t1, t2, false));
	}

	// Sort trips by departure time
	sort(trips.begin(), trips.end());

	int numA(0), numB(0);
	while (!trips.empty()) {
	    // Add a train and delete first trip on list
	    Trip trip = trips.front();
	    if (trip.stationA) { ++numA; }
	    else { ++numB; }
	    trips.erase(trips.begin());

	    // Search rest of trips
	    bool stationA;
	    stationA = !trip.stationA;
	    int time = trip.arrive + turnaround;

	    int n = 0;
	    while (n < trips.size()) {
		const Trip &t = trips[n];
		if (t.stationA == stationA &&
	 	    t.depart >= time) {
		    // Train can take this trip, update status & erase
		    stationA = !t.stationA;
		    time = t.arrive + turnaround;

		    trips.erase(trips.begin() + n);
		}
		else {
		    ++n;
		}
	    }
	}

	cout << "Case #" << (i + 1) << ": " << numA << " " << numB << endl;
    }

    return 0;
}
