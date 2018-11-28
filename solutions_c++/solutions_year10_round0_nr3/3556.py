#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <queue>
#include "arraylist.h"
using namespace std;

void start(char* input) {
	ifstream openfile (input);
	ofstream tofile ("C-small-attempt0.out");

	string sCases;
	getline(openfile, sCases);
	int cases = atoi(sCases.c_str());

	for (int n=1;n<=cases;n++) {
		string sRides;
		getline(openfile, sRides, ' ');
		int rides = atoi(sRides.c_str());

		string sPeople;
		getline(openfile, sPeople, ' ');
		int maxPeople = atoi(sPeople.c_str());

		string sGroups;
		getline(openfile,sGroups);
		int groups = atoi(sGroups.c_str());

		queue<int> q;
		for (int g=0;g<groups;g++) {
			string sGroup;
			if (g != groups-1)
				getline(openfile, sGroup, ' ');
			else
				getline(openfile, sGroup);
			int group = atoi(sGroup.c_str());
			q.push(group);
		}

		int euros = 0;
		for (int r=0;r<rides;r++) {
			//for (Object o: q)
			//	System.out.print(o + " ");
			//System.out.println();
			int currentPeople = 0;
			arraylist<int> peopleUsed;
			int size = q.size();

			int count = 0;
			while (count < size && (currentPeople + q.front() <= maxPeople)) {
				int p = q.front();
				q.pop();
				peopleUsed.add(p);
				currentPeople += p;
				count++;
			}

			euros += currentPeople;
			for (int i=0;i<peopleUsed.length();i++)
				q.push(peopleUsed[i]);

		}

		cout << "Case #" << n << ": " << euros << "\n";
		tofile << "Case #" << n << ": " << euros << "\n";

	}
	openfile.close();
	tofile.close();
}

int main(int argc, char** argv) {
	start("C-small-attempt0.in"); //change class
	return 0;
}