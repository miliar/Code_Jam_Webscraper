
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <map>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

void readTimes(ifstream &fin, int cnt, int tt, vector<int> &deps, vector<int> &arvs) {
	char tmp[100], ttime[20];
	unsigned int dt, at;

	for(int i=0; i<cnt; i++) {

		fin.getline(tmp, 100);
		istringstream s1(tmp);

		s1.getline(ttime, 20, ':');
		dt = atoi(ttime) * 60;
		s1.getline(ttime, 20, ' ');
		dt += atoi(ttime);

		s1.getline(ttime, 20, ':');
		at = atoi(ttime) * 60;
		s1.getline(ttime, 20);
		at += atoi(ttime);
		at += tt;

		deps.push_back(dt);
		arvs.push_back(at);
	}
}

void trainTimetable(string input_file) {

	int no_tcs, tt, na, nb, startA, startB;
	char tmp[50], tmp2[50];
	ifstream fin(input_file.c_str());
	ofstream fout("output_file");

	vector<int> Adeps;
	vector<int> Aarvs;
	vector<int> Bdeps;
	vector<int> Barvs;

	fin.getline(tmp, 50);
	no_tcs = atoi(tmp);

	for(int i=0; i<no_tcs; i++) {

		startA = 0;
		startB = 0;

		fin.getline(tmp, 50);
		tt = atoi(tmp);

		fin.getline(tmp, 50);
		istringstream s1(tmp);

		s1.getline(tmp2, 50, ' ');
		na = atoi(tmp2);

		s1.getline(tmp2, 50);
		nb = atoi(tmp2);

		if(na != 0 && nb != 0) {

			Adeps.clear();
			Aarvs.clear();
			Bdeps.clear();
			Barvs.clear();

			readTimes(fin, na, tt, Adeps, Barvs);
			readTimes(fin, nb, tt, Bdeps, Aarvs);

			sort(Adeps.begin(), Adeps.end());
			sort(Aarvs.begin(), Aarvs.end());
			sort(Bdeps.begin(), Bdeps.end());
			sort(Barvs.begin(), Barvs.end());

			int Ain = 0, Bin = 0;
			for(int j=0; j<na; j++) {
				if(Ain < nb && Aarvs[Ain] <= Adeps[j]) {
					Ain++;
				} else {
					startA++;
				}
			}

			for(int j=0; j<nb; j++) {
				if(Bin < na && Barvs[Bin] <= Bdeps[j]) {
					Bin++;
				} else {
					startB++;
				}
			}
		} else {
			if(na) startA = na;
			if(nb) startB = nb;
		}

		fout << "Case #" << i+1 << ": " << startA << " " << startB << endl;
	}

	cout << "Output File: ./output_file";
}

int main() {

	string input_file;
	cout << "Enter the path of the input_file: ";
	cin >> input_file;
	trainTimetable(input_file);

}
