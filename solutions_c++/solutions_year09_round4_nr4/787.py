#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

struct plant {
	bool covered;
	double distA;
	double distB;
	int x;
	int y;
	int r;
};

bool compDists(pair<bool, plant*> a, pair<bool, plant*> b) {
	double da = a.first?a.second->distA:a.second->distB;
	double db = b.first?b.second->distA:b.second->distB;
	return da < db;
}


double plantDist(plant a, plant b) {
	int dx = a.x - b.x;
	int dy = a.y - b.y;
	return sqrt(dx * dx + dy * dy) + a.r + b.r;
}

int main (int argc, char * const argv[]) {
    cout << "Input file name: ";
	string filename;
	getline(cin, filename);
	
	cout << "Output file name: ";
	string outFileName;
	getline(cin, outFileName);
	
	ofstream out;
	out.open(outFileName.c_str());
	
	ifstream in;
	in.open(filename.c_str());
	
	if(in.fail()) {
		cout << "File not found" << endl;
		exit(1);
	}
	
	string params;
	getline(in, params);
	stringstream paramsStream;
	paramsStream << params;
	
	int T;
	
	paramsStream >> T;
	
	for(int i = 0; i < T; i++) {
		out << "Case #" << i + 1 << ": ";
		string size;
		getline(in, size);
		stringstream sizeStream;
		sizeStream << size;
		
		int N;
		sizeStream >> N;
		
		vector<plant> plants;
		
		for(int j = 0; j < N; j++) {
			plant newPlant;
			
			string thisRow;
			getline(in, thisRow);
			stringstream thisPS;
			thisPS << thisRow;
			thisPS >> newPlant.x >> newPlant.y >> newPlant.r;
			newPlant.covered = false;
			plants.push_back(newPlant);
		}
		
		int largestA = 0;
		int largestB = 0;
		double largestDist = 0;
		
		for(int j = 0; j < N; j++) {
			for(int k = 0; k < N; k++) {
				double dist = plantDist(plants[j], plants[k]);
				if(dist > largestDist) {
					largestA = j;
					largestB = k;
					largestDist = dist;
				}
			}
		}
		
		vector<pair<bool, plant*> > fromDists;
		for(int j = 0; j < N; j++) {
			plants[j].distA = plantDist(plants[j], plants[largestA]);
			plants[j].distB = plantDist(plants[j], plants[largestB]);
			fromDists.push_back(make_pair(false, &plants[j]));
			fromDists.push_back(make_pair(true, &plants[j]));
		}
		
		sort(fromDists.begin(), fromDists.end(), compDists);
		
		double diam = 0;
		
		for(int j = 0; j < fromDists.size(); j++) {
			if(!fromDists[j].second->covered) {
				fromDists[j].second->covered = true;
				diam = fromDists[j].first?fromDists[j].second->distA:fromDists[j].second->distB;
			}
		}
		
		
		out << fixed << setprecision(6) << diam / 2 << endl;
	}
	
	cout << "Done!";
	string dummy;
	getline(cin, dummy);
    return 0;
}
