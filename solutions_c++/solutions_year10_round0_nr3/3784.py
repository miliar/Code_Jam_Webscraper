#include <iostream>

#include <vector>
#include <list>
#include <fstream>
#include <sstream>

using namespace std;

/*
struct Snapper {
	Snapper(Snapper* parent = 0, bool on = false, bool power = false)
		:Parent(parent), On(on), Power(power) {}

	Snapper* Parent;

	bool On;
	bool Power;

	void Toggle() {

		On = !On;

		if(Parent != 0 && Parent->On && On) {
			Power = true;
		}
	}
}
*/

vector<string> tokenize(string str) {

	stringstream ss(str);

	string token;
	vector<string> tokens;

	while( getline(ss, token, ' ') ) {
		tokens.push_back(token);
	}

	return tokens;

}

int toInt(string str) {
	stringstream ss(str);
	int i;
	ss >> i;
	return i;
}

struct Rollercoaster {
	int RidesPerDay;
	int PeoplePerRide;
};

struct RideCase {
	Rollercoaster coaster;
	list<int> Groups;
};

int main() {

	ifstream file("C-small-attempt0.in");
	if(!file.is_open()) {
		cout << "Failed to open file!" << endl;
		return 0;
	}

	ofstream out("out.out");

	int nInputs;
	//int nGroups;
	list<int> groups;	

	string line;

	getline(file, line);
	vector<string> tokens = tokenize(line);
	nInputs = toInt(tokens[0]);

	vector<RideCase> cases;

	int money = 0;

	for(int i = 0; i < nInputs; ++i) {
		vector<string> line1, line2;
		getline(file, line);
		line1 = tokenize(line);
		getline(file, line);
		line2 = tokenize(line);
		
		Rollercoaster roller;
		roller.RidesPerDay = toInt(line1[0]);
		roller.PeoplePerRide = toInt(line1[1]);

		
		int nGroups = toInt(line1[2]);
		
		list<int> groups;

		for(int j = 0; j < nGroups; ++j) {
			groups.push_back( toInt(line2[j]) );
		}
		
		RideCase rc;
		rc.coaster = roller;
		rc.Groups = groups;

		// cases.push_back(rc);

		for(int j = 0; j < roller.RidesPerDay; ++j) {
			int nPassengers = 0;
			// vector<int> riding;
			// int nGroups = groups.size();
			// int queue = groups.size();
			int groupsWent = 0;

			while(nPassengers < roller.PeoplePerRide) {
				int nG = groups.front();

				if(groupsWent < nGroups && nPassengers + nG <= roller.PeoplePerRide) {
					nPassengers += nG;
					groups.pop_front();
					// riding.push_back(nG);

					money += nG;
					groupsWent += 1;
				} else {
					break;
				}

				groups.push_back(nG);
			}
		}

		cout << "Case #" << i+1 << ": " << money << endl;
		out << "Case #" << i+1 << ": " << money << endl;
		money = 0;
	}

	getchar();
	return 0;
}